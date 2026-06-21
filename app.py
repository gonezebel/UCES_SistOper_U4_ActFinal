import os
from flask import Flask, render_template_string


app = Flask(__name__)

VIDEO_EMBED_URL = os.environ.get(
    "VIDEO_EMBED_URL",
    "https://www.youtube-nocookie.com/embed/w_kRN8vMg6Y",
)


@app.route("/")
def index():
    return render_template_string(
        PAGE,
        video_embed_url=VIDEO_EMBED_URL,
    )


PAGE = """
<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Studio Design 3D | Sala de Situación IT</title>
  <style>
    :root {
      --ink: #182022;
      --muted: #5d6769;
      --paper: #f7f5ef;
      --panel: #ffffff;
      --line: #d8d4c8;
      --teal: #007f7a;
      --teal-2: #35b5aa;
      --lime: #c8e34d;
      --brick: #b84a3a;
      --steel: #4c6570;
      --shadow: 0 18px 50px rgba(24, 32, 34, 0.14);
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      color: var(--ink);
      background:
        linear-gradient(90deg, rgba(24,32,34,.05) 1px, transparent 1px),
        linear-gradient(0deg, rgba(24,32,34,.05) 1px, transparent 1px),
        var(--paper);
      background-size: 32px 32px;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.5;
    }

    a { color: var(--teal); }

    .topbar {
      position: sticky;
      top: 0;
      z-index: 20;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      min-height: 62px;
      padding: 10px clamp(16px, 4vw, 48px);
      background: rgba(247, 245, 239, 0.92);
      border-bottom: 1px solid var(--line);
      backdrop-filter: blur(14px);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
      letter-spacing: .01em;
    }

    .brand-mark {
      width: 34px;
      height: 34px;
      display: grid;
      place-items: center;
      color: white;
      background: conic-gradient(from 160deg, var(--teal), var(--steel), var(--brick), var(--teal));
      border-radius: 6px;
      font-size: 15px;
    }

    nav {
      display: flex;
      flex-wrap: wrap;
      justify-content: flex-end;
      gap: 8px;
    }

    nav a {
      padding: 7px 10px;
      border: 1px solid transparent;
      border-radius: 6px;
      color: var(--ink);
      font-size: 14px;
      text-decoration: none;
    }

    nav a:hover {
      border-color: var(--line);
      background: rgba(255,255,255,.66);
    }

    .hero {
      display: grid;
      grid-template-columns: minmax(0, 1.05fr) minmax(300px, .95fr);
      gap: clamp(24px, 4vw, 52px);
      align-items: center;
      min-height: calc(100vh - 62px);
      padding: clamp(28px, 5vw, 72px) clamp(16px, 5vw, 72px);
      background:
        radial-gradient(circle at 78% 20%, rgba(0,127,122,.15), transparent 30%),
        linear-gradient(135deg, rgba(255,255,255,.3), rgba(255,255,255,0));
    }

    .kicker {
      display: inline-flex;
      gap: 8px;
      align-items: center;
      padding: 6px 10px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: rgba(255,255,255,.65);
      color: var(--steel);
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
    }

    h1 {
      margin: 18px 0 14px;
      max-width: 900px;
      font-size: clamp(38px, 6vw, 78px);
      line-height: .95;
      letter-spacing: 0;
    }

    h2 {
      margin: 0 0 12px;
      font-size: clamp(27px, 4vw, 46px);
      line-height: 1.03;
      letter-spacing: 0;
    }

    h3 {
      margin: 0 0 8px;
      font-size: 20px;
      letter-spacing: 0;
    }

    p { margin: 0 0 12px; }

    .lead {
      max-width: 740px;
      color: var(--muted);
      font-size: clamp(18px, 2.2vw, 22px);
    }

    .button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 44px;
      padding: 10px 16px;
      border: 1px solid var(--ink);
      border-radius: 6px;
      background: var(--ink);
      color: white;
      font-weight: 800;
      text-decoration: none;
      cursor: pointer;
    }

    .button.secondary {
      background: rgba(255,255,255,.7);
      color: var(--ink);
    }

    .studio-board {
      position: relative;
      min-height: 520px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background:
        linear-gradient(135deg, rgba(0,127,122,.08), transparent),
        rgba(255,255,255,.76);
      box-shadow: var(--shadow);
      overflow: hidden;
    }

    .blueprint {
      position: absolute;
      inset: 24px;
      border: 1px solid rgba(24,32,34,.16);
      background:
        linear-gradient(90deg, rgba(0,127,122,.12) 1px, transparent 1px),
        linear-gradient(0deg, rgba(0,127,122,.12) 1px, transparent 1px);
      background-size: 24px 24px;
      border-radius: 6px;
    }

    .cpu-chip {
      position: absolute;
      left: 50%;
      top: 47%;
      width: 150px;
      height: 150px;
      transform: translate(-50%, -50%);
      display: grid;
      place-items: center;
      border: 2px solid var(--ink);
      border-radius: 8px;
      background: #f2f0e8;
      font-weight: 900;
      box-shadow: inset 0 0 0 10px rgba(0,127,122,.08);
    }

    .cpu-chip::before,
    .cpu-chip::after {
      content: "";
      position: absolute;
      inset: -18px;
      border: 1px dashed rgba(24,32,34,.35);
      border-radius: 10px;
      animation: pulse 2.2s ease-in-out infinite;
    }

    .cpu-chip::after {
      inset: -34px;
      animation-delay: .5s;
    }

    @keyframes pulse {
      0%, 100% { opacity: .2; transform: scale(.94); }
      50% { opacity: .72; transform: scale(1); }
    }

    .node {
      position: absolute;
      width: 230px;
      height: 118px;
      padding: 16px 18px;
      display: grid;
      place-content: center;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: white;
      box-shadow: 0 10px 30px rgba(24,32,34,.1);
      font-size: 16px;
      line-height: 1.25;
      font-weight: 800;
      text-align: center;
      overflow: visible;
    }

    .node span {
      display: block;
      color: var(--muted);
      font-weight: 600;
      line-height: 1.35;
      overflow-wrap: anywhere;
    }

    .n1 { left: 34px; top: 54px; }
    .n2 { right: 34px; top: 54px; }
    .n3 { left: 34px; bottom: 54px; }
    .n4 { right: 34px; bottom: 54px; }

    .signal {
      position: absolute;
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--lime);
      box-shadow: 0 0 0 8px rgba(200,227,77,.18);
      animation: travel 6s linear infinite;
    }

    @keyframes travel {
      0% { left: 22%; top: 18%; }
      25% { left: 73%; top: 23%; }
      50% { left: 72%; top: 76%; }
      75% { left: 24%; top: 74%; }
      100% { left: 22%; top: 18%; }
    }

    section {
      padding: clamp(34px, 5vw, 62px) clamp(16px, 5vw, 72px);
      border-top: 1px solid var(--line);
    }

    .section-head {
      display: grid;
      grid-template-columns: minmax(0, .85fr) minmax(280px, .55fr);
      gap: 28px;
      align-items: end;
      margin-bottom: 18px;
    }

    .section-head p {
      color: var(--muted);
      font-size: 18px;
    }

    .section-head > :only-child {
      grid-column: 1 / -1;
    }

    .section-head > :only-child p {
      max-width: none;
    }

    .section-head.full-width {
      grid-template-columns: 1fr;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 16px;
    }

    .card {
      grid-column: span 6;
      padding: 18px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: rgba(255,255,255,.86);
      box-shadow: 0 12px 34px rgba(24,32,34,.08);
    }

    .wide { grid-column: span 12; }
    .third { grid-column: span 4; }

    .control-grid {
      display: grid;
      grid-template-columns: repeat(4, minmax(130px, 1fr));
      gap: 12px;
    }

    label {
      display: grid;
      gap: 7px;
      color: var(--muted);
      font-size: 13px;
      font-weight: 800;
    }

    input[type="range"] { width: 100%; accent-color: var(--teal); }

    .metric-row {
      display: grid;
      grid-template-columns: repeat(4, minmax(0, 1fr));
      gap: 10px;
      margin-top: 14px;
    }

    .metric {
      padding: 12px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf6;
    }

    .metric strong {
      display: block;
      font-size: 24px;
      line-height: 1;
    }

    .metric span { color: var(--muted); font-size: 12px; }

    .timeline {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 14px;
    }

    .slice {
      min-width: 42px;
      padding: 8px 9px;
      border-radius: 6px;
      color: white;
      font-size: 12px;
      font-weight: 900;
      text-align: center;
      animation: pop .4s ease both;
    }

    .slice.render { background: var(--brick); }
    .slice.meet { background: var(--teal); }
    .slice.os { background: var(--steel); }

    @keyframes pop {
      from { opacity: 0; transform: translateY(8px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .semaphore {
      display: grid;
      gap: 8px;
      margin-top: 14px;
    }

    .lock-line {
      display: grid;
      grid-template-columns: 130px 1fr;
      gap: 10px;
      align-items: center;
    }

    .bar {
      position: relative;
      min-height: 32px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #f2f0e8;
      overflow: hidden;
    }

    .bar span {
      position: absolute;
      inset: 0 auto 0 0;
      display: grid;
      place-items: center;
      color: white;
      background: var(--teal);
      font-size: 12px;
      font-weight: 900;
      white-space: nowrap;
    }

    .bar.danger span { background: var(--brick); }

    .memory-wall {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      gap: 8px;
      margin-top: 14px;
    }

    .page {
      min-height: 54px;
      display: grid;
      place-items: center;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fbfaf6;
      color: var(--muted);
      font-size: 12px;
      font-weight: 900;
      text-align: center;
    }

    .page.active { background: var(--teal); color: white; }
    .page.swap { background: #ece7d8; color: var(--ink); }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 12px;
      font-size: 14px;
    }

    th, td {
      padding: 9px 10px;
      border-bottom: 1px solid var(--line);
      text-align: left;
      vertical-align: top;
    }

    th { color: var(--steel); font-size: 12px; text-transform: uppercase; }

    .flow {
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 8px;
      margin-top: 14px;
    }

    .flow-step {
      min-height: 82px;
      padding: 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf6;
      font-weight: 800;
    }

    .flow-step small {
      display: block;
      margin-top: 5px;
      color: var(--muted);
      font-weight: 600;
    }

    .spool-map {
      display: grid;
      grid-template-columns: 1fr 1.15fr 1fr;
      gap: 10px;
      align-items: stretch;
      margin-top: 14px;
    }

    .spool-box {
      min-height: 128px;
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf6;
    }

    .spool-box strong {
      display: block;
      margin-bottom: 8px;
      font-size: 16px;
    }

    .mini-list {
      display: grid;
      gap: 6px;
      margin: 0;
      padding: 0;
      list-style: none;
    }

    .mini-list li {
      padding: 7px 8px;
      border-radius: 6px;
      background: white;
      border: 1px solid var(--line);
      color: var(--steel);
      font-size: 13px;
      font-weight: 800;
    }

    .spool-arrow {
      display: grid;
      place-items: center;
      color: var(--teal);
      font-weight: 900;
      font-size: 26px;
    }

    .dma-panel {
      display: grid;
      gap: 8px;
      margin-top: 14px;
    }

    .dma-path {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 8px;
    }

    .dma-step {
      min-height: 78px;
      padding: 11px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf6;
      font-weight: 900;
    }

    .dma-step small {
      display: block;
      margin-top: 5px;
      color: var(--muted);
      font-weight: 600;
    }

    .dma-step.good {
      border-color: rgba(0,127,122,.35);
      background: rgba(0,127,122,.08);
    }

    .dma-step.bad {
      border-color: rgba(184,74,58,.35);
      background: rgba(184,74,58,.08);
    }

    .network-map {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 12px;
      align-items: stretch;
      margin-top: 14px;
    }

    .network-node {
      min-height: 178px;
      padding: 16px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf6;
      overflow-wrap: anywhere;
    }

    .network-node strong {
      display: block;
      margin-bottom: 7px;
      font-size: 18px;
    }

    .network-node p {
      margin: 0;
      color: var(--muted);
      font-size: 15px;
    }

    .network-node.service {
      background: rgba(0,127,122,.08);
      border-color: rgba(0,127,122,.28);
    }

    .network-node.service strong {
      color: var(--teal);
    }

    .result-note {
      margin-top: 12px;
      padding: 12px 14px;
      border-radius: 8px;
      background: rgba(200,227,77,.16);
      color: var(--steel);
      font-weight: 700;
    }

    .decision {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 12px 0 6px;
    }

    .pill {
      padding: 6px 9px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: #fbfaf6;
      color: var(--steel);
      font-size: 12px;
      font-weight: 800;
    }

    .case-grid {
      display: grid;
      grid-template-columns: minmax(0, .95fr) minmax(280px, 1.05fr);
      gap: 16px;
      align-items: stretch;
    }

    .video-frame {
      width: 100%;
      aspect-ratio: 16 / 9;
      border: 0;
      border-radius: 8px;
      background: #111;
    }

    .short-frame {
      max-width: 315px;
      margin: 0 auto;
      aspect-ratio: 9 / 16;
    }

    .intro-video {
      display: grid;
      justify-items: center;
      margin-top: 18px;
    }

    .identity-grid {
      display: grid;
      grid-template-columns: repeat(2, minmax(220px, 1fr));
      gap: 8px 18px;
      margin-top: 18px;
      color: rgba(255,255,255,.88);
      font-size: 14px;
    }

    .identity-grid strong {
      display: block;
      color: white;
      font-size: 12px;
      text-transform: uppercase;
    }

    .footer {
      padding: 36px clamp(16px, 5vw, 72px);
      background: var(--ink);
      color: white;
    }

    .footer a { color: var(--lime); }
    .muted { color: var(--muted); }
    .callout {
      border-left: 4px solid var(--teal);
      padding: 12px 14px;
      background: rgba(0,127,122,.08);
      border-radius: 0 8px 8px 0;
    }

    @media (max-width: 980px) {
      .hero,
      .section-head,
      .case-grid {
        grid-template-columns: 1fr;
      }
      .hero { min-height: auto; }
      .studio-board { min-height: 430px; }
      .card,
      .third { grid-column: span 12; }
      .control-grid,
      .metric-row,
      .flow,
      .spool-map,
      .dma-path,
      .network-map { grid-template-columns: 1fr 1fr; }
      nav { display: none; }
    }

    @media (max-width: 620px) {
      .control-grid,
      .metric-row,
      .flow,
      .spool-map,
      .dma-path,
      .network-map { grid-template-columns: 1fr; }
      .studio-board { min-height: 360px; }
      .node {
        width: 142px;
        height: 86px;
        padding: 10px 8px;
        font-size: 12px;
      }
      .cpu-chip { width: 118px; height: 118px; }
      .lock-line { grid-template-columns: 1fr; }
      .memory-wall { grid-template-columns: repeat(4, 1fr); }
      .identity-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <header class="topbar">
    <div class="brand"><div class="brand-mark">3D</div> Studio Design 3D | IT</div>
    <nav aria-label="Secciones">
      <a href="#intro">Introducción</a>
      <a href="#procesos">Procesos</a>
      <a href="#memoria">Memoria</a>
      <a href="#io">E/S</a>
      <a href="#archivos">Archivos</a>
      <a href="#redes">Redes</a>
      <a href="#caso">Conclusión</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="inicio">
      <div>
        <div class="kicker">Gerencia IT | Studio Design 3D</div>
        <h1>Sala de Situación del Sistema Operativo</h1>
        <p class="lead">
          ¿Cómo vamos a sostener la operación de Studio Design 3D cuando coinciden
          renders pesados, videollamadas con clientes, presupuestos compartidos, plotters saturados,
          freelancers conectados por Wi-Fi y proyectos confidenciales en el servidor? La respuesta, a continuación.
        </p>
      </div>

      <div class="studio-board" aria-label="Mapa animado de recursos del sistema">
        <div class="blueprint"></div>
        <div class="cpu-chip">CPU<br>MMU<br>DMA</div>
        <div class="node n1">Render farm<span>Procesos + memoria</span></div>
        <div class="node n2">Plotter A0<span>Spooling</span></div>
        <div class="node n3">Servidor NTFS<span>Permisos + auditoría</span></div>
        <div class="node n4">Wi-Fi freelance<span>DHCP + DNS + AD</span></div>
        <div class="signal"></div>
      </div>
    </section>

    <section id="intro">
      <div class="section-head full-width">
        <div>
          <h2>Primero, el riesgo de una operación sin controles</h2>
          <p>
            En un estudio creativo, un borrado accidental, una copia no autorizada o una falla de backup
            no son incidentes menores: pueden comprometer meses de trabajo, entregas comerciales y confianza del cliente;
            si los activos digitales son el producto, la gestión de archivos, usuarios, procesos y respaldos es parte directa del negocio.
          </p>
        </div>
        <div class="callout">
          Mi propuesta es operar con permisos por rol, auditoría, colas de trabajo, respaldo probado y servicios
          centralizados. El sistema operativo deja de ser invisible y pasa a ser una capa de continuidad del negocio.
        </div>
      </div>
      <div class="intro-video">
        <iframe class="video-frame short-frame" src="{{ video_embed_url }}" title="Riesgo operativo en activos digitales" allowfullscreen></iframe>
      </div>
    </section>

    <section id="procesos">
      <div class="section-head">
        <div>
          <h2>1. Gestión de Procesos</h2>
          <p>La gestión de procesos permite repartir CPU, alternar estados de ejecución y sincronizar recursos compartidos para sostener respuesta e integridad de datos.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Round Robin: render pesado + videollamada</h3>
          <p>
            Round Robin asigna un quantum fijo y, cuando se agota, devuelve el proceso a la cola de listos.
            Así el render no monopoliza la CPU y la videollamada recibe turnos frecuentes, reduciendo el congelamiento percibido.
          </p>
          <div class="decision">
            <span class="pill">Proceso largo: render</span>
            <span class="pill">Proceso interactivo: llamada</span>
            <span class="pill">Cambio de contexto</span>
          </div>
          <label>Quantum simulado <span id="quantumValue"></span>
            <input id="quantum" type="range" min="1" max="6" value="3">
          </label>
          <div class="timeline" id="rrTimeline" aria-label="Linea de tiempo Round Robin"></div>
          <p class="result-note" id="rrExplain"></p>
        </article>

        <article class="card">
          <h3>B. Semáforo: Presupuesto_Torre.xlsx</h3>
          <p>
            La condición de carrera aparece cuando dos gerentes leen y escriben el mismo archivo al mismo tiempo.
            Un semáforo binario protege la sección crítica: quien obtiene el candado guarda primero; el otro espera.
          </p>
          <label><input id="semaphoreToggle" type="checkbox" checked> Usar semáforo de exclusión mutua</label>
          <div class="semaphore" id="semaphoreDemo"></div>
          <p class="result-note" id="semaphoreText"></p>
        </article>
      </div>
    </section>

    <section id="memoria">
      <div class="section-head">
        <div>
          <h2>2. Gestión de Memoria</h2>
          <p>La gestión de memoria asigna, protege y recupera espacio para que varios programas trabajen a la vez sin pisarse, usando RAM, memoria virtual y traducción de direcciones.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Paginación + MMU</h3>
          <p>
            La paginación divide memoria virtual y física en bloques de tamaño fijo. Eso elimina la necesidad de encontrar
            huecos contiguos grandes y reduce la fragmentación externa. La MMU traduce cada dirección virtual del software
            a una dirección física consultando tablas de páginas.
          </p>
          <div class="memory-wall" id="memoryWall"></div>
          <p class="result-note" id="mmuText"></p>
        </article>

        <article class="card">
          <h3>B. Swapping y reemplazo LRU</h3>
          <p>
            Cuando la RAM está al límite, Windows usa archivo de paginación en SSD como respaldo. Para una estación de diseño
            conviene LRU: si una textura o página no se usó recientemente, es mejor candidata a salir al disco.
          </p>
          <table id="lruTable" aria-label="Cuadro de algoritmo LRU"></table>
          <p class="result-note">
            <strong>Hit:</strong> la página solicitada ya estaba en RAM.
            <strong>Fallo:</strong> la página no estaba cargada y el sistema debe traerla desde disco o reemplazar otra página.
          </p>
        </article>
      </div>
    </section>

    <section id="io">
      <div class="section-head">
        <div>
          <h2>3. Control de Entrada/Salida</h2>
          <p>El sistema operativo desacopla equipos rápidos de periféricos lentos y evita que la CPU copie cada bloque a mano.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Spooling del plotter</h3>
          <p>
            Los planos entran a una cola de impresión en disco. Cada PC entrega el trabajo al spooler y queda liberada,
            mientras el plotter consume la cola secuencialmente.
          </p>
          <div class="spool-map" aria-label="Flujo de spooling">
            <div class="spool-box">
              <strong>Estaciones de trabajo</strong>
              <ul class="mini-list">
                <li>Arquitecto 1 envía plano</li>
                <li>Arquitecto 2 envía plano</li>
                <li>Arquitecto 3 envía plano</li>
                <li>Arquitecto 4 envía plano</li>
                <li>Arquitecto 5 envía plano</li>
              </ul>
            </div>
            <div class="spool-box">
              <strong>Spooler en disco</strong>
              <ul class="mini-list">
                <li>Ordena trabajos</li>
                <li>Libera las PCs</li>
                <li>Retiene la cola aunque el plotter sea lento</li>
              </ul>
            </div>
            <div class="spool-box">
              <strong>Plotter A0</strong>
              <ul class="mini-list">
                <li>Imprime uno por vez</li>
                <li>Recibe trabajos ya encolados</li>
                <li>Evita bloquear a usuarios</li>
              </ul>
            </div>
          </div>
        </article>

        <article class="card">
          <h3>B. DMA para 500 GB de materiales</h3>
          <p>
            Con DMA, el controlador del disco externo transfiere datos directo a RAM y avisa por interrupción al terminar bloques.
            La CPU coordina, pero no queda ocupada moviendo byte por byte.
          </p>
          <label><input id="dmaToggle" type="checkbox" checked> Usar DMA en la transferencia</label>
          <div class="dma-panel" id="dmaDemo"></div>
          <p class="result-note" id="dmaText"></p>
        </article>
      </div>
    </section>

    <section id="archivos">
      <div class="section-head">
        <div>
          <h2>4. Archivos y Seguridad</h2>
          <p>Contratos, planos y presupuestos tienen valor económico. NTFS permite ACL, auditoría y atributos útiles para investigar incidentes.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Permisos NTFS sobre Contratos Confidenciales</h3>
          <table>
            <thead><tr><th>Grupo</th><th>Operación permitida</th><th>Política recomendada</th></tr></thead>
            <tbody>
              <tr><td>Directores</td><td>Leer, escribir, modificar, listar, eliminar, administrar permisos</td><td>Control total con auditoría habilitada</td></tr>
              <tr><td>Pasantes</td><td>Ninguna sobre contratos confidenciales</td><td>Sin herencia de permisos; acceso solo a carpetas de practica</td></tr>
            </tbody>
          </table>
        </article>

        <article class="card">
          <h3>B. Auditoría de actividad a las 03:00 AM</h3>
          <p>Además del nombre, el sistema de archivos registra atributos que ayudan a reconstruir qué pasó.</p>
          <div class="decision">
            <span class="pill">Fecha de modificación</span>
            <span class="pill">Último acceso</span>
            <span class="pill">Propietario</span>
            <span class="pill">Tamaño</span>
            <span class="pill">Permisos ACL</span>
            <span class="pill">Atributos: oculto, solo lectura, cifrado</span>
          </div>
          <table>
            <thead><tr><th>Hora</th><th>Evidencia</th><th>Lectura gerencial</th></tr></thead>
            <tbody>
              <tr><td>02:58</td><td>Inicio de sesión freelance</td><td>Validar identidad contra AD y logs</td></tr>
              <tr><td>03:01</td><td>Último acceso a Plano_Master.rvt</td><td>Posible copia o lectura no autorizada</td></tr>
              <tr><td>03:04</td><td>Fecha de modificación cambia</td><td>Posible alteración del archivo</td></tr>
            </tbody>
          </table>
        </article>
      </div>
    </section>

    <section id="redes">
      <div class="section-head">
        <div>
          <h2>5. Administración de Redes</h2>
          <p>La red del estudio debe absorber freelancers rotativos y sucursales sin crear usuarios locales equipo por equipo.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. DHCP + DNS para laptops freelance</h3>
          <div class="network-map" aria-label="Flujo de red para laptops freelance">
            <div class="network-node">
              <strong>1. Laptop freelance</strong>
              <p>Se conecta al Wi-Fi de la oficina sin configuración manual previa.</p>
            </div>
            <div class="network-node service">
              <strong>2. DHCP</strong>
              <p>Entrega dirección IP, puerta de enlace y servidor DNS.</p>
            </div>
            <div class="network-node service">
              <strong>3. DNS</strong>
              <p>Traduce www.proyectos-studio.com a la IP del servidor interno.</p>
            </div>
            <div class="network-node">
              <strong>4. Intranet</strong>
              <p>El usuario llega al recurso correcto y las políticas definen qué puede ver o modificar.</p>
            </div>
          </div>
          <div class="result-note">
            Resultado: 15 freelancers pueden incorporarse rápido sin configurar equipo por equipo, manteniendo acceso por rol.
          </div>
        </article>

        <article class="card">
          <h3>B. Active Directory para nuevas sucursales</h3>
          <p>
            Active Directory centraliza identidad, grupos, permisos y políticas. En vez de duplicar usuarios locales,
            el estudio administra roles una sola vez y replica reglas entre sedes.
          </p>
          <div class="decision">
            <span class="pill">Inicio de sesión centralizado</span>
            <span class="pill">Grupos por rol</span>
            <span class="pill">Políticas de seguridad</span>
            <span class="pill">Permisos compartidos</span>
            <span class="pill">Escalabilidad para sucursales</span>
          </div>
          <p class="callout">
            Decisión de gerente IT: crear grupos "Directores", "Arquitectos", "Freelance temporal" y "Pasantes";
            después asignar permisos a carpetas y recursos, no a personas sueltas.
          </p>
        </article>
      </div>
    </section>

    <section id="caso">
      <div class="section-head">
        <div>
          <h2>Control ejecutivo de continuidad</h2>
          <p>El objetivo final es que Studio Design 3D pueda crecer sin depender de soluciones manuales ni permisos improvisados.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>Riesgos que cierro desde IT</h3>
          <p>
            La arquitectura propuesta evita que un render monopolice recursos, que un presupuesto se sobrescriba,
            que el plotter bloquee estaciones de trabajo, que una transferencia masiva deje inutilizable la CPU,
            o que usuarios temporales accedan a información fuera de su rol.
          </p>
          <div class="decision">
            <span class="pill">Backups 3-2-1 probados</span>
            <span class="pill">Permisos por rol NTFS/AD</span>
            <span class="pill">Auditoría de borrados masivos</span>
            <span class="pill">Versionado de proyectos</span>
            <span class="pill">Alertas fuera de horario</span>
          </div>
        </article>
        <article class="card">
          <h3>Decision para el directorio</h3>
          <p>
            Recomiendo formalizar un entorno Windows administrado por Active Directory, carpetas NTFS por rol,
            auditoría sobre activos críticos, política de backup verificada, monitoreo de recursos y procesos de
            incorporación rápida para freelancers. La inversión se justifica porque protege entregas, reputación y continuidad.
          </p>
        </article>
      </div>
    </section>
  </main>

  <footer class="footer">
    <strong>Studio Design 3D | Arquitectura IT para continuidad operativa</strong>
    <div class="identity-grid">
      <div><strong>Universidad</strong>UCES</div>
      <div><strong>Programa</strong>Tecnicatura Universitaria en Programación de Software</div>
      <div><strong>Asignatura</strong>Sistemas Operativos</div>
      <div><strong>Actividad</strong>Actividad Integradora Final</div>
      <div><strong>Profesor/a</strong>Grimaldi, Camila</div>
      <div><strong>Alumno/a</strong>Beloqui, Gonzalo</div>
      <div><strong>Matrícula</strong>148741</div>
      <div><strong>Fecha de entrega</strong>2026/06/22</div>
    </div>
  </footer>

  <script>
    const $ = (id) => document.getElementById(id);
    const scenario = {
      renderLoad: 82,
      ramPressure: 92,
      plotterJobs: 5,
      freelancers: 15
    };

    function updateRoundRobin() {
      const q = Number($("quantum").value);
      $("quantumValue").textContent = `${q} unidades`;
      const processes = [
        { name: "Render", short: "R", burst: Math.ceil(scenario.renderLoad / 8), cls: "render" },
        { name: "Meet", short: "V", burst: 6, cls: "meet" },
        { name: "SO", short: "SO", burst: 3, cls: "os" }
      ];
      let queue = processes.map(p => ({ ...p }));
      let timeline = [];
      let time = 0;
      while (queue.length && timeline.length < 22) {
        const p = queue.shift();
        const run = Math.min(q, p.burst);
        timeline.push({ ...p, run, at: time });
        time += run;
        p.burst -= run;
        if (p.burst > 0) queue.push(p);
      }
      $("rrTimeline").innerHTML = timeline.map((s, i) =>
        `<div class="slice ${s.cls}" style="animation-delay:${i * 35}ms">${s.short}<br>${s.run}u</div>`
      ).join("");
      $("rrExplain").textContent =
        `Con quantum ${q}, la llamada vuelve a CPU varias veces antes de que el render termine. ` +
        `Si el quantum fuera enorme, el render se parecería a FCFS y aumentaría el congelamiento.`;
    }

    function updateSemaphore() {
      const on = $("semaphoreToggle").checked;
      if (on) {
        $("semaphoreDemo").innerHTML = `
          <div class="lock-line"><strong>Gerente A</strong><div class="bar"><span style="width:55%">espera(), edita, señal()</span></div></div>
          <div class="lock-line"><strong>Gerente B</strong><div class="bar"><span style="left:56%; width:42%">espera y guarda después</span></div></div>
        `;
        $("semaphoreText").textContent = "Resultado: presupuesto consistente. Solo un proceso entra a la sección crítica por vez.";
      } else {
        $("semaphoreDemo").innerHTML = `
          <div class="lock-line"><strong>Gerente A</strong><div class="bar danger"><span style="width:62%">lee 100, guarda 130</span></div></div>
          <div class="lock-line"><strong>Gerente B</strong><div class="bar danger"><span style="left:25%; width:62%">lee 100, guarda 115</span></div></div>
        `;
        $("semaphoreText").textContent = "Resultado: condición de carrera. Una escritura pisa a la otra y se pierde información.";
      }
    }

    function updateMemory() {
      const pressure = scenario.ramPressure;
      const activePages = Math.min(8, Math.max(3, Math.round(pressure / 13)));
      const pages = ["Geom", "Tex-A", "Tex-B", "Luz", "Cam", "BIM", "UI", "Cache", "Swap-A", "Swap-B", "Swap-C", "Swap-D"];
      $("memoryWall").innerHTML = pages.map((p, i) => {
        const cls = i < activePages ? "active" : i > 7 ? "swap" : "";
        return `<div class="page ${cls}">${p}</div>`;
      }).join("");
      $("mmuText").textContent =
        `${activePages} páginas activas quedan en RAM. Las menos usadas pueden ir al SSD; la MMU mantiene la traducción virtual-física.`;
      renderLRU(activePages);
    }

    function renderLRU(frames) {
      const refs = ["Tex-A", "BIM", "Luz", "Tex-A", "Geom", "Cam", "BIM", "UI", "Tex-B", "Luz"];
      const capacity = Math.min(5, Math.max(3, frames - 2));
      let memory = [];
      const rows = refs.map((ref, step) => {
        let action = "hit";
        let evicted = "-";
        if (!memory.includes(ref)) {
          action = "fallo";
          if (memory.length >= capacity) {
            evicted = memory.shift();
          }
          memory.push(ref);
        } else {
          memory = memory.filter(p => p !== ref);
          memory.push(ref);
        }
        return `<tr><td>${step + 1}</td><td>${ref}</td><td>${action}</td><td>${memory.join(", ")}</td><td>${evicted}</td></tr>`;
      }).join("");
      $("lruTable").innerHTML = `
        <thead><tr><th>Paso</th><th>Página solicitada</th><th>Resultado</th><th>RAM después del acceso</th><th>Sale al SSD</th></tr></thead>
        <tbody>${rows}</tbody>
      `;
    }

    function updateDMA() {
      const on = $("dmaToggle").checked;
      if (on) {
        $("dmaDemo").innerHTML = `
          <div class="dma-path">
            <div class="dma-step good">Disco externo<small>lee bloques de materiales</small></div>
            <div class="dma-step good">Controlador DMA<small>transfiere directo a RAM</small></div>
            <div class="dma-step good">CPU<small>configura, sigue trabajando y recibe interrupciones</small></div>
          </div>
        `;
        $("dmaText").textContent = "Resultado: la copia de 500 GB avanza sin ocupar a la CPU en cada movimiento de datos.";
      } else {
        $("dmaDemo").innerHTML = `
          <div class="dma-path">
            <div class="dma-step bad">Disco externo<small>envía bloques</small></div>
            <div class="dma-step bad">CPU saturada<small>interviene en cada transferencia</small></div>
            <div class="dma-step bad">Trabajo del diseñador<small>pierde respuesta durante la copia</small></div>
          </div>
        `;
        $("dmaText").textContent = "Consecuencia: la CPU queda ocupada moviendo datos y la estación responde peor durante la transferencia.";
      }
    }

    $("quantum").addEventListener("input", updateRoundRobin);
    $("semaphoreToggle").addEventListener("change", updateSemaphore);
    $("dmaToggle").addEventListener("change", updateDMA);
    updateRoundRobin();
    updateMemory();
    updateSemaphore();
    updateDMA();
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
