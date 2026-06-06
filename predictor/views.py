import math
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# ─── Modelo matemático ────────────────────────────────────────────────
# Pesos calibrados manualmente según el planteamiento del proyecto.
# z = w1·asistencia + w2·promedio + w3·horas + w4·trabajos + w5·participacion + w6·concentracion + b
PESOS = {
    'asistencia':     2.5,
    'promedio':       3.0,
    'horas_estudio':  1.8,
    'trabajos':       1.5,
    'participacion':  1.2,
    'concentracion':  1.0,
}
BIAS = -7.2


def sigmoid(z: float) -> float:
    """σ(z) = 1 / (1 + e^(-z))"""
    return 1 / (1 + math.exp(-z))


def derivada_sigmoide(z: float) -> float:
    """σ'(z) = σ(z) · (1 − σ(z))  →  sensibilidad de cada variable"""
    s = sigmoid(z)
    return s * (1 - s)


def calcular_prediccion(datos: dict) -> dict:
    """Calcula z, probabilidad y análisis de sensibilidad."""
    # Normalizar entradas a rango [0, 1]
    asistencia    = datos['asistencia'] / 100         # 0–100 %
    promedio      = datos['promedio'] / 100            # 0–100 pts
    horas_estudio = datos['horas_estudio'] / 40        # 0–40 h/sem
    trabajos      = datos['trabajos'] / 10             # 0–10 trabajos
    participacion = datos['participacion'] / 5         # 0–5 nivel
    concentracion = datos['concentracion'] / 5         # 0–5 nivel

    norm = {
        'asistencia':     asistencia,
        'promedio':       promedio,
        'horas_estudio':  horas_estudio,
        'trabajos':       trabajos,
        'participacion':  participacion,
        'concentracion':  concentracion,
    }

    # Combinación lineal
    z = BIAS + sum(PESOS[k] * norm[k] for k in PESOS)

    probabilidad = sigmoid(z)
    porcentaje = round(probabilidad * 100, 1)

    # Derivadas parciales → sensibilidad (cuánto mueve cada variable)
    ds_dz = derivada_sigmoide(z)
    sensibilidades = {k: round(PESOS[k] * ds_dz * 100, 2) for k in PESOS}

    # Factores positivos y negativos
    positivos = []
    negativos = []

    if datos['asistencia'] >= 80:
        positivos.append(f"✔ Alta asistencia ({datos['asistencia']}%) — favorece la aprobación.")
    elif datos['asistencia'] < 60:
        negativos.append(f"✖ Asistencia baja ({datos['asistencia']}%) — riesgo alto de reprobación.")

    if datos['promedio'] >= 60:
        positivos.append(f"✔ Promedio actual de {datos['promedio']} pts está sobre la nota mínima.")
    else:
        negativos.append(f"✖ Promedio de {datos['promedio']} pts por debajo de la nota de aprobación.")

    if datos['horas_estudio'] >= 10:
        positivos.append(f"✔ {datos['horas_estudio']} h/semana de estudio — dedicación adecuada.")
    elif datos['horas_estudio'] < 5:
        negativos.append(f"✖ Solo {datos['horas_estudio']} h/semana de estudio — insuficiente.")

    if datos['trabajos'] >= 7:
        positivos.append(f"✔ {datos['trabajos']} trabajos entregados — buen cumplimiento.")
    elif datos['trabajos'] < 4:
        negativos.append(f"✖ Solo {datos['trabajos']} trabajos entregados — baja entrega.")

    if datos['participacion'] >= 4:
        positivos.append("✔ Alta participación en clases — indicador positivo.")
    elif datos['participacion'] <= 2:
        negativos.append("✖ Participación baja en clases.")

    if datos['concentracion'] >= 4:
        positivos.append("✔ Buenos hábitos de concentración y estudio.")
    elif datos['concentracion'] <= 2:
        negativos.append("✖ Hábitos de concentración deficientes.")

    # Generar la expresión z extendida
    formula_z_str = f"z = {BIAS}"
    formula_z_str += f" + {PESOS['asistencia']}*{norm['asistencia']:.3f}"
    formula_z_str += f" + {PESOS['promedio']}*{norm['promedio']:.3f}"
    formula_z_str += f" + {PESOS['horas_estudio']}*{norm['horas_estudio']:.3f}"
    formula_z_str += f" + {PESOS['trabajos']}*{norm['trabajos']:.3f}"
    formula_z_str += f" + {PESOS['participacion']}*{norm['participacion']:.3f}"
    formula_z_str += f" + {PESOS['concentracion']}*{norm['concentracion']:.3f}"

    return {
        'z': round(z, 4),
        'formula_z_str': formula_z_str,
        'porcentaje': porcentaje,
        'positivos': positivos,
        'negativos': negativos,
        'sensibilidades': sensibilidades,
    }


# ─── Vistas ───────────────────────────────────────────────────────────

def index(request):
    return render(request, 'predictor/index.html')


@csrf_exempt
def predecir(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            resultado = calcular_prediccion({
                'asistencia':    float(datos.get('asistencia', 0)),
                'promedio':      float(datos.get('promedio', 0)),
                'horas_estudio': float(datos.get('horas_estudio', 0)),
                'trabajos':      float(datos.get('trabajos', 0)),
                'participacion': float(datos.get('participacion', 0)),
                'concentracion': float(datos.get('concentracion', 0)),
            })
            return JsonResponse({'ok': True, **resultado})
        except Exception as e:
            return JsonResponse({'ok': False, 'error': str(e)}, status=400)
    return JsonResponse({'ok': False, 'error': 'Método no permitido'}, status=405)
