# EduPredict — Guía de presentación y demo

**Integrantes:** Aron Barrientos · Víctor Gangas · Paola Pereira  
**Carrera:** Ingeniería en Informática · **Asignatura:** Cálculo Diferencial  
**URL demo:** http://127.0.0.1:8000/  
**PDF de la presentación:** `presentacion/presentacion.pdf`

> **Acceso rápido:** haz **5 clics** en el título **EduPredict** en la página principal. En la guía web: **Oscuro/Claro**, buscador, filtro por integrante, **Solo lo que diré (guion)**, reparto manual/al azar (**guardado en BD** vía `/api/guia/reparto/`), **📌 Anclar en su lugar**.

**Reparto por defecto (6 slides cada uno + slide 17 compartida):**

| Integrante | Slides que presenta |
|------------|---------------------|
| **Aron** | 1, 2, 8, 11, 14, 16 |
| **Paola** | 3, 6, 7, 12, 15, 19 |
| **Víctor** | 4, 5, 9, 10, 13, 18 |
| **Los tres** | 17 (resultados) |

---

## Símbolos — significa → sirve para

| Símbolo | Significa | Sirve para |
|---------|-----------|------------|
| **z** | Suma ponderada de las 6 variables | Juntar todos los datos en un número antes de la probabilidad |
| **P · σ(z)** | Probabilidad de aprobar en (0, 1) — se acerca a 0 o 1, no llega exacto | Mostrar el % en el medidor sin resultados imposibles |
| **wᵢ · PESOS** | Importancia de cada variable | Que promedio y asistencia pesen más |
| **x** | Dato normalizado (0–1) | Comparar asistencia, horas, etc. en la misma escala |
| **P·(1−P)** | Derivada de la sigmoide | Saber si un cambio pequeño mueve mucho la curva |
| **∂P/∂xᵢ** | Cuánto sube P al mejorar xᵢ | Gráfico de sensibilidades — orientar al estudiante |
| **× 100** | De probabilidad a porcentaje | Ver “72,7 %” en lugar de “0,727” |

---

## Las diapositivas del PDF — explicadas fácil

Recorre el PDF en orden. Cada bloque dice **de qué va la slide**, **quién puede hablar** y **qué decir** sin tecnicismos.

### Diapositiva 1 · Portada

**Título en Canva:** EDUPREDICT — PREDICTOR DE RENDIMIENTO ACADÉMICO ESTUDIANTIL

**Quién:** Aron (presenta al equipo — saludo breve).

**De qué va:** Slide formal con nombre del proyecto, integrantes y datos del curso:

- **Nombres:** Aron Barrientos, Víctor Gangas, Paola Pereira
- **Carrera:** Ingeniería en Informática
- **Asignatura:** Cálculo Diferencial
- **Sección:** 2026/O CBCD01/D-IEI-N5-P2-C2(F)/D Ñuñoa
- **Profesor:** Leonardo Andrés Olmos Saraniti
- **Fecha:** 03/06/2026

**Guion del equipo (Aron):**

> “¡Hola a todos! Somos el equipo conformado por Paola Pereira, Víctor Gangas y yo, Aron Barrientos, estudiantes de la carrera de Ingeniería en Informática. Hoy les presentamos nuestro proyecto de la asignatura de Cálculo Diferencial: EduPredict, un predictor de rendimiento académico estudiantil.”

---

### Diapositiva 2 · Definición del proyecto *(Etapa I)*

**Título en Canva:** 2 Definición del proyecto

**Quién:** Aron

**De qué va:** Aplicación web que predice la probabilidad de aprobar según variables académicas y personales. Dos columnas:

**Izquierda — datos que ingresa el usuario** (las 6 barras de la app):

- Porcentaje de asistencia
- Promedio de notas
- Horas de estudio semanal
- Cantidad de trabajos entregados
- Participación en clases
- Nivel de concentración o hábitos de estudio

**Derecha — qué entrega la app:** porcentaje de probabilidad + interpretación en texto.

**Ejemplo de la slide (conecta con el código):** “El estudiante tiene un 78 % de probabilidad de aprobar. Los factores que más favorecen el resultado son la alta asistencia y el promedio actual. El principal factor negativo es la baja cantidad de horas de estudio semanal.” — Es lo mismo que muestra la app en el medidor y en **Factores identificados** (listas ✔ y ✖ en `predictor/views.py`).

**Guion del equipo (Aron):**

> “El proyecto consiste en desarrollar una aplicación web capaz de predecir la probabilidad de aprobación de un estudiante a partir de distintas variables académicas y personales.”

**Guion del equipo (Víctor — variables y salida):**

> “Para alimentar este sistema, definimos que se ingresarán seis datos: asistencia, promedio, horas de estudio semanal, trabajos entregados, participación y concentración. La app calculará una probabilidad en porcentaje y entregará una interpretación. Por ejemplo: el estudiante tiene un 78 % de probabilidad de aprobar; los factores que más favorecen son la alta asistencia y el promedio actual.”

---

### Diapositiva 3 · Tema de investigación y problemática *(Etapa I)*

