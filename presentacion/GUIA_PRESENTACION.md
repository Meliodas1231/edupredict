# EduPredict — Guía de presentación y demo

**Integrantes:** Aron Barrientos · Víctor Gangas · Paola Pereira  
**Carrera:** Ingeniería en Informática · **Asignatura:** Cálculo Diferencial  
**URL demo:** http://127.0.0.1:8000/

> **Acceso rápido:** haz **5 clics** en el título **EduPredict** en la página principal.

---

## Orden sugerido del video (10–15 min)

| Min | Quién | Qué |
|-----|-------|-----|
| 0–2 | Aron | Qué es EduPredict + problemática |
| 2–5 | Paola | Modelo matemático (z, sigmoide) |
| 5–8 | Aron | Demo: formulario + resultado |
| 8–11 | Víctor | Derivadas, sensibilidades, factores |
| 11–13 | Víctor | GeoGebra paso a paso |
| 13–15 | Todos | Conclusiones + área TFL |

---

# PARTE 1 — Aron Barrientos
## Introducción y recorrido por la interfaz

### Qué decir al inicio (30 s)

> “Somos el equipo de EduPredict. Desarrollamos una aplicación web que estima la **probabilidad de aprobación** de un estudiante usando **6 variables académicas** y conceptos de **Cálculo Diferencial**: combinación lineal, función sigmoide, límites, continuidad y derivadas.”

### Encabezado de la página

| Elemento | Qué es | Qué decir |
|----------|--------|-----------|
| **EduPredict** | Nombre del producto | Predictor de rendimiento académico estudiantil |
| Subtítulo | Enfoque matemático | Basado en sigmoide, derivadas y combinación lineal |
| Temas (Oscuro / Claro / Rosa) | Preferencia visual | No afecta el cálculo; solo la interfaz |

### Sección: Datos del estudiante (formulario izquierdo)

**Qué hace:** Recibe 6 entradas con sliders. Al enviar, llama al servidor Django (`POST /predecir/`).

| Variable | Rango | Peso en el modelo | Qué decir |
|----------|-------|-------------------|-----------|
| Asistencia | 0–100 % | 2,5 | Mayor impacto junto al promedio |
| Promedio | 0–100 pts | 3,0 | Peso más alto |
| Horas de estudio | 0–40 h/sem | 1,8 | Esfuerzo sostenido |
| Trabajos entregados | 0–10 | 1,5 | Cumplimiento |
| Participación | 0–5 | 1,2 | Variable cualitativa |
| Concentración | 0–5 | 1,0 | Hábitos de estudio |

**Ejemplo para demo:** Asistencia 98 %, Promedio 60, Horas 24, Trabajos 7/10, Participación 5/5, Concentración 3/5.

**Botón “Calcular predicción”:** Envía JSON al backend → Python ejecuta `calcular_prediccion()` → devuelve porcentaje, sensibilidades y factores.

### Sección: Resultado (gauge)

| Elemento | Qué muestra |
|----------|-------------|
| Gauge semicircular | Probabilidad % (ej. 72,7 %) |
| Veredicto | ≥ 70 % alta probabilidad; ≥ 50 % en riesgo; &lt; 50 % reprobación |
| Fórmula | `z = … → σ(z) = …` |

**Qué decir:**

> “El servidor calcula **z** (combinación lineal), aplica la **sigmoide** y nos da un porcentaje entre 0 y 100.”

---

# PARTE 2 — Paola Pereira
## Modelo matemático y sigmoide

### Paso 1 — Normalización

- asistencia ÷ 100 · promedio ÷ 100 · horas ÷ 40 · trabajos ÷ 10 · participación ÷ 5 · concentración ÷ 5

### Paso 2 — Combinación lineal

```
z = −7,2 + 2,5·asist + 3,0·prom + 1,8·horas + 1,5·trab + 1,2·part + 1,0·conc
```

### Paso 3 — Función sigmoide

```
σ(z) = 1 / (1 + e^(−z))
P = σ(z) × 100
```

**Qué decir:**

> “La sigmoide convierte **z** en probabilidad. Los **límites** evitan salir de 0 % y 100 %. La **continuidad** hace que al mover un slider el cambio sea gradual.”

### Curva sigmoide (gráfico en la app)

| Parte | Significado |
|-------|-------------|
| Eje X = z | Combinación lineal |
| Eje Y = σ(z) | Probabilidad 0–1 |
| Punto ● | Estudiante actual (z₀, σ(z₀)) |
| Línea en 0,5 | Zona de incertidumbre |

---

# PARTE 3 — Víctor Gangas
## Derivadas, sensibilidades y factores

### Fórmulas

```
σ'(z) = σ(z) · (1 − σ(z))
∂σ/∂xᵢ = wᵢ · σ'(z)
Sensibilidad en app = wᵢ · σ'(z) · 100
```

**Qué decir:**

> “Las barras muestran cuánto mueve la probabilidad cada variable. **Promedio** e **Asistencia** impactan más por sus pesos. El término **P·(1−P)** es máximo cuando P ≈ 50 %.”

### Factores identificados

- **Positivos (✔):** variables sobre umbrales favorables.
- **Negativos (✖):** variables que aumentan el riesgo de reprobación.

### Tabla bajo la sigmoide

| Columna | Significado |
|---------|-------------|
| z | Entrada al modelo |
| σ(z) | Probabilidad |
| σ'(z) | Derivada |
| Prob. % | Porcentaje |
| Estado | Aprueba / En riesgo / Reprueba |

---

# PARTE 4 — GeoGebra (Víctor o Paola)

**URL:** https://www.geogebra.org/calculator?lang=es

Usar la sección **Exportar a GeoGebra** en la app (copiar cada expresión).

| # | Expresión | Para qué |
|---|-----------|----------|
| 1 | `f(x) = 1 / (1 + e^(-x))` | Curva sigmoide |
| 2 | `g(x) = f'(x)` | Derivada |
| 3 | Desarrollo de z | Combinación lineal con datos |
| 4 | `z_0 = …` | Valor z del estudiante |
| 5 | `P = (z_0, f(z_0))` | Punto en la curva |
| 6 | `t(x) = g(z_0) * (x - z_0) + f(z_0)` | Recta tangente |

**Guion (1 min):**

> “Graficamos la sigmoide, su derivada, calculamos z, marcamos el punto del estudiante y la recta tangente — aplicación directa de la Unidad IV: Derivadas.”

---

# PARTE 5 — Cierre (los tres)

- Modelo con 6 variables ponderadas  
- Probabilidad en tiempo real  
- Derivadas para orientar mejoras  
- Cálculo Diferencial + Informática  

> “EduPredict muestra que funciones, límites y derivadas permiten estimar y explicar el rendimiento académico.”

---

## Checklist antes de grabar

- [ ] `python manage.py runserver` activo  
- [ ] Sliders con datos de ejemplo  
- [ ] “Calcular predicción” ejecutado  
- [ ] GeoGebra abierto  
- [ ] Fórmulas copiadas desde Exportar a GeoGebra  
- [ ] Los 3 integrantes en cámara  

## Atajos en la app

| Acción | Efecto |
|--------|--------|
| **3 clics** en logo **EP** | Easter egg DOOM |
| **5 clics** en título **EduPredict** | Abre esta guía |
