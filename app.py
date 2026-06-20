import os
from flask import Flask, render_template_string


app = Flask(__name__)

VIDEO_EMBED_URL = os.environ.get(
    "VIDEO_EMBED_URL",
    "https://www.youtube-nocookie.com/embed?listType=search&list=Pixar%20Toy%20Story%202%20deleted%20backup",
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
  <title>Studio Design 3D | Sala de Crisis IT</title>
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

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 24px;
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
      width: 130px;
      padding: 10px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: white;
      box-shadow: 0 10px 30px rgba(24,32,34,.1);
      font-size: 13px;
      font-weight: 800;
    }

    .node span {
      display: block;
      color: var(--muted);
      font-weight: 600;
    }

    .n1 { left: 24px; top: 52px; }
    .n2 { right: 34px; top: 62px; }
    .n3 { left: 48px; bottom: 58px; }
    .n4 { right: 42px; bottom: 54px; }

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
      padding: clamp(48px, 7vw, 92px) clamp(16px, 5vw, 72px);
      border-top: 1px solid var(--line);
    }

    .section-head {
      display: grid;
      grid-template-columns: minmax(0, .85fr) minmax(280px, .55fr);
      gap: 28px;
      align-items: end;
      margin-bottom: 26px;
    }

    .section-head p {
      color: var(--muted);
      font-size: 18px;
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

    .queue {
      display: flex;
      gap: 8px;
      align-items: end;
      min-height: 130px;
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fbfaf6;
      overflow-x: auto;
    }

    .job {
      min-width: 58px;
      display: grid;
      place-items: center;
      border-radius: 6px 6px 0 0;
      background: var(--teal);
      color: white;
      font-size: 12px;
      font-weight: 900;
    }

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
      .flow { grid-template-columns: 1fr 1fr; }
      nav { display: none; }
    }

    @media (max-width: 620px) {
      .control-grid,
      .metric-row,
      .flow { grid-template-columns: 1fr; }
      .studio-board { min-height: 360px; }
      .node { width: 116px; font-size: 12px; }
      .cpu-chip { width: 118px; height: 118px; }
      .lock-line { grid-template-columns: 1fr; }
      .memory-wall { grid-template-columns: repeat(4, 1fr); }
    }
  </style>