**Título en Canva:** 3 Tema de investigación, nociones matemáticas y problemáticas a abordar

**Quién:** Paola

**De qué va:** Marco del problema. **No lleva tabla de fórmulas** en esta slide.

**Izquierda — Tema de investigación:** modelos predictivos aplicados al rendimiento académico; cómo distintas variables influyen en la probabilidad de aprobar.

**Derecha — Problemática:** los estudiantes no saben qué factores afectan más; creen que solo importa la nota, pero también influyen asistencia, constancia, participación y hábitos de estudio.

**Pregunta central:** ¿Cómo podemos estimar matemáticamente la probabilidad de aprobación según los datos académicos?

*La tabla con las 6 nociones matemáticas está en la **slide 4** (siguiente).*

**Guion del equipo (Paola):**

> “Así es, Aron. La problemática principal es que, en muchos casos, los estudiantes no saben con claridad qué factores afectan más su rendimiento. A veces creen que solo importa la nota, pero también influyen la asistencia, la constancia, la participación y los hábitos de estudio. Por eso el problema es: ¿cómo podemos estimar matemáticamente la probabilidad de aprobación según sus datos académicos? Para esto desarrollamos una aplicación predictiva con conceptos de Cálculo Diferencial.”

---

### Diapositiva 4 · Nociones matemáticas *(Etapa I)*

**Título en Canva:** 4 Tema de investigación, nociones matemáticas y problemáticas a abordar

**Quién:** Víctor

**De qué va:** Tabla de 6 conceptos. Para cada fila explica **para qué sirve**, no solo el nombre:

| Concepto | Para qué sirve (qué decir) | Dónde se ve en la app |
|----------|---------------------------|------------------------|
| **Función matemática** | Recibe los 6 datos y devuelve la probabilidad — es el motor del predictor | Al pulsar **Calcular predicción** (`calcular_prediccion` en el servidor) |
| **Combinación lineal** | Suma variables con pesos distintos; promedio (3,0) y asistencia (2,5) pesan más | El valor **z** bajo el medidor |
| **Función sigmoide** | Convierte z en un % entre 0 y 100 que cualquiera entiende | Medidor circular y curva en S |
| **Límites y asíntotas** | La curva se acerca a 0 y 1 pero no llega exactamente (σ ∈ (0,1)) | Evita −10 % o 150 %; ver nota abajo |
| **Continuidad** | Mejorar un poco sube un poco — sin saltos raros al mover sliders | Mueve una barra y verás cambio gradual |
| **Derivadas** | Indican qué variable conviene mejorar primero | Gráfico de barras y factores ✔/✖ |

**¿Por qué nunca llega exactamente a 0 % ni a 100 %?**

- **Significa:** σ(z) = 1 / (1 + e^(−z)). Para cualquier *z* finito, e^(−z) > 0, así que σ(z) queda estrictamente entre 0 y 1. Solo cuando *z* → +∞ se acerca a 1 y cuando *z* → −∞ se acerca a 0 (asíntotas horizontales en el gráfico).
- **Sirve para:** explicar en clase por qué la app muestra 99,9… % o 0,0… % pero no el extremo exacto.

**Guion del equipo (Aron — combinación lineal):**

> “Y aquí es donde entra la matemática detrás del código. Transformamos los datos con combinación lineal: z = −7,2 + 2,5·asist + 3,0·prom + 1,8·horas + 1,5·trab + 1,2·part + 1,0·conc. No todas las variables pesan igual; el promedio y la asistencia influyen mucho más que la concentración.”

**Complemento (Paola — tabla de la slide):**

> “No usamos Cálculo por usarlo: cada concepto de la tabla cumple un rol concreto en la app.”

---

### Diapositiva 5 · Objetivos y preguntas *(Etapa I)*

**Título en Canva:** 5 Objetivos y preguntas

**Quién:** Víctor

**Objetivo general — para qué sirve:** app web que estime si un estudiante aprueba, con datos reales y Cálculo — herramienta de orientación, no solo calculadora.

**Objetivos específicos — qué hicimos:**
- **Identificar variables** → las 6 barras de la app
- **Modelo con sigmoide** → convertir datos en probabilidad
- **Derivadas** → saber qué mover para mejorar más rápido

**Las 6 preguntas — para qué las hicimos** (respuestas en slide 10):
1. ¿Qué variables influyen más? → priorizar esfuerzo
2. ¿Cómo representar el rendimiento con una función? → formalizar en matemáticas
3. ¿Cómo cambia si sube la asistencia? → impacto de ir a clases
4. ¿Cómo cambia si aumentan las horas? → cuantificar esfuerzo extra
5. ¿Por qué sigmoide? → acota entre 0 % y 100 %
6. ¿Derivadas y rendimiento? → recomendar en qué enfocarse

> “Nuestro objetivo fue orientar al estudiante…” *(sin línea en guion del equipo — usar bullets de arriba)*

---

### Diapositiva 6 · Temas iniciales involucrados *(Etapa I)*

**Título en Canva:** 6 Temas iniciales involucrados

**Quién:** Paola

