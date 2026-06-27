# EduPredict — Guía de presentación y demo

**Integrantes:** Aron Barrientos · Víctor Gangas · Paola Pereira  
**Carrera:** Ingeniería en Informática · **Asignatura:** Cálculo Diferencial  
**URL demo:** http://127.0.0.1:8000/  
**PDF de la presentación:** `presentacion/presentacion.pdf`

> **Acceso rápido:** haz **5 clics** en el título **EduPredict** en la página principal (abre la versión web de esta guía).

---

## Las diapositivas del PDF — explicadas fácil

Recorre el PDF en orden. Cada bloque dice **de qué va la slide**, **quién puede hablar** y **qué decir** sin tecnicismos.

### Diapositiva 1 · Portada

**Quién:** Los tres (5 seg cada uno) o Aron presenta al grupo.

**De qué va:** Nombres, carrera, profesor, fecha. Solo saludar y decir el nombre del proyecto.

> “Somos Aron, Víctor y Paola. Nuestro proyecto se llama EduPredict: un predictor de si un estudiante aprueba o no, usando matemáticas de Cálculo.”

---

### Diapositiva 2 · Definición del proyecto *(Etapa I)*

**Quién:** Aron

**De qué va:** Explica la idea general: una web donde ingresas datos del estudiante (asistencia, notas, horas de estudio, etc.) y la app responde con un **porcentaje de probabilidad de aprobar**, más un texto que lo interpreta.

> “Muchos estudiantes no saben qué les conviene mejorar. EduPredict junta varios datos y entrega un porcentaje claro, por ejemplo: 78 % de probabilidad de aprobar, y explica qué está ayudando y qué perjudicando.”

---

### Diapositiva 3 · Problemática + tabla matemática *(Etapa I)*

**Quién:** Paola

**De qué va:** Primero el **problema**: ¿cómo estimar matemáticamente la probabilidad de aprobar? Luego la **tabla de 6 filas** — no leas código; di en palabras simples:

- **Función** — entran datos, sale un resultado.
- **Combinación lineal** — cada variable suma con un peso (nota y asistencia pesan más).
- **Sigmoide** — convierte el cálculo en un % entre 0 y 100.
- **Límites** — nunca da menos de 0 % ni más de 100 %.
- **Continuidad** — si mejoras un poco, sube un poco (sin saltos raros).
- **Derivadas** — muestran qué conviene mejorar primero.

> “Usamos seis ideas de Cálculo que ya vimos en clase, aplicadas a notas y asistencia reales.”

---

### Diapositiva 4 · Objetivos y preguntas *(Etapa I)*

**Quién:** Aron

**De qué va:** **Objetivo general:** crear la web predictiva. **Específicos:** elegir variables, armar el modelo con sigmoide, usar derivadas. Las **6 preguntas** son las que investigaron (las responderán en slide 9).

> “Nuestro objetivo fue construir una app que estime la probabilidad de aprobar. Para eso nos hicimos preguntas como: ¿qué variable influye más? ¿por qué usamos sigmoide?”

---

### Diapositiva 5 · Temas involucrados *(Etapa I)*

**Quién:** Cualquiera (30 seg)

**De qué va:** Lista rápida: Cálculo, programación, web, GeoGebra y las 6 variables académicas. No profundizar.

> “Mezclamos Cálculo Diferencial con programación web y visualización.”

---

### Diapositiva 6 · Cronograma *(Etapa I)*

**Quién:** Paola o Aron

**De qué va:** Semana 1: teoría y variables. Semana 2: modelo y programación. Semana 3: gráficos y presentación. Menciona quién hizo qué (Víctor teoría, Aron variables, Paola pesos, etc.).

> “Planificamos en tres semanas: primero la matemática, luego la app, al final la demo y Canva.”

---

### Diapositiva 7 · Herramientas tecnológicas *(Etapa II)*

**Quién:** Paola

**De qué va:** GeoGebra para ver curvas · Excel/calculadora para probar pesos · VS Code para escribir código · Python/Django para el cerebro de la app · HTML/CSS/JS para la pantalla que ve el usuario.

> “Elegimos herramientas que nos permitieron calcular, programar y mostrar gráficos sin complicarnos.”

---

### Diapositiva 8 · Fuentes de información *(Etapa II)*

**Quién:** Víctor

**De qué va:** Cuatro fuentes: libros de Cálculo (Stewart, Ortiz), estudio sobre rendimiento académico (Vargas & Montero), y documentación web (MDN, GeoGebra). Una frase por fuente.

> “No inventamos todo: nos basamos en libros de Cálculo, un estudio sobre asistencia y notas, y tutoriales para programar y graficar.”

