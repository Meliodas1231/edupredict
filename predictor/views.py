import math
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import GuiaReparto


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

    # Generar recomendaciones personalizadas con mínimos
    recomendaciones = []
    
    # 1. Asistencia (min_ok = 80%)
    asist_val = datos['asistencia']
    if asist_val >= 80:
        recomendaciones.append({
            'tipo': 'bueno',
            'titulo': 'Asistencia',
            'descripcion': f"Tu asistencia es excelente ({asist_val}%). Sigue asistiendo a todas tus clases para no perder el hilo de las explicaciones y participar activamente.",
            'icono': '✅'
        })
    elif asist_val >= 60:
        dif = 80 - asist_val
        recomendaciones.append({
            'tipo': 'mejorar',
            'titulo': 'Asistencia',
            'descripcion': f"Tu asistencia es regular ({asist_val}%). Necesitas mejorarla en al menos {dif:.1f}% para alcanzar el nivel óptimo recomendado (80%). La asistencia es clave para la aprobación.",
            'icono': '⚠️'
        })
    else:
        dif = 80 - asist_val
        recomendaciones.append({
            'tipo': 'critico',
            'titulo': 'Asistencia Crítica',
            'descripcion': f"Alerta: Tu asistencia es críticamente baja ({asist_val}%). Debes subir tu asistencia en al menos {dif:.1f}% para llegar al 80% mínimo recomendado y evitar la reprobación por inasistencias.",
            'icono': '🚨'
        })

    # 2. Promedio (min_ok = 70 pts para seguro, 60 pts para aprobado básico)
    prom_val = datos['promedio']
    if prom_val >= 70:
        recomendaciones.append({
            'tipo': 'bueno',
            'titulo': 'Promedio Académico',
            'descripcion': f"Tu promedio es sólido ({prom_val} pts). Continúa manteniendo esta disciplina en tus evaluaciones para consolidar tu aprobación.",
            'icono': '✅'
        })
    elif prom_val >= 60:
        dif = 70 - prom_val
        recomendaciones.append({
            'tipo': 'mejorar',
            'titulo': 'Promedio Aceptable',
            'descripcion': f"Tu promedio es de {prom_val} pts. Aunque está aprobado, te recomendamos subir tu promedio en al menos {dif:.1f} pts para alcanzar un margen seguro (70 pts).",
            'icono': '⚠️'
        })
    else:
        dif_aprob = 60 - prom_val
        dif_seguro = 70 - prom_val
        recomendaciones.append({
            'tipo': 'critico',
            'titulo': 'Promedio Insuficiente',
            'descripcion': f"Tu promedio actual es reprobatorio ({prom_val} pts). Como mínimo absoluto debes subir {dif_aprob:.1f} pts para alcanzar la nota mínima de 60 pts, e idealmente {dif_seguro:.1f} pts para estar a salvo.",
            'icono': '🚨'
        })

    # 3. Horas de estudio semanal (min_ok = 10 horas)
    horas_val = datos['horas_estudio']
    if horas_val >= 10:
        recomendaciones.append({
            'tipo': 'bueno',
            'titulo': 'Horas de Estudio',
            'descripcion': f"Dedicas un buen tiempo al estudio ({horas_val} h/semana). Mantén este valioso hábito de estudio independiente para afianzar tus conocimientos.",
            'icono': '✅'
        })
    elif horas_val >= 5:
        dif = 10 - horas_val
        recomendaciones.append({
            'tipo': 'mejorar',
            'titulo': 'Horas de Estudio',
            'descripcion': f"Estudias {horas_val} h/semana. Te sugerimos incrementar al menos {dif:.1f} horas adicionales de estudio a la semana para llegar a la meta mínima de 10 h/semana.",
            'icono': '⚠️'
        })
    else:
        dif = 10 - horas_val
        recomendaciones.append({
            'tipo': 'critico',
            'titulo': 'Horas de Estudio Críticas',
            'descripcion': f"Tu dedicación es muy baja ({horas_val} h/semana). Incrementa tu estudio en al menos {dif:.1f} horas semanales para alcanzar el mínimo sugerido de 10 horas.",
            'icono': '🚨'
        })

    # 4. Trabajos entregados (min_ok = 7 trabajos)
    trabajos_val = datos['trabajos']
    if trabajos_val >= 8:
        recomendaciones.append({
            'tipo': 'bueno',
            'titulo': 'Entregas de Trabajos',
            'descripcion': f"Tienes un excelente cumplimiento en la entrega de tareas ({trabajos_val}/10). Sigue con este excelente nivel de cumplimiento.",
            'icono': '✅'
        })
    elif trabajos_val >= 4:
        dif = 7 - trabajos_val
        recomendaciones.append({
            'tipo': 'mejorar',
            'titulo': 'Entrega de Trabajos',
            'descripcion': f"Has entregado {trabajos_val}/10 trabajos. Deberías entregar al menos {dif} trabajo(s) más para alcanzar el mínimo ideal de 7 entregados y asegurar ese puntaje.",
            'icono': '⚠️'
        })
    else:
        dif = 7 - trabajos_val
        recomendaciones.append({
            'tipo': 'critico',
            'titulo': 'Entrega de Trabajos Crítica',
            'descripcion': f"Solo has entregado {trabajos_val}/10 trabajos. Es urgente que entregues al menos {dif} trabajo(s) adicionales para llegar al mínimo aceptable de 7 entregados.",
            'icono': '🚨'
        })

    # 5. Participación en clases (min_ok = 3/5)
    part_val = datos['participacion']
    if part_val >= 4:
        recomendaciones.append({
            'tipo': 'bueno',
            'titulo': 'Participación en Clases',
            'descripcion': f"Tu participación en clase es alta ({part_val}/5). Esto te ayuda a internalizar los conceptos e interactuar mejor con los temas explicados.",
            'icono': '✅'
        })
    elif part_val == 3:
        recomendaciones.append({
            'tipo': 'mejorar',
            'titulo': 'Participación en Clases',
            'descripcion': f"Tu nivel de participación es de {part_val}/5. Deberías intentar aumentar tu participación en al menos 1 nivel (llegar a 4/5) para consolidar tu proceso de aprendizaje activo.",
            'icono': '⚠️'
        })
    else:
        recomendaciones.append({
            'tipo': 'critico',
            'titulo': 'Baja Participación',
            'descripcion': f"Tu participación es muy baja ({part_val}/5). Intenta incrementarla en al menos 2 niveles para alcanzar un nivel saludable (mínimo de 3/5 o 4/5). Preguntar dudas sencillas es un buen inicio.",
            'icono': '🚨'
        })

    # 6. Hábitos de concentración (min_ok = 3/5)
    conc_val = datos['concentracion']
    if conc_val >= 4:
        recomendaciones.append({
            'tipo': 'bueno',
            'titulo': 'Hábitos de Concentración',
            'descripcion': f"Tus hábitos de concentración son excelentes ({conc_val}/5). Continúa estudiando en áreas libres de distracciones y con enfoque estructurado.",
            'icono': '✅'
        })
    elif conc_val == 3:
        recomendaciones.append({
            'tipo': 'mejorar',
            'titulo': 'Hábitos de Concentración',
            'descripcion': f"Tu concentración es regular ({conc_val}/5). Intenta mejorar tus hábitos en al menos 1 nivel (meta de 4/5) organizando tus sesiones de estudio y desconectando el celular.",
            'icono': '⚠️'
        })
    else:
        recomendaciones.append({
            'tipo': 'critico',
            'titulo': 'Enfoque Deficiente',
            'descripcion': f"Tu concentración al estudiar es baja ({conc_val}/5). Necesitas aumentar tu nivel de enfoque en al menos 2 niveles utilizando técnicas de estudio estructuradas como Pomodoro.",
            'icono': '🚨'
        })

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
        'recomendaciones': recomendaciones,
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