**Área matemática — el cerebro teórico:**
- **Cálculo Diferencial** — base del proyecto
- **Límites y continuidad** — resultados coherentes al cambiar datos
- **Derivadas** — qué conviene mejorar primero
- **Sigmoide** — probabilidad comprensible

**Área tecnológica — cómo lo hicimos usable:**
- **JS + HTML/CSS** — interfaz con barras y botones
- **Visualización** — medidor, curva y barras sin leer fórmulas
- **GeoGebra** — mostrar la matemática en clase

**Variables académicas — qué mide cada una:**
- Asistencia → constancia en clases
- Promedio → desempeño evaluado
- Horas → dedicación fuera del aula
- Participación → involucramiento
- Trabajos → cumplimiento de evaluaciones
- Concentración → calidad del estudio

> “El proyecto une tres piezas…” *(sin línea en guion del equipo — usar bullets de arriba)*

---

### Diapositiva 7 · Cronograma del proyecto *(Etapa I)*

**Título en Canva:** 7 Cronograma del proyecto

**Quién:** Paola

**Para qué sirve esta slide:** demostrar que hubo planificación, responsables y productos concretos en cada semana.

| Semana | Tarea | Para qué la hicimos | Quién |
|--------|-------|---------------------|-------|
| 1 | Investigar Cálculo (funciones, derivadas, sigmoide…) | Base teórica antes de programar | Víctor |
| 1 | Definir 6 variables | Elegir datos reales e ingresables | Aron |
| 2 | Diseñar modelo (combinación lineal + sigmoide) | El “cerebro” matemático del predictor | Paola |
| 2 | Programar web (HTML/CSS/JS + Django) | Producto usable en navegador | Aron y Paola |
| 3 | Visualizaciones (medidor, sigmoide, sensibilidades) | Entender resultados sin fórmulas | Víctor |
| 3 | Presentación y demo (Canva, GeoGebra) | Mostrar proyecto completo | Los tres |

**Texto inferior:** EduPredict estima probabilidad de aprobar y aplica Cálculo para ver cómo cambia el resultado al modificar variables.

**Guion del equipo (Aron — cronograma y roles; también slide 15):**

> “Para organizar todo este desarrollo, trabajamos con un cronograma de tres semanas documentado en nuestra bitácora. Víctor se encargó de investigar los conceptos matemáticos y diseñar la visualización de resultados. Paola diseñó el modelo matemático predictivo definiendo las ponderaciones. Y entre Paola y yo nos encargamos de programar la aplicación web.”

**Complemento:**

> “Planificamos en tres semanas con productos concretos por tarea.”

---

### Diapositiva 8 · Herramientas Tecnológicas *(Etapa II)*

**Título en Canva:** 8 Etapa II: Herramientas Tecnológicas

**Quién:** Aron | Por qué la elegimos |
|-------------|-------------------|---------------------|
| **GeoGebra** | σ(z), derivada, tangente, punto del estudiante | Ver Cálculo en clase; límites y asíntotas |
| **Excel/Sheets** (opc.) | Probar pesos y z en diseño | Validar antes de Python; acordar en equipo |
| **VS Code** | Escribir todo el código | Un editor para Python y web |
| **Python + Django 6.0.6** | `calcular_prediccion()`, `/predecir/` | Servidor hace la matemática |
| **HTML/CSS/JS** | Formulario, medidor, gráficos | Interfaz clara; JS conecta con servidor |
| **SQLite** (opc.) | Config Django; no guardamos historial | Calculamos en tiempo real |

**Guion del equipo (Paola):**

> “A nivel tecnológico, unificamos el desarrollo en Visual Studio Code. Implementamos el modelo en el servidor con Python 3.13 y Django 6.0.6. Para la interfaz usamos HTML, CSS y JavaScript; JS envía los datos al servidor y muestra la barra de probabilidad y gráficos de sensibilidad interactivos.”

---

### Diapositiva 9 · Fuentes de Información *(Etapa II)*

**Título en Canva:** 9 Fuentes de Información

**Quién:** Víctor

| Fuente | Para qué nos sirvió |
|--------|---------------------|
| **Stewart** (7.ª ed.) | Funciones logísticas, límites, asíntotas, derivación |
| **Vargas & Montero** (2016) | Respaldo real: asistencia, horas y aprobación |
| **MDN + GeoGebra** | Implementar `e^(-z)` y visualizar la curva |
| **Ortiz Campos** (Patria) | Funciones, límites, continuidad, derivadas aplicadas |

**Guion del equipo (Paola):**

> “Toda nuestra investigación se fundamentó teóricamente en libros como Cálculo de una Variable de James Stewart y estudios estadísticos de rendimiento académico.”

**Complemento (tabla de fuentes):**

> “Con esas fuentes respondemos las seis preguntas orientadoras de la slide 5.”

---

### Diapositiva 10 · Respuestas a preguntas *(Etapa II)*

**Título en Canva:** 10 Respuestas a preguntas

**Quién:** Víctor

Conecta con **slide 5** (preguntas) y **slide 4** (matemática). Explica el sentido de cada respuesta:

1. **¿Qué variables influyen más?** → Promedio (3,0) y asistencia (2,5) pesan más; la app lo refleja en sensibilidades. *Fuente: Vargas & Montero + PESOS*
2. **¿Función matemática?** → `calcular_prediccion`: 6 datos → z → σ(z). *Stewart, Ortiz*
3. **¿Si sube asistencia?** → z y P suben gradualmente (continuidad); demo con slider. *EduPredict + Ortiz*
4. **¿Si suben horas?** → Igual; impacto mayor cerca de P ≈ 50 % (P·(1−P)). *Ortiz + EduPredict*
5. **¿Por qué sigmoide?** → σ(z) ∈ (0,1): se acerca a 0 y 1 pero nunca llega exactamente; evita % imposibles. *Stewart*
6. **¿Derivadas y rendimiento?** → wᵢ·P·(1−P) indica qué mejorar; gráfico de sensibilidades. *Ortiz + GeoGebra + EduPredict*

> “En la slide 5 planteamos seis preguntas de investigación. Aquí les damos la respuesta — y cada fila de la tabla conecta con algo que ya pueden ver en EduPredict o en las fuentes que citamos.”

> “Primera pregunta: **¿qué variables influyen más?** Según Vargas y Montero, y según nuestros `PESOS` en el código, el promedio pesa 3,0 y la asistencia 2,5. Esas dos arrastran más la probabilidad; las otras cuatro también suman, pero con menos peso. Por eso la app las resalta en factores y en el gráfico de sensibilidades.”

> “Segunda: **¿cómo representamos el rendimiento con una función?** Con `calcular_prediccion`: tomamos los seis datos del estudiante, calculamos z y aplicamos la sigmoide σ(z). Eso es la traducción matemática del rendimiento — la idea de Stewart y Ortiz hecha código.”

> “Tercera y cuarta van juntas: **¿qué pasa si sube la asistencia o las horas de estudio?** Más asistencia o más horas → z sube → la probabilidad sube de forma gradual, no a saltos. Lo pueden comprobar moviendo los sliders en la app. El impacto no es siempre igual: cuando P está cerca del 50 %, el factor P·(1−P) es mayor y el cambio se nota más; cerca de 0 % o 100 % la curva ya está casi plana.”

> “Quinta: **¿por qué la sigmoide para probabilidad?** Porque σ(z) siempre queda entre 0 y 1 — se acerca a los extremos pero nunca llega exactamente a 0 % ni 100 %, como vimos en la slide 4. Así evitamos probabilidades imposibles, del tipo −10 % o 150 %. Stewart lo plantea como función continua ideal para este tipo de modelos.”

> “Sexta: **¿para qué sirven las derivadas en el rendimiento académico?** La fórmula ∂P/∂xᵢ = wᵢ·P·(1−P) — que Víctor detalla en la slide 11 — nos dice qué variable conviene mejorar primero. Eso es exactamente lo que muestra el gráfico de barras de sensibilidades en EduPredict y lo que replicamos en GeoGebra: no solo ‘¿aprobará?’, sino ‘¿en qué debería enfocarse el estudiante?’.”

---

### Diapositiva 11 · Aplicación de la Unidad IV: Derivadas *(Etapa II)*

**Título en Canva:** 11 Aplicación de la Unidad IV: Derivadas

**Quién:** Aron

**Para qué usamos derivadas:** responder *“si mejoro un poco en asistencia, horas u otra variable, ¿cuánto sube la probabilidad?”*

**Fórmulas — qué significan (no memorizar):**
- **σ'(z) = P · (1 − P)** → pendiente de la sigmoide en el punto del estudiante
- **∂σ/∂xᵢ = wᵢ · P · (1 − P)** → pendiente × peso de la variable

**Dónde se ve:**
- **App** → gráfico “Análisis de derivadas” (barras)
- **GeoGebra** → curva + recta tangente (la tangente *es* la derivada dibujada)

**Código:** `derivada_sigmoide(z)` → `PESOS[k] * derivada_sigmoide(z) * 100` = barras

**Sigmoide — límites en el gráfico (conecta con slide 4):**

- **Significa:** las líneas y = 0 y y = 1 en la curva de la app son asíntotas; el punto del estudiante se acerca pero no las toca, porque e^(−z) > 0 siempre.
- **Sirve para:** demostrar con los sliders que al ir al extremo ves ~0,1 % o ~99,9 %, no 0 % ni 100 % exactos.

**Guion del equipo (Paola — sigmoide):**

> “Luego, para convertir z en una probabilidad continua entre 0 % y 100 %, utilizamos la función sigmoide σ(z) = 1 / (1 + e^(−z)). La usamos por dos propiedades vitales: límites y continuidad. La curva se acerca a 0 y 1 cuando z es muy bajo o muy alto, así la probabilidad nunca es negativa ni supera el 100 %. Al ser continua, una mejora pequeña produce un cambio gradual y realista.”

**Guion del equipo (Víctor — derivadas):**

> “Exactamente. Para la Unidad IV incorporamos derivadas. σ'(z) = σ(z)·(1−σ(z)), es decir P·(1−P). Con la regla de la cadena: ∂σ/∂xᵢ = wᵢ·P·(1−P). La derivada indica qué tan rápido sube la probabilidad por cada mejora en asistencia u otra variable; lo visualizamos en EduPredict y en GeoGebra.”