---

### Diapositiva 9 · Respuestas a preguntas orientadoras *(Etapa II)*

**Quién:** Víctor (puede repartir filas con Paola)

**De qué va:** Recorre la tabla fila por fila: cada pregunta → respuesta corta → fuente. Conecta con lo que ya dijeron en slide 3.

> “Con las fuentes y EduPredict respondimos: las variables que más pesan son promedio y asistencia; la sigmoide nos da el porcentaje; las derivadas dicen qué mejorar.”

---

### Diapositivas 10–11 · Unidad IV Derivadas *(Etapa II)*

**Quién:** Víctor + Paola

**De qué va:** Slide 10: fórmulas de derivada (no memorizar, explicar idea). Slide 11: tablas de símbolos — qué significa P, w, etc. en palabras: “P = probabilidad”, “w = qué tan importante es cada dato”.

> “La derivada nos dice qué tan rápido sube la probabilidad si mejoras asistencia u horas. Cuando estás cerca del 50 %, el cambio se nota más.”

---

### Diapositiva 12 · Respuestas e ideas propuestas

**Quién:** Víctor

**De qué va:** Tres ideas: (1) Promedio y asistencia pesan más. (2) Mejorar ayuda más cuando estás “en el aire” (~50 %). (3) EduPredict muestra factores y gráfico de sensibilidades.

> “En resumen: sabemos qué variables importan y la app le dice al estudiante en qué enfocarse.”

---

### Diapositiva 13 · Resumen de progreso

**Quién:** Aron

**De qué va:** **Importante:** di “Etapa I y II completadas”, no “en desarrollo”. Etapa I: objetivos y matemática. Etapa II: herramientas, fuentes, derivadas, bitácora.

> “Completamos la planificación, la investigación, las fuentes, el modelo y la aplicación web.”

---

### Diapositiva 14 · Bitácora *(Etapa II)*

**Quién:** Paola (rápido, 20 seg)

**De qué va:** Muestra que hubo trabajo semanal con fechas, tareas y responsables. No leer toda la tabla.

> “En la bitácora quedó registrado quién investigó, quién programó y quién hizo los gráficos, semana a semana.”

---

### Diapositiva 15 · Presentación del producto *(Etapa III)*

**Quién:** Aron (con Víctor mostrando gráficos)

**De qué va:** **Aquí cambias al navegador** (127.0.0.1:8000). Muestra captura o app en vivo: sliders → Calcular → gauge → sensibilidades → sigmoide → Exportar GeoGebra. Ver sección “Demo app” más abajo.

> “Este es EduPredict funcionando: ingresamos datos, calculamos y vemos el porcentaje y los gráficos.”

---

### Diapositiva 16 · Resultados y conclusiones *(Etapa III)*

**Quién:** Los tres

**De qué va:** Si la slide está vacía, agrega 3–4 bullets: cumplimos objetivos, app funciona, Cálculo aplicado a un caso real, el equipo aprendió a investigar y programar.

> “Logramos una app que predice aprobación, aplicamos derivadas en un caso real y aprendimos a trabajar en equipo con evidencia.”

---

### Diapositiva 17 · Área de impacto TFL *(Etapa III)*

**Quién:** Víctor

**De qué va:** La tabla muestra que no es solo Cálculo: también programación, estadística, requisitos, innovación (ABPro), ética. Una fila = una frase.

> “EduPredict une Cálculo con Informática: programamos, analizamos datos y definimos qué necesita el usuario.”

---

### Diapositiva 18 · Bibliografía *(Etapa III)*

**Quién:** Paola o Víctor

**De qué va:** Mismas 4 fuentes de slide 8, en formato bibliográfico (autor, año, título). Cierra citando correctamente.

> “Estas son las referencias que usamos, citadas según el formato solicitado.”

---

## Orden sugerido del video (10–15 min)

| Min | Quién | Qué |
|-----|-------|-----|
| 0–2 | Aron | Slides 1–2: portada + definición |
| 2–4 | Paola | Slides 3–5: matemática + objetivos |
| 4–6 | Paola / Víctor | Slides 6–9: cronograma, herramientas, fuentes, respuestas |
| 6–8 | Víctor | Slides 10–12: derivadas + ideas |
| 8–11 | Aron | Slide 15: **demo app en vivo** |
| 11–13 | Víctor | GeoGebra (desde la app) |
| 13–15 | Todos | Slides 16–18: conclusiones, TFL, bibliografía |

---

# PARTE 1 — Aron Barrientos
## La página web — qué hace cada parte *(Demo slide 15)*