</head>
<body>
  <header class="topbar">
    <div class="brand"><div class="brand-mark">3D</div> Studio Design 3D | IT</div>
    <nav aria-label="Secciones">
      <a href="#simulador">Simulador</a>
      <a href="#procesos">Procesos</a>
      <a href="#memoria">Memoria</a>
      <a href="#io">E/S</a>
      <a href="#archivos">Archivos</a>
      <a href="#redes">Redes</a>
      <a href="#caso">Caso real</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="inicio">
      <div>
        <div class="kicker">Actividad integradora | Gerencia IT</div>
        <h1>Sala de Crisis del Sistema Operativo</h1>
        <p class="lead">
          Una experiencia interactiva para explicar a los dueños de un estudio de arquitectura y animacion
          como Windows coordina CPU, memoria, perifericos, archivos y red cuando todo el equipo llega al
          cierre de una entrega critica.
        </p>
        <div class="hero-actions">
          <a class="button" href="#simulador">Abrir tablero</a>
          <a class="button secondary" href="#caso">Ver caso real</a>
        </div>
      </div>

      <div class="studio-board" aria-label="Mapa animado de recursos del sistema">
        <div class="blueprint"></div>
        <div class="cpu-chip">CPU<br>MMU<br>DMA</div>
        <div class="node n1">Render farm<span>Procesos + memoria</span></div>
        <div class="node n2">Plotter A0<span>Spooling</span></div>
        <div class="node n3">Servidor NTFS<span>Permisos + auditoria</span></div>
        <div class="node n4">Wi-Fi freelance<span>DHCP + DNS + AD</span></div>
        <div class="signal"></div>
      </div>
    </section>

    <section id="simulador">
      <div class="section-head">
        <div>
          <h2>El tablero del gerente IT</h2>
          <p>Moviendo estas variables cambia el diagnostico: mas render, mas freelancers, mas presion de RAM o mas planos enviados al plotter.</p>
        </div>
        <div class="callout">
          La consigna se responde desde una situacion empirica: viernes 17:00, entrega para un cliente,
          archivos confidenciales y usuarios rotativos entrando a la red.
        </div>
      </div>

      <div class="card wide">
        <div class="control-grid">
          <label>Render 3D en CPU/GPU <span id="renderValue"></span>
            <input id="renderLoad" type="range" min="40" max="100" value="82">
          </label>
          <label>Presion de RAM <span id="ramValue"></span>
            <input id="ramPressure" type="range" min="50" max="100" value="92">
          </label>
          <label>Planos al plotter <span id="plotterValue"></span>
            <input id="plotterJobs" type="range" min="1" max="8" value="5">
          </label>
          <label>Freelancers Wi-Fi <span id="freelanceValue"></span>
            <input id="freelancers" type="range" min="0" max="25" value="15">
          </label>
        </div>

        <div class="metric-row">
          <div class="metric"><strong id="riskCpu"></strong><span>Riesgo CPU sin planificacion</span></div>
          <div class="metric"><strong id="riskRam"></strong><span>Probabilidad de swapping</span></div>
          <div class="metric"><strong id="riskPrint"></strong><span>Minutos de cola de impresion</span></div>
          <div class="metric"><strong id="riskNet"></strong><span>Altas evitadas por AD/DHCP</span></div>
        </div>
      </div>
    </section>

    <section id="procesos">
      <div class="section-head">
        <div>
          <h2>1. Gestion de Procesos</h2>
          <p>El objetivo no es que el render gane siempre: es que la videollamada siga viva y que el presupuesto no se corrompa.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Round Robin: render pesado + videollamada</h3>
          <p>
            Round Robin asigna un quantum fijo y, cuando se agota, devuelve el proceso a la cola de listos.
            Asi el render no monopoliza la CPU y la videollamada recibe turnos frecuentes, reduciendo el congelamiento percibido.
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
          <p class="muted" id="rrExplain"></p>
        </article>

        <article class="card">
          <h3>B. Semaforo: Presupuesto_Torre.xlsx</h3>
          <p>
            La condicion de carrera aparece cuando dos gerentes leen y escriben el mismo archivo al mismo tiempo.
            Un semaforo binario protege la seccion critica: quien obtiene el candado guarda primero; el otro espera.
          </p>
          <label><input id="semaphoreToggle" type="checkbox" checked> Usar semaforo de exclusion mutua</label>
          <div class="semaphore" id="semaphoreDemo"></div>
          <p class="muted" id="semaphoreText"></p>
        </article>
      </div>
    </section>

    <section id="memoria">
      <div class="section-head">
        <div>
          <h2>2. Gestion de Memoria</h2>
          <p>Las texturas, modelos BIM y escenas 3D no tienen por que estar contiguas: paginacion y MMU hacen la traduccion.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Paginacion + MMU</h3>
          <p>
            La paginacion divide memoria virtual y fisica en bloques de tamano fijo. Eso elimina la necesidad de encontrar
            huecos contiguos grandes y reduce la fragmentacion externa. La MMU traduce cada direccion virtual del software
            a una direccion fisica consultando tablas de paginas.
          </p>
          <div class="memory-wall" id="memoryWall"></div>
          <p class="muted" id="mmuText"></p>
        </article>

        <article class="card">
          <h3>B. Swapping y reemplazo LRU</h3>
          <p>
            Cuando la RAM esta al limite, Windows usa archivo de paginacion en SSD como respaldo. Para una estacion de diseno
            conviene LRU: si una textura o pagina no se uso recientemente, es mejor candidata a salir al disco.
          </p>
          <table id="lruTable" aria-label="Cuadro de algoritmo LRU"></table>
        </article>
      </div>
    </section>

    <section id="io">
      <div class="section-head">
        <div>
          <h2>3. Control de Entrada/Salida</h2>
          <p>El sistema operativo desacopla equipos rapidos de perifericos lentos y evita que la CPU copie cada bloque a mano.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Spooling del plotter</h3>
          <p>
            Los planos entran a una cola de impresion en disco. Cada PC entrega el trabajo al spooler y queda liberada,
            mientras el plotter consume la cola secuencialmente.
          </p>
          <div class="queue" id="printQueue"></div>
          <p class="muted" id="spoolText"></p>
        </article>

        <article class="card">
          <h3>B. DMA para 500 GB de materiales</h3>
          <p>
            Con DMA, el controlador del disco externo transfiere datos directo a RAM y avisa por interrupcion al terminar bloques.
            La CPU coordina, pero no queda ocupada moviendo byte por byte.
          </p>
          <div class="flow">
            <div class="flow-step">Disco externo<small>500 GB de texturas</small></div>
            <div class="flow-step">Controlador DMA<small>busca bloques</small></div>
            <div class="flow-step">RAM<small>buffer destino</small></div>
            <div class="flow-step">CPU<small>solo configura y recibe interrupciones</small></div>
            <div class="flow-step">Servidor<small>copia persistida</small></div>
          </div>
          <div class="metric-row">
            <div class="metric"><strong>500 GB</strong><span>Transferencia</span></div>
            <div class="metric"><strong>Alto</strong><span>Uso CPU sin DMA</span></div>
            <div class="metric"><strong>Bajo</strong><span>Uso CPU con DMA</span></div>
            <div class="metric"><strong>Mejor</strong><span>Multitarea del disenador</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="archivos">
      <div class="section-head">
        <div>
          <h2>4. Archivos y Seguridad</h2>
          <p>Contratos, planos y presupuestos tienen valor economico. NTFS permite ACL, auditoria y atributos utiles para investigar incidentes.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. Permisos NTFS sobre Contratos Confidenciales</h3>
          <table>
            <thead><tr><th>Grupo</th><th>Operacion permitida</th><th>Politica recomendada</th></tr></thead>
            <tbody>
              <tr><td>Directores</td><td>Leer, escribir, modificar, listar, eliminar, administrar permisos</td><td>Control total con auditoria habilitada</td></tr>
              <tr><td>Finanzas</td><td>Leer, escribir y modificar documentos presupuestarios</td><td>Modificar, sin administrar permisos</td></tr>
              <tr><td>Pasantes</td><td>Ninguna sobre contratos confidenciales</td><td>Sin herencia de permisos; acceso solo a carpetas de practica</td></tr>
            </tbody>
          </table>
        </article>

        <article class="card">
          <h3>B. Auditoria de actividad a las 03:00 AM</h3>
          <p>Ademas del nombre, el sistema de archivos registra atributos que ayudan a reconstruir que paso.</p>
          <div class="decision">
            <span class="pill">Fecha de modificacion</span>
            <span class="pill">Ultimo acceso</span>
            <span class="pill">Propietario</span>
            <span class="pill">Tamano</span>
            <span class="pill">Permisos ACL</span>
            <span class="pill">Atributos: oculto, solo lectura, cifrado</span>
          </div>
          <table>
            <thead><tr><th>Hora</th><th>Evidencia</th><th>Lectura gerencial</th></tr></thead>
            <tbody>
              <tr><td>02:58</td><td>Inicio de sesion freelance</td><td>Validar identidad contra AD y logs</td></tr>
              <tr><td>03:01</td><td>Ultimo acceso a Plano_Master.rvt</td><td>Posible copia o lectura no autorizada</td></tr>
              <tr><td>03:04</td><td>Fecha de modificacion cambia</td><td>Posible alteracion del archivo</td></tr>
            </tbody>
          </table>
        </article>
      </div>
    </section>

    <section id="redes">
      <div class="section-head">
        <div>
          <h2>5. Administracion de Redes</h2>
          <p>La red del estudio debe absorber freelancers rotativos y sucursales sin crear usuarios locales equipo por equipo.</p>
        </div>
      </div>

      <div class="grid">
        <article class="card">
          <h3>A. DHCP + DNS para laptops freelance</h3>
          <div class="flow">
            <div class="flow-step">Laptop entra al Wi-Fi<small>Sin configuracion manual</small></div>
            <div class="flow-step">DHCP asigna IP<small>IP, gateway y DNS</small></div>
            <div class="flow-step">DNS resuelve<small>www.proyectos-studio.com</small></div>
            <div class="flow-step">Intranet responde<small>Servidor correcto</small></div>
            <div class="flow-step">Politicas aplican<small>Acceso por rol</small></div>
          </div>
          <p class="muted" id="networkText"></p>
        </article>

        <article class="card">
          <h3>B. Active Directory para nuevas sucursales</h3>
          <p>
            Active Directory centraliza identidad, grupos, permisos y politicas. En vez de duplicar usuarios locales,
            el estudio administra roles una sola vez y replica reglas entre sedes.
          </p>
          <div class="decision">
            <span class="pill">Inicio de sesion centralizado</span>
            <span class="pill">Grupos por rol</span>
            <span class="pill">Politicas de seguridad</span>
            <span class="pill">Permisos compartidos</span>
            <span class="pill">Escalabilidad para sucursales</span>
          </div>
          <p class="callout">
            Decision de gerente IT: crear grupos "Directores", "Finanzas", "Arquitectos", "Freelance temporal" y
            "Pasantes"; despues asignar permisos a carpetas y recursos, no a personas sueltas.
          </p>
        </article>
      </div>
    </section>

    <section id="caso">
      <div class="section-head">
        <div>
          <h2>Caso real integrado: Pixar y Toy Story 2</h2>
          <p>Un estudio creativo casi perdio activos criticos por borrado mas falla de backups. Sirve para contrastar que hariamos distinto en Studio Design 3D.</p>
        </div>
      </div>

      <div class="case-grid">
        <article class="card">
          <h3>Que fallo</h3>
          <p>
            En 1998, archivos de Toy Story 2 fueron borrados de servidores internos y luego se descubrio que los backups
            no venian funcionando correctamente. La recuperacion dependio de una copia externa que tenia una directora tecnica.
          </p>
          <h3>Como lo hariamos distinto</h3>
          <div class="decision">
            <span class="pill">Backups 3-2-1 probados</span>
            <span class="pill">Permisos minimos NTFS/AD</span>
            <span class="pill">Auditoria de borrados masivos</span>
            <span class="pill">Versionado de proyectos</span>
            <span class="pill">Alertas fuera de horario</span>
          </div>
          <p class="muted">
            El video usa una busqueda embebida de YouTube. Para fijar un video puntual en Render, definir la variable
            <code>VIDEO_EMBED_URL</code> con una URL del tipo <code>https://www.youtube-nocookie.com/embed/ID</code>.
          </p>
        </article>
        <article class="card">
          <iframe class="video-frame" src="{{ video_embed_url }}" title="Video sobre el caso Pixar Toy Story 2" allowfullscreen></iframe>
          <p class="muted">
            Fuentes externas para el caso: WSJ, Creative Bloq y Wikipedia. La explicacion tecnica principal se apoya en la bibliografia local de la materia.
          </p>
        </article>
      </div>
    </section>

    <section id="bibliografia">
      <div class="section-head">
        <div>
          <h2>Base bibliografica usada</h2>
          <p>La narrativa de la web traduce conceptos de los apuntes y libros a decisiones concretas del gerente IT.</p>
        </div>
      </div>
      <div class="grid">
        <article class="card third"><h3>Procesos</h3><p>Guia Unidad 2: estados, planificacion Round Robin, semaforos y condiciones de carrera.</p></article>
        <article class="card third"><h3>Memoria</h3><p>Guia Unidad 3: paginacion, memoria virtual, MMU, swapping, pagefile y LRU.</p></article>
        <article class="card third"><h3>E/S, archivos y red</h3><p>Guia Unidad 4: spooling, DMA, NTFS, atributos, DHCP, DNS y Active Directory.</p></article>
        <article class="card wide"><p>Tambien se usan como respaldo teorico los libros de Silberschatz, Tanenbaum y Stallings incluidos en la carpeta de bibliografia.</p></article>
      </div>
    </section>
  </main>

  <footer class="footer">
    <strong>Studio Design 3D | Propuesta de arquitectura IT basada en Sistemas Operativos</strong>
    <p>Trabajo individual/equipo para Actividad Integradora Final. Web Python/Flask preparada para Render.</p>
  </footer>

  <script>
    const $ = (id) => document.getElementById(id);
    const sliders = ["renderLoad", "ramPressure", "plotterJobs", "freelancers", "quantum"];

    function level(value) {
      if (value >= 85) return "critico";
      if (value >= 70) return "alto";
      return "controlado";
    }

    function updateDashboard() {
      const render = Number($("renderLoad").value);
      const ram = Number($("ramPressure").value);
      const jobs = Number($("plotterJobs").value);
      const freelancers = Number($("freelancers").value);
      $("renderValue").textContent = `${render}%`;
      $("ramValue").textContent = `${ram}%`;
      $("plotterValue").textContent = `${jobs}`;
      $("freelanceValue").textContent = `${freelancers}`;
      $("riskCpu").textContent = level(render);
      $("riskRam").textContent = `${Math.max(0, ram - 55)}%`;
      $("riskPrint").textContent = `${jobs * 9}`;
      $("riskNet").textContent = `${freelancers}`;
      updateRoundRobin();
      updateMemory();
      updateSpooling();
      updateNetwork();
    }

    function updateRoundRobin() {
      const renderLoad = Number($("renderLoad").value);
      const q = Number($("quantum").value);
      $("quantumValue").textContent = `${q} unidades`;
      const processes = [
        { name: "Render", short: "R", burst: Math.ceil(renderLoad / 8), cls: "render" },
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
        `Si el quantum fuera enorme, el render se pareceria a FCFS y aumentaria el congelamiento.`;
    }

    function updateSemaphore() {
      const on = $("semaphoreToggle").checked;
      if (on) {
        $("semaphoreDemo").innerHTML = `
          <div class="lock-line"><strong>Gerente A</strong><div class="bar"><span style="width:55%">wait(), edita, signal()</span></div></div>
          <div class="lock-line"><strong>Gerente B</strong><div class="bar"><span style="left:56%; width:42%">espera y guarda despues</span></div></div>
        `;
        $("semaphoreText").textContent = "Resultado: presupuesto consistente. Solo un proceso entra a la seccion critica por vez.";
      } else {
        $("semaphoreDemo").innerHTML = `
          <div class="lock-line"><strong>Gerente A</strong><div class="bar danger"><span style="width:62%">lee 100, guarda 130</span></div></div>
          <div class="lock-line"><strong>Gerente B</strong><div class="bar danger"><span style="left:25%; width:62%">lee 100, guarda 115</span></div></div>
        `;
        $("semaphoreText").textContent = "Resultado: condicion de carrera. Una escritura pisa a la otra y se pierde informacion.";
      }
    }

    function updateMemory() {
      const pressure = Number($("ramPressure").value);
      const activePages = Math.min(8, Math.max(3, Math.round(pressure / 13)));
      const pages = ["Geom", "Tex-A", "Tex-B", "Luz", "Cam", "BIM", "UI", "Cache", "Swap-A", "Swap-B", "Swap-C", "Swap-D"];
      $("memoryWall").innerHTML = pages.map((p, i) => {
        const cls = i < activePages ? "active" : i > 7 ? "swap" : "";
        return `<div class="page ${cls}">${p}</div>`;
      }).join("");
      $("mmuText").textContent =
        `${activePages} paginas calientes quedan en RAM. Las menos usadas pueden ir al SSD; la MMU mantiene la traduccion virtual-fisica.`;
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
        <thead><tr><th>Paso</th><th>Pagina solicitada</th><th>Resultado</th><th>RAM despues del acceso</th><th>Sale al SSD</th></tr></thead>
        <tbody>${rows}</tbody>
      `;
    }

    function updateSpooling() {
      const jobs = Number($("plotterJobs").value);
      $("printQueue").innerHTML = Array.from({ length: jobs }).map((_, i) => {
        const height = 38 + ((i % 4) * 18);
        return `<div class="job" style="height:${height}px">Plano ${i + 1}</div>`;
      }).join("");
      $("spoolText").textContent =
        `${jobs} arquitectos entregan trabajos al spooler. Sus PCs vuelven a trabajar mientras el plotter imprime uno por vez.`;
    }

    function updateNetwork() {
      const freelancers = Number($("freelancers").value);
      $("networkText").textContent =
        `Con ${freelancers} freelancers, DHCP evita configurar IP manualmente y DNS evita recordar direcciones numericas de la intranet.`;
    }

    sliders.forEach(id => $(id).addEventListener("input", updateDashboard));
    $("semaphoreToggle").addEventListener("change", updateSemaphore);
    updateDashboard();
    updateSemaphore();
  </script>
</body>
</html>
"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