---

### Diapositiva 12 · Símbolos del modelo *(Etapa II)*

**Título en Canva:** Tabla 1 — Símbolos del modelo y su implementación en EduPredict · Tabla 2 — Interpretación de la derivada parcial

**Quién:** Paola

**Tabla 1 — Para qué sirve cada símbolo** (`predictor/views.py`):

| Símbolo | Para qué sirve | En el código |
|---------|----------------|--------------|
| **P** | Probabilidad de aprobar (0–1) | `probabilidad = sigmoid(z)` |
| **x** | Dato normalizado (0–1) | `asistencia/100`, `horas_estudio/40`, … |
| **wᵢ** | Importancia de la variable | `PESOS[k]` |
| **P·(1−P)** | Sensibilidad de la curva | `derivada_sigmoide(z)` |
| **∂P/∂xᵢ** | Cuánto sube P al mejorar xᵢ | `PESOS[k] * derivada_sigmoide(z)` |
| **× 100** | Escala para el gráfico | `sensibilidades = … * 100` |

**Tabla 2 — Para qué sirve cada parte:**

| Parte | Pregunta que responde | Ejemplo |
|-------|----------------------|---------|
| **∂P/∂xᵢ** | Si mejoro un poquito, ¿cuánto sube P? | “¿Cuánto ayuda una hora más de estudio?” |
| **wᵢ** | ¿Qué tan importante es la variable? | Promedio 3,0 vs concentración 1,0 |
| **P·(1−P)** | ¿Cuándo el cambio se nota más? | Máximo cerca de 50 %; mínimo cerca de 0 % o 100 % |

> “Esta diapositiva traduce la matemática de las slides anteriores — especialmente las fórmulas de derivadas que explicó Víctor en la slide 11 — al código real de EduPredict. No es decoración: cada símbolo de la tabla tiene una línea concreta en `predictor/views.py`.”

> “En la **Tabla 1**, fila por fila: **P** es la probabilidad de aprobar entre 0 y 1 — en código, `probabilidad = sigmoid(z)`, lo que ve el estudiante al final. **x** es cada dato normalizado a la misma escala — por ejemplo asistencia entre 100 o horas entre 40 — para que todas las variables sean comparables. **wᵢ** es el peso de cada variable: por eso el promedio pesa más que la concentración; vive en el diccionario `PESOS`.”

> “Siguen **P·(1−P)** y **∂P/∂xᵢ**: la primera es la derivada de la sigmoide en el punto actual — qué tan inclinada está la curva — y la calculamos con `derivada_sigmoide(z)`. La segunda combina ese factor con el peso wᵢ: `PESOS[k] * derivada_sigmoide(z)`. Eso responde ‘si mejoro solo esta variable un poquito, ¿cuánto sube P?’. El **× 100** al final solo escala el resultado para que las barras del gráfico se lean en porcentaje.”

> “La **Tabla 2** descompone esa misma idea en tres piezas. **∂P/∂xᵢ** responde cuánto ayuda mejorar una variable concreta — ‘¿cuánto sube la probabilidad con una hora más de estudio?’. **wᵢ** dice qué tan crítica es esa variable en el modelo — el promedio pesa 3,0, la concentración 1,0. Y **P·(1−P)** recuerda que la sensibilidad depende de dónde esté el estudiante en la curva: cerca del 50 % un pequeño cambio se nota mucho; cerca de 0 % o 100 % casi no mueve la aguja. Con estas dos tablas, cualquiera puede ir de la fórmula en la pizarra a la línea exacta en el repositorio.”

---

### Diapositiva 13 · Respuestas e Ideas Propuestas

**Título en Canva:** 13 Respuestas e Ideas Propuestas

**Quién:** Víctor

**Tres bloques — para qué sirve cada uno:**

1. **Variables de mayor peso** — Promedio y asistencia pesan más → el estudiante sabe dónde enfocarse primero.
2. **Análisis de cambio** — Mejorar impacta más en la zona de incertidumbre (P ≈ 50 %), porque P·(1−P) es máximo → explica por qué a veces un esfuerzo “se nota mucho”.
3. **Propuesta EduPredict** — Factores negativos + gráfico de sensibilidades → la app no solo da un %, **orienta qué mejorar**.

> “Promedio y asistencia pesan más…” *(sin línea en guion del equipo — usar bullets de arriba)*

---

### Diapositiva 14 · Resumen de Progreso

**Título en Canva:** 14 Resumen de Progreso

**Quién:** Aron

**⚠️ Canva dice “Etapa II en Desarrollo” — al presentar di “Etapa I y II completadas”.**

**Etapa I — para qué sirvió:**
- Objetivos claros → supimos qué construir
- Base matemática → sigmoide, pesos, derivadas antes de programar
- Equipo organizado → tareas repartidas (slide 7)

**Etapa II — para qué sirvió:**
- Herramientas elegidas → Django, GeoGebra (slide 8)
- Fuentes revisadas → Stewart, Ortiz, Vargas (slide 9)
- Modelo de derivadas → sensibilidades en la app (slides 11–13)

