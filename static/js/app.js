// ── Funciones matemáticas (mirror del backend, para el canvas) ────────
function sigmoid(z) { return 1 / (1 + Math.exp(-z)); }
function sigmoidDeriv(z) { const s = sigmoid(z); return s * (1 - s); }

// ── Curva sigmoide en canvas ──────────────────────────────────────────
let currentZ = null;

function drawSigmoid(zActual) {
    const canvas = document.getElementById('sigmoidCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const W = canvas.width, H = canvas.height;
    const PAD = { top: 24, right: 24, bottom: 36, left: 44 };
    const w = W - PAD.left - PAD.right;
    const h = H - PAD.top - PAD.bottom;

    ctx.clearRect(0, 0, W, H);

    // Fondo
    ctx.beginPath();
    ctx.fillStyle = getComputedStyle(document.body).getPropertyValue('--surface2').trim() || '#1e2235';
    if (ctx.roundRect) ctx.roundRect(0, 0, W, H, 10);
    else ctx.rect(0, 0, W, H);
    ctx.fill();

    // Helpers de coordenadas
    const zMin = -6, zMax = 6;
    const toX = z => PAD.left + ((z - zMin) / (zMax - zMin)) * w;
    const toY = sig => PAD.top + (1 - sig) * h;

    // Grid horizontal
    [0, 0.25, 0.5, 0.75, 1].forEach(v => {
        const y = toY(v);
        ctx.beginPath();
        ctx.moveTo(PAD.left, y); ctx.lineTo(PAD.left + w, y);
        ctx.strokeStyle = 'rgba(255,255,255,.06)';
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.fillStyle = '#7b82a8';
        ctx.font = '10px Inter, sans-serif';
        ctx.textAlign = 'right';
        ctx.fillText(v.toFixed(2), PAD.left - 6, y + 4);
    });

    // Grid vertical
    [-6, -4, -2, 0, 2, 4, 6].forEach(z => {
        const x = toX(z);
        ctx.beginPath();
        ctx.moveTo(x, PAD.top); ctx.lineTo(x, PAD.top + h);
        ctx.strokeStyle = 'rgba(255,255,255,.06)';
        ctx.lineWidth = 1;
        ctx.stroke();
        ctx.fillStyle = '#7b82a8';
        ctx.font = '10px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText(z, x, PAD.top + h + 16);
    });

    // Línea σ = 0.5
    ctx.beginPath();
    ctx.moveTo(PAD.left, toY(0.5)); ctx.lineTo(PAD.left + w, toY(0.5));
    ctx.strokeStyle = 'rgba(108,99,255,.3)';
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    ctx.stroke();
    ctx.setLineDash([]);

    // Curva sigmoide
    const grad = ctx.createLinearGradient(PAD.left, 0, PAD.left + w, 0);
    grad.addColorStop(0, '#6c63ff');
    grad.addColorStop(1, '#00d4aa');
    ctx.beginPath();
    for (let i = 0; i <= w; i++) {
        const z = zMin + (i / w) * (zMax - zMin);
        const sig = sigmoid(z);
        if (i === 0) ctx.moveTo(toX(z), toY(sig));
        else ctx.lineTo(toX(z), toY(sig));
    }
    ctx.strokeStyle = grad;
    ctx.lineWidth = 2.5;
    ctx.shadowColor = '#6c63ff';
    ctx.shadowBlur = 8;
    ctx.fillStyle = 'transparent'; // Forzar sin relleno
    ctx.stroke();
    // NO PONER NINGUN ctx.fill() aquí.
    ctx.shadowBlur = 0;

    // Punto del estudiante
    if (zActual !== null) {
        const zClamped = Math.max(zMin, Math.min(zMax, zActual));
        const px = toX(zClamped);
        const py = toY(sigmoid(zActual));

        // Línea vertical punteada
        ctx.beginPath();
        ctx.moveTo(px, PAD.top); ctx.lineTo(px, py);
        ctx.strokeStyle = 'rgba(0,212,170,.4)';
        ctx.lineWidth = 1; ctx.setLineDash([3, 3]);
        ctx.stroke(); ctx.setLineDash([]);

        // Halo
        ctx.beginPath();
        ctx.arc(px, py, 10, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(0,212,170,.15)';
        ctx.fill();

        // Punto
        ctx.beginPath();
        ctx.arc(px, py, 5, 0, Math.PI * 2);
        ctx.fillStyle = '#00d4aa';
        ctx.shadowColor = '#00d4aa';
        ctx.shadowBlur = 12;
        ctx.fill();
        ctx.shadowBlur = 0;

        // Etiqueta
        const label = `z=${zActual.toFixed(2)}, σ=${sigmoid(zActual).toFixed(3)}`;
        const lx = px + 10 > PAD.left + w - 100 ? px - 115 : px + 10;
        ctx.fillStyle = '#e8eaf6';
        ctx.font = 'bold 11px Inter, sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText(label, lx, py - 8);
    }

    // Ejes etiquetas
    ctx.fillStyle = '#7b82a8';
    ctx.font = '11px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('z', PAD.left + w / 2, H - 2);
    ctx.save();
    ctx.translate(12, PAD.top + h / 2);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText('σ(z)', 0, 0);
    ctx.restore();
}

// ── Tabla de valores ─────────────────────────────────────────────────
function renderTable(zActual) {
    const tbody = document.getElementById('sigTableBody');
    tbody.innerHTML = '';

    // Rango de z: de -5 a 5 en pasos de 0.5, + el z actual intercalado
    const steps = [];
    for (let z = -5; z <= 5; z += 0.5) steps.push(parseFloat(z.toFixed(1)));

    // Si el z actual no está exactamente en la lista, lo insertamos
    if (zActual !== null) {
        const rounded = parseFloat(zActual.toFixed(1));
        if (!steps.includes(rounded)) {
            steps.push(parseFloat(zActual.toFixed(4)));
            steps.sort((a, b) => a - b);
        }
    }

    steps.forEach(z => {
        const sig = sigmoid(z);
        const deriv = sigmoidDeriv(z);
        const pct = (sig * 100).toFixed(1);
        const isHighlight = zActual !== null && Math.abs(z - zActual) < 0.001;

        let tagClass = 'tag-reprueba', tagText = 'Reprueba';
        if (sig >= 0.70) { tagClass = 'tag-aprueba'; tagText = 'Aprueba ✓'; }
        else if (sig >= 0.50) { tagClass = 'tag-riesgo'; tagText = 'En riesgo'; }

        const tr = document.createElement('tr');
        if (isHighlight) tr.className = 'row-highlight';
        tr.innerHTML = `
      <td>${isHighlight ? `<strong>${z.toFixed(4)}</strong> ←` : z.toFixed(1)}</td>
      <td>${sig.toFixed(4)}</td>
      <td>${deriv.toFixed(4)}</td>
      <td>${pct}%</td>
      <td><span class="${tagClass}">${tagText}</span></td>
    `;
        tbody.appendChild(tr);

        // Scroll automático a la fila del estudiante
        if (isHighlight) {
            setTimeout(() => tr.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 100);
        }
    });
}

// Dibujar curva inicial vacía
drawSigmoid(null);

const CAMPOS = [
    { id: 'asistencia', sufijo: '%', max: 100 },
    { id: 'promedio', sufijo: ' pts', max: 100 },
    { id: 'horas_estudio', sufijo: ' h', max: 40 },
    { id: 'trabajos', sufijo: ' / 10', max: 10 },
    { id: 'participacion', sufijo: ' / 5', max: 5 },
    { id: 'concentracion', sufijo: ' / 5', max: 5 },
];

const NOMBRES = {
    asistencia: 'Asistencia',
    promedio: 'Promedio',
    horas_estudio: 'Horas estudio',
    trabajos: 'Trabajos',
    participacion: 'Participación',
    concentracion: 'Concentración',
};

// Sincronizar sliders con sus badges
CAMPOS.forEach(({ id, sufijo, max }) => {
    const input = document.getElementById(id);
    const badge = document.getElementById(`${id}-val`);

    const update = () => {
        badge.textContent = input.value + sufijo;
        // Colorear el track del slider
        const pct = (input.value / max) * 100;
        input.style.setProperty('--pct', pct + '%');
        input.style.background =
            `linear-gradient(to right, var(--accent) ${pct}%, var(--surface2) ${pct}%)`;
    };

    input.addEventListener('input', update);
    update(); // estado inicial
});

// ── Gauge SVG ─────────────────────────────────────────────────────────
// El arco va desde 20,110 hasta 180,110 → semicírculo de radio 90
// Longitud total del arco ≈ π × 90 ≈ 283
const ARC_LEN = Math.PI * 90;

function setGauge(pct) {
    const fill = document.getElementById('gaugeFill');
    const pctEl = document.getElementById('gaugePct');
    const filled = (pct / 100) * ARC_LEN;
    fill.setAttribute('stroke-dasharray', `${filled} ${ARC_LEN}`);
    pctEl.textContent = pct + '%';

    // Color según resultado
    if (pct >= 70) fill.style.stroke = 'var(--accent2)';
    else if (pct >= 50) fill.style.stroke = '#f9a825';
    else fill.style.stroke = 'var(--danger)';
}

// ── Gráfico de sensibilidades (barras) ───────────────────────────────
function renderSens(sensibilidades) {
    const chart = document.getElementById('sensChart');
    chart.innerHTML = '';

    // Máximo para escalar barras
    const maxVal = Math.max(...Object.values(sensibilidades));

    Object.entries(sensibilidades).forEach(([key, val]) => {
        const pct = maxVal > 0 ? (val / maxVal) * 100 : 0;
        const row = document.createElement('div');
        row.className = 'sens-row';
        row.innerHTML = `
      <span class="sens-name">${NOMBRES[key]}</span>
      <div class="sens-bar-wrap">
        <div class="sens-bar" style="width:0%" data-target="${pct}"></div>
      </div>
      <span class="sens-value">${val.toFixed(2)}</span>
    `;
        chart.appendChild(row);
    });

    // Animar barras después de insertar
    requestAnimationFrame(() => {
        chart.querySelectorAll('.sens-bar').forEach(bar => {
            bar.style.width = bar.dataset.target + '%';
        });
    });
}

// ── Renderizar factores ───────────────────────────────────────────────
function renderFactores(positivos, negativos) {
    const posEl = document.getElementById('positivos');
    const negEl = document.getElementById('negativos');

    posEl.innerHTML = positivos.length
        ? positivos.map((f, i) =>
            `<div class="factor-item" style="animation-delay:${i * .07}s">${f}</div>`
        ).join('')
        : '<p class="factor-empty">Sin factores positivos destacados.</p>';

    negEl.innerHTML = negativos.length
        ? negativos.map((f, i) =>
            `<div class="factor-item" style="animation-delay:${i * .07}s">${f}</div>`
        ).join('')
        : '<p class="factor-empty">Sin factores negativos destacados.</p>';
}

// ── Veredicto ─────────────────────────────────────────────────────────
function setVeredicto(pct) {
    const el = document.getElementById('verdict');
    el.className = 'verdict';
    if (pct >= 70) {
        el.textContent = '🟢 Alta probabilidad de aprobación';
        el.classList.add('aprueba');
    } else if (pct >= 50) {
        el.textContent = '🟡 Situación en riesgo — mejorable';
        el.classList.add('riesgo');
    } else {
        el.textContent = '🔴 Alta probabilidad de reprobación';
        el.classList.add('reprueba');
    }
}

// ── GeoGebra Export ───────────────────────────────────────────────────
let ggbExpressions = [];

function renderGgb(data) {
    const container = document.getElementById('ggbLines');
    const btn = document.getElementById('btnCopyAll');

    if (!data) {
        container.innerHTML = '<p class="factor-empty">Calcula una predicción para ver las fórmulas</p>';
        btn.style.display = 'none';
        return;
    }

    const { z, formula_z_str } = data;
    const sig = sigmoid(z);
    const deriv = sigmoidDeriv(z);

    // Fórmulas para GeoGebra
    const lines = [
        { label: '1. Función Sigmoide', expr: `f(x) = 1 / (1 + e^(-x))` },
        { label: '2. Derivada de la Sigmoide', expr: `g(x) = f'(x)` },
        { label: '3. Desarrollo de la variable z', expr: formula_z_str },
        { label: '4. Valor Final z', expr: `z_0 = ${z.toFixed(4)}` },
        { label: '5. Punto Estudiante en Curva', expr: `P = (z_0, f(z_0))` },
        { label: '6. Recta Tangente (Tasa de Cambio)', expr: `t(x) = g(z_0) * (x - z_0) + f(z_0)` },
    ];

    ggbExpressions = lines.map(l => l.expr);

    container.innerHTML = lines.map((l, i) => `
    <div class="ggb-row" style="animation-delay: ${i * 0.05}s">
      <div class="ggb-row-inner">
        <div class="ggb-label">${l.label}</div>
        <div class="ggb-expr">${l.expr}</div>
      </div>
      <button class="btn-copy ggb-copy-btn" data-expr="${l.expr.replace(/"/g, '&quot;')}">Copiar</button>
    </div>
  `).join('');

    // Attach listeners instead of inline onclick to prevent quote issues
    document.querySelectorAll('.ggb-copy-btn').forEach(button => {
        button.addEventListener('click', function () {
            copyText(this.getAttribute('data-expr'), this);
        });
    });

    btn.style.display = 'block';
    btn.textContent = '📋 Copiar todo al portapapeles';
    btn.className = 'btn-copy-all';
}

function fallbackCopyTextToClipboard(text, btnElement, successMsg) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.top = "0";
    textArea.style.left = "0";
    textArea.style.position = "fixed";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try {
        document.execCommand('copy');
        animateCopyBtn(btnElement, successMsg);
    } catch (err) {
        alert('No se pudo copiar. Tu navegador bloqueó la acción.');
    }
    document.body.removeChild(textArea);
}

function animateCopyBtn(btnElement, successMsg) {
    const old = btnElement.getAttribute('data-original-text') || btnElement.textContent;
    if (!btnElement.hasAttribute('data-original-text')) {
        btnElement.setAttribute('data-original-text', old);
    }

    btnElement.textContent = successMsg;
    btnElement.classList.add('copied');
    setTimeout(() => {
        btnElement.textContent = old;
        btnElement.classList.remove('copied');
    }, 1500);
}

function copyText(text, btnElement) {
    if (!navigator.clipboard) {
        fallbackCopyTextToClipboard(text, btnElement, '✓ Copiado');
        return;
    }
    navigator.clipboard.writeText(text)
        .then(() => animateCopyBtn(btnElement, '✓ Copiado'))
        .catch(() => fallbackCopyTextToClipboard(text, btnElement, '✓ Copiado'));
}

function copyAllGgb() {
    const text = ggbExpressions.join('\n');
    const btn = document.getElementById('btnCopyAll');

    if (!navigator.clipboard) {
        fallbackCopyTextToClipboard(text, btn, '✓ ¡Fórmulas copiadas!');
        return;
    }
    navigator.clipboard.writeText(text)
        .then(() => animateCopyBtn(btn, '✓ ¡Fórmulas copiadas!'))
        .catch(() => fallbackCopyTextToClipboard(text, btn, '✓ ¡Fórmulas copiadas!'));
}

// ── Submit ────────────────────────────────────────────────────────────
document.getElementById('predictorForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const btnText = document.getElementById('btnText');
    const btnSpinner = document.getElementById('btnSpinner');
    btnText.textContent = 'Calculando…';
    btnSpinner.classList.remove('hidden');

    const payload = {};
    CAMPOS.forEach(({ id }) => {
        payload[id] = parseFloat(document.getElementById(id).value);
    });

    try {
        const res = await fetch('/predecir/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        const data = await res.json();

        if (!data.ok) throw new Error(data.error);

        // Actualizar UI
        setGauge(data.porcentaje);
        setVeredicto(data.porcentaje);
        document.getElementById('formulaZ').textContent = `z = ${data.z}  →  σ(z) = ${(data.porcentaje / 100).toFixed(4)}`;
        renderSens(data.sensibilidades);
        renderFactores(data.positivos, data.negativos);
        // Curva sigmoide y tabla
        currentZ = data.z;
        drawSigmoid(data.z);
        renderTable(data.z);
        renderGgb(data);

    } catch (err) {
        alert('Error al calcular: ' + err.message);
    } finally {
        btnText.textContent = 'Calcular predicción';
        btnSpinner.classList.add('hidden');
    }
});

// ── Año en el footer ──────────────────────────────────────────────────
document.getElementById('year').textContent = new Date().getFullYear();