GUIA_REPARTO_CLAVE = 'equipo'


@csrf_exempt
@require_http_methods(['GET', 'POST', 'DELETE'])
def guia_reparto(request):
    """GET/POST/DELETE reparto de la guía de presentación (persistido en SQLite)."""
    if request.method == 'GET':
        obj = GuiaReparto.objects.filter(clave=GUIA_REPARTO_CLAVE).first()
        if not obj:
            return JsonResponse({
                'ok': True,
                'slides': {},
                'parts': {},
                'customized': False,
            })
        return JsonResponse({
            'ok': True,
            'slides': obj.slides,
            'parts': obj.partes,
            'customized': bool(obj.slides or obj.partes),
            'updated_at': obj.modificado_en.isoformat(),
        })

    if request.method == 'DELETE':
        GuiaReparto.objects.filter(clave=GUIA_REPARTO_CLAVE).delete()
        return JsonResponse({'ok': True})

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'ok': False, 'error': 'JSON inválido'}, status=400)

    slides = payload.get('slides') or {}
    parts = payload.get('parts') or {}
    if not isinstance(slides, dict) or not isinstance(parts, dict):
        return JsonResponse({'ok': False, 'error': 'slides y parts deben ser objetos'}, status=400)

    valid = {'aron', 'paola', 'victor', 'todos'}
    for key, val in {**slides, **parts}.items():
        if val not in valid:
            return JsonResponse({'ok': False, 'error': f'Integrante no válido: {val}'}, status=400)

    obj, _ = GuiaReparto.objects.update_or_create(
        clave=GUIA_REPARTO_CLAVE,
        defaults={'slides': slides, 'partes': parts},
    )
    return JsonResponse({
        'ok': True,
        'updated_at': obj.modificado_en.isoformat(),
    })