> “Completamos planificación, investigación…” *(sin línea en guion del equipo — usar bullets Etapa I y II de arriba)*

---

### Diapositiva 15 · Bitácora Etapa II

**Título en Canva:** 15 Bitácora Etapa II

**Quién:** Paola (30–40 seg)

**Para qué sirve:** evidencia del trabajo con fechas y responsables — conecta con cronograma (slide 7).

| Fecha | Qué hicimos | Para qué sirvió | Quién |
|-------|-------------|-----------------|-------|
| 10/06 · Sem. 1 | Investigar Cálculo (sigmoide, derivadas…) | Base teórica slides 4 y 11 | Víctor |
| 10/06 · Sem. 1 | Definir 6 variables | Datos de las barras de la app | Aron |
| 17/06 · Sem. 2 | Modelo en Excel (pesos) | Probar antes de Python — asist. 2,5, prom. 3,0 | Paola |
| 17/06 · Sem. 2 | Programar web Django + JS | App funcional con `/predecir/` | Aron y Paola |
| 26/06 · Sem. 3 | Medidor, sensibilidades, factores | Resultado comprensible sin fórmulas | Víctor |
| 26/06 · Sem. 3 | Presentación + demo | Canva, GeoGebra, app lista | Los tres |

> “En la bitácora quedó el registro semanal…” *(mismo bloque de roles que slide 7 — ver guion de Aron arriba)*

---

### Diapositiva 16 · Presentación del producto o prototipo *(Etapa III)*

**Título en Canva:** 16 Presentación del producto o prototipo

**Quién:** Aron (demo en vivo en 127.0.0.1:8000 o captura de la slide)

**Para qué sirve:** mostrar el prototipo terminado — conecta slide 2 con la app real.

**Izquierda:** 6 barras + botón **Calcular predicción** → genera z y probabilidad.

**Derecha — para qué sirve cada bloque:**

| Bloque | Para qué sirve |
|--------|----------------|
| **Resultado** (medidor + σ(z)) | % de probabilidad — respuesta principal |
| **Análisis de derivadas** | Qué variable mejorar primero |
| **Factores identificados** | Interpretación ✔/✖ (como ejemplo 78 % slide 2) |
| **Curva sigmoide** | Ver dónde está el estudiante en la curva |
| **Tabla z / σ / σ' / Estado** | Reprueba · En riesgo · Aprueba |