> “Ahora les mostramos EduPredict en el navegador: ponemos los datos del estudiante y la app nos dice qué tan probable es que apruebe.”

### Parte superior

- **EduPredict** — nombre del proyecto
- **Temas de color** — solo cambian colores, el cálculo es el mismo

### Columna izquierda — Datos del estudiante

Seis barras deslizantes. Cada una es un dato real del alumno:

| Variable | Rango | Peso | Qué decir |
|----------|-------|------|-----------|
| Asistencia | 0–100 % | 2,5 | Muy importante |
| Promedio | 0–100 pts | 3,0 | La más importante |
| Horas de estudio | 0–40 h/sem | 1,8 | Esfuerzo sostenido |
| Trabajos entregados | 0–10 | 1,5 | Cumplimiento |
| Participación | 0–5 | 1,2 | Participación en clases |
| Concentración | 0–5 | 1,0 | Hábitos de estudio |

**Ejemplo para la demo:** Asistencia 98 %, Promedio 60, Horas 24, Trabajos 7, Participación 5, Concentración 3 → pulsa **Calcular predicción**.

### Columna derecha — Resultado (arriba)

- **Medidor circular** — el % grande (ej. 72,7 %)
- **Frase de color** — verde = va bien; amarillo = en riesgo; rojo = difícil aprobar
- **Números abajo** — el cálculo interno; puedes decir “aquí está la matemática”

> “La app junta todos los datos, calcula y nos entrega un porcentaje fácil de entender.”

---

# PARTE 2 — Paola Pereira
## La matemática — explicada simple *(Slides 3 y 10)*

### Paso 1 — Preparar los números

Antes de sumar, cada dato se lleva a una escala parecida (entre 0 y 1). Ejemplo: 75 % asistencia → 0,75.

### Paso 2 — Sumar con pesos

Cada variable suma distinto. **Promedio pesa 3,0** y **asistencia 2,5** — son las más importantes. Eso produce un número llamado **z**.

### Paso 3 — Pasar a porcentaje (sigmoide)

Con una fórmula curva (sigmoide), z se convierte en probabilidad entre 0 % y 100 %. Nunca se pasa de esos límites.

> “Primero juntamos los datos con pesos, después la curva sigmoide lo transforma en un porcentaje.”

### Gráfico de la curva (abajo en la app)

| Parte | Significado |
|-------|-------------|
| Eje horizontal | El cálculo interno (z) |
| Eje vertical | Probabilidad de 0 a 1 |
| Punto verde ● | Dónde está el estudiante que acabas de calcular |
| Línea en el medio (0,5) | Zona de “no sé si apruebo o no” (50 %) |

---

# PARTE 3 — Víctor Gangas
## Derivadas y consejos — en la app *(Slides 10–12)*

**Idea simple:** la derivada responde “si mejoro un poquito en X, ¿cuánto sube mi probabilidad?”

### Gráfico de barras — Análisis de derivadas

Barra más larga = esa variable mueve más el resultado. Normalmente **Promedio** y **Asistencia** salen arriba.

> “Este gráfico le dice al estudiante: ‘si quieres subir tu probabilidad, conviene enfocarte primero en esto’.”

### Factores identificados

- **Lista verde (✔)** — cosas que van bien (ej. buena asistencia)
- **Lista roja (✖)** — cosas que perjudican (ej. pocas horas de estudio)

### Tabla de números (debajo del gráfico)

Opcional: no explicar cada columna; solo di que muestra cómo cambia la probabilidad al variar z.

---

# PARTE 4 — GeoGebra *(Slide 15 demo)*

**URL:** https://www.geogebra.org/calculator?lang=es

En la app, baja hasta **Exportar a GeoGebra**. Copia cada fórmula con el botón verde.

| # | Qué pegar | Para qué decir |
|---|-----------|----------------|
| 1 | Curva en S (sigmoide) | “Así se ve la probabilidad en matemáticas” |
| 2 | Derivada | “Qué tan inclinada está la curva” |
| 3–4 | Cálculo z del estudiante | “Con los datos que ingresamos” |
| 5 | Punto P en la curva | “Aquí está nuestro estudiante de ejemplo” |
| 6 | Recta tangente | “Unidad IV: la derivada como pendiente” |

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
- [ ] PDF `presentacion/presentacion.pdf` listo (slides 15, 16 y 18 completadas si faltaban)

## Atajos en la app

| Acción | Efecto |
|--------|--------|
| **3 clics** en logo **EP** | Easter egg DOOM |
| **5 clics** en título **EduPredict** | Abre esta guía (HTML) |