> “Ingresamos seis datos y la app entrega probabilidad, sensibilidades, factores y sigmoide…” *(sin línea en guion del equipo — agregar al grabar: abrir http://127.0.0.1:8000/ y demo en vivo)*

---

### Diapositiva 17 · Resultados y conclusiones *(Etapa III)*

**Título en Canva:** 17 Resultados y conclusiones

**Quién:** Los tres

**Para qué sirve:** demostrar que el modelo funciona con **dos escenarios** de la slide.

**Escenario A (~33 %):** reprobación probable → alerta + derivadas indican qué mejorar.

**Escenario B (~73 %):** aprobación probable → factores ✔ positivos → punto más a la derecha en sigmoide.

**Conclusiones (slide 13):**
- Objetivo cumplido: probabilidad con Cálculo aplicado
- La app orienta, no solo calcula
- Trabajo en equipo con evidencia

**Estados:** z bajo → Reprueba · medio → En riesgo · alto → Aprueba (≥70 % en código).

> “Con distintos datos cambia el veredicto…” *(sin línea en guion del equipo — usar escenarios A y B de arriba)*

---

### Diapositiva 18 · Área de impacto TFL *(Etapa III)*

**Título en Canva:** 18 EduPredict y competencias del tronco formativo (TFL)

**Quién:** Víctor (una frase por fila)

**Intro:** articula matemática, informática y contexto académico real.

| Asignatura TFL | Para qué en EduPredict |
|----------------|------------------------|
| **Cálculo Diferencial** | Sigmoide, límites, derivadas — modelar cambio |
| **Programación / Web** | Django + HTML/CSS/JS — solución usable |
| **Estadística descriptiva** | Variables, pesos, probabilidad |
| **Ing. de requisitos** | 6 variables según necesidad usuario |
| **Innovación / ABPro** | Indagación, bitácora, prototipo |
| **Gestión de proyectos** | Cronograma y roles del equipo |
| **Ciencia de datos / IA** | Regresión logística (sigmoide) |
| **Ética profesional** | Datos simulados; sin guardar historial |

**Guion del equipo (Víctor — cierre):**

> “Como conclusión final, con EduPredict logramos articular la matemática, la informática y un contexto académico real. No solo aplicamos límites, continuidad y derivadas para modelar la tasa de variación, sino que implementamos soluciones computacionales reales con programación e ingeniería de requisitos. ¡Muchas gracias por su atención!”

---

### Diapositiva 19 · Bibliografía *(Etapa III)*

**Quién:** Paola

**De qué va:** Mismas 4 fuentes de slide 9, en formato bibliográfico.

> “Estas son las referencias que usamos, citadas según el formato solicitado.”

---

## Guion continuo para el video *(borrador del equipo — ya repartido en cada diapositiva arriba)*

Referencia narrativa de principio a fin. **El texto ya está en los bloques “Guion del equipo” de cada slide.** Esta sección sirve para leer el hilo completo de una vez.

### Aron — Apertura y definición *(slides 1–2)*

> ¡Hola a todos! Somos el equipo conformado por Paola Pereira, Víctor Gangas y yo, Aron Barrientos, estudiantes de Ingeniería en Informática. Hoy les presentamos EduPredict, nuestro proyecto de Cálculo Diferencial: un predictor de rendimiento académico estudiantil.
>
> El proyecto consiste en desarrollar una aplicación web capaz de predecir la probabilidad de aprobación de un estudiante a partir de distintas variables académicas y personales.

### Paola — Problemática *(slide 3)*

> Así es, Aron. La problemática es que muchos estudiantes no saben qué factores afectan más su rendimiento. A veces creen que solo importa la nota, pero también influyen la asistencia, la constancia, la participación y los hábitos de estudio.
>
> Por eso nos preguntamos: ¿cómo podemos estimar matemáticamente la probabilidad de aprobación según los datos académicos? Para esto desarrollamos una aplicación predictiva con Cálculo Diferencial.

### Víctor — Variables y salida *(slide 2)*

> El sistema permite ingresar seis datos: asistencia, promedio, horas de estudio semanal, trabajos entregados, participación y concentración. Con ellos calcula un porcentaje de probabilidad y una interpretación.
>
> Por ejemplo: “El estudiante tiene un 78 % de probabilidad de aprobar. Los factores que más favorecen son la alta asistencia y el promedio actual.” *(Completar en demo: mencionar factor negativo si aplica, ej. pocas horas de estudio.)*

### Aron — Combinación lineal *(slide 4 · fórmula z)*

> Aquí entra la matemática del código. Modelamos con combinación lineal:
>
> `z = −7,2 + 2,5·asist + 3,0·prom + 1,8·horas + 1,5·trab + 1,2·part + 1,0·conc`
>
> No todas las variables pesan igual: promedio y asistencia influyen más que concentración. *(Antes de sumar, cada dato se normaliza entre 0 y 1 — ver PARTE 2.)*

### Paola — Sigmoide, límites y continuidad *(slides 4 y 11)*

> Convertimos z en probabilidad con la sigmoide: `σ(z) = 1 / (1 + e^(−z))`.
>
> Usamos esta función por sus límites y su continuidad: la curva se acerca a 0 y 1 sin pasarse del 0 % al 100 %, y un esfuerzo pequeño produce un cambio gradual — como al mover los sliders en la app.

### Víctor — Derivadas *(slides 11–12)*

> En la Unidad IV usamos derivadas. `σ'(z) = P·(1−P)` y por variable `∂σ/∂xᵢ = wᵢ·P·(1−P)`. Indica qué tan rápido sube la probabilidad si mejora asistencia u otra variable. Lo vemos en el gráfico de sensibilidades de EduPredict y en GeoGebra con la recta tangente.

### Aron — Cronograma y roles *(slides 7 y 15)*

> Organizamos el trabajo en tres semanas, documentado en la bitácora. Víctor investigó la matemática y las visualizaciones. Paola diseñó el modelo y los pesos. Paola y yo programamos la aplicación web.

### Paola — Herramientas y fuentes *(slides 8–9)*

> Usamos Visual Studio Code, Python 3.13 con Django 6.0.6 en el servidor, y HTML/CSS/JavaScript en la interfaz — JS envía datos a `/predecir/` y muestra el medidor y gráficos de sensibilidad.
>
> Nos fundamentamos en Stewart (*Cálculo de una Variable*), Ortiz, Vargas & Montero y documentación MDN/GeoGebra.

### Aron — Demo en vivo *(slide 16 · IMPORTANTE — agregar al video)*

> *(Abrir http://127.0.0.1:8000/)* Ahora les mostramos EduPredict: ingresamos los seis datos, pulsamos Calcular predicción, vemos el porcentaje, las barras de derivadas, los factores ✔/✖ y la curva sigmoide.

### Víctor — Cierre y TFL *(slides 17–18)*

> Con EduPredict articulamos matemática, informática y contexto académico real: límites, continuidad, derivadas, programación, requisitos e ingeniería de software. ¡Muchas gracias por su atención!

---

### Tabla de concordancia: guion ↔ guía ↔ slides

| Bloque del guion | ¿Concuerda? | Slide(s) | Ya en la guía MD |
|------------------|-------------|----------|------------------|
| Saludo + EduPredict | ✅ Sí | 1 | Diapositiva 1 |
| Definición web predictiva | ✅ Sí | 2 | Diapositiva 2 |
| Problemática + pregunta | ✅ Sí | 3 | Diapositiva 3 |
| 6 variables + ejemplo 78 % | ✅ Sí* | 2 | Diapositiva 2 (*falta factor negativo en el guion) |
| Fórmula z y pesos | ✅ Sí | 4 | Slides 4 + PARTE 2 |
| Sigmoide + límites + continuidad | ✅ Sí | 4, 11 | Slides 4, 11 + símbolos |
| Derivadas + fórmulas | ✅ Sí | 11–12 | Slides 11–12 + PARTE 3 |
| Cronograma / bitácora / roles | ✅ Sí | 7, 15 | Slides 7 y 15 |
| Django, VS Code, HTML/JS | ✅ Sí | 8 | Diapositiva 8 |
| Fuentes Stewart, etc. | ✅ Sí | 9, 19 | Diapositivas 9 y 19 |
| Cierre TFL | ✅ Sí | 18 | Diapositiva 18 |
| **Demo app en vivo** | ❌ Falta en guion | 16 | PARTE 1 + slide 16 |
| Objetivos y 6 preguntas | ❌ Falta en guion | 5 | Diapositiva 5 |
| Temas involucrados (3 áreas) | ❌ Falta en guion | 6 | Diapositiva 6 |
| Respuestas a preguntas (tabla) | ❌ Falta en guion | 10 | Diapositiva 10 |
| Ideas: P ≈ 50 %, mayor peso | ❌ Falta en guion | 13 | Diapositiva 13 |
| Etapas I y II completadas | ❌ Falta en guion | 14 | Diapositiva 14 |
| Dos escenarios (33 % vs 73 %) | ❌ Falta en guion | 17 | Diapositiva 17 |
| GeoGebra paso a paso | ⚠️ Solo mencionado | 16 demo | PARTE 4 |
| Normalización (÷100, ÷40…) | ⚠️ No dicho en guion | 4, 12 | PARTE 2 paso 1 |
| Bibliografía formal | ⚠️ Solo Stewart citado | 19 | Diapositiva 19 |

**Conclusión:** el guion del compañero cubre bien el **hilo narrativo del video** (intro → problema → matemática → equipo → tech → cierre). La guía MD ya tiene **todo eso y más** (slide por slide). Lo que conviene **sumar al guion al grabar**: demo slide 16, escenarios slide 17, y una frase de slide 13 (zona 50 %).

---

## Orden sugerido del video (10–15 min)

| Min | Quién | Qué |
|-----|-------|-----|
| 0–2 | Aron | Slides 1–2: portada + definición del proyecto |
| 2–3 | Paola | Slide 3: tema de investigación y problemática |
| 3–5 | Paola | Slides 4–6: nociones matemáticas + objetivos + temas |
| 5–7 | Paola / Víctor | Slides 7–10: cronograma, herramientas, fuentes, respuestas |
| 7–10 | Víctor / Paola | Slides 11–14: derivadas, símbolos, ideas, progreso |
| 10–11 | Paola | Slide 15: bitácora |
| 11–14 | Aron | Slide 16: **demo en vivo** |
| 14–15 | Todos | Slide 17: resultados (2 escenarios) |
| 15–16 | Víctor | Slide 18: área TFL |
| 16–17 | Paola/Víctor | Slide 19: bibliografía y cierre |

---

# PARTE 1 — Aron Barrientos
## La página web — qué hace cada parte *(Demo slide 16 · conecta con slide 2)*

> “En la slide 2 definimos la app: ingresamos seis datos y obtenemos probabilidad más interpretación. Ahora lo mostramos en vivo.”

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

**Ejemplo como en la slide 2:** Asistencia alta (ej. 95 %), Promedio ~60, Horas bajas (ej. 3–4 h) → la app debería mostrar ~70–80 %, con ✔ asistencia y promedio, y ✖ pocas horas de estudio.

**Otro ejemplo numérico:** Asistencia 98 %, Promedio 60, Horas 24, Trabajos 7, Participación 5, Concentración 3 → pulsa **Calcular predicción**.

### Columna derecha — Resultado (arriba)

- **Medidor circular** — el % grande (ej. 72,7 %)
- **Frase de color** — verde = va bien; amarillo = en riesgo; rojo = difícil aprobar
- **Números abajo** — el cálculo interno; puedes decir “aquí está la matemática”

> “La app junta todos los datos, calcula y nos entrega un porcentaje fácil de entender.”

---

# PARTE 2 — Paola Pereira
## La matemática — explicada simple *(Slides 4, 12 y demo)*

### Paso 1 — Preparar los números

Antes de sumar, cada dato se lleva a una escala parecida (entre 0 y 1). Ejemplo: 75 % asistencia → 0,75.

### Paso 2 — Sumar con pesos

Cada variable suma distinto. **Promedio pesa 3,0** y **asistencia 2,5** — son las más importantes. Eso produce un número llamado **z**.

### Paso 3 — Pasar a porcentaje (sigmoide)

Con la sigmoide, *z* se convierte en probabilidad en el intervalo **(0, 1)**: entre 0 % y 100 % pero sin llegar nunca al extremo exacto (e^(−z) > 0 siempre → σ(z) nunca es 0 ni 1). Solo se acerca — asíntotas. Ver nota en slide 4.

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
## Derivadas y consejos — en la app *(Slides 11, 13)*

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

# PARTE 4 — GeoGebra *(Slide 16 demo)*

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
