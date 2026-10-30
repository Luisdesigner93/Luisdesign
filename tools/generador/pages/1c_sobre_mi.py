# Sobre mí (sobre-mi.html): nombre, etiquetas, bajada, foto con ancho máximo del contenido y texto de presentación.
# Contenido: texto de presentación indicado por Luis. Etiquetas tomadas del CV.

page('sobre-mi.html', 'Sobre mí · Luis Vicencio, diseñador y Product Owner',
     'Luis Vicencio es diseñador y Product Owner en Chile, especializado en branding, diseño web, UX/UI y gestión de productos digitales con Scrum.',
     current='sobre', extra_css=['css/home-v2.css', 'css/inicio.css'], contact=False, html_class='motion inicio',
     jsonld=[person_ld(alumniOf=[{'@type': 'CollegeOrUniversity', 'name': n} for n in ('Universidad de Valparaíso', 'Politecnico di Milano', 'Universidad del Desarrollo')],
                       knowsAbout=['Branding', 'Identidad visual', 'Diseño web', 'UX/UI', 'Product Owner', 'Scrum'])],
     body='''    <section class="pl-sec sobre-intro frame-grid" aria-labelledby="sobre-titulo">
      <div class="pl-inner">
        <div class="sobre-cabecera">
          <h1 class="sobre-titulo" id="sobre-titulo">Luis Vicencio</h1>
          <p class="sobre-rol">Diseñador y Product Owner</p>
        </div>
        <ul class="sobre-meta">
          <li>Región de Valparaíso, Chile</li>
        </ul>
        <p class="sobre-bajada">Soy Luis, diseñador y consultor en estrategia de marca y producto digital. Desde hace más de 7 años trabajo con negocios, equipos y organizaciones para transformar ideas y necesidades en marcas, experiencias y soluciones digitales.</p>
      </div>
    </section>

    <section class="pl-sec sobre-foto-sec">
      <div class="pl-inner">
        <div class="narrow">
          <figure class="sobre-foto">
            <img src="img/marca/luis-vicencio-escena.png" width="1536" height="1024" alt="Retrato de Luis Vicencio" loading="lazy" decoding="async">
          </figure>
        </div>
      </div>
    </section>

    <section class="pl-sec sobre-etapas" aria-labelledby="etapas-title">
      <div class="pl-inner">
        <div class="narrow">
          <p class="pl-lead sobre-etapas-intro" id="etapas-title">Mi experiencia se puede entender como una evolución en tres etapas:</p>
          <ol class="career">
            <li class="card">
              <div class="career-when"><span>2017 – 2022</span></div>
              <div>
                <h3>Diseño, identidad y experiencias digitales</h3>
                <p>Construcción de marcas, comunicación visual, UX/UI y soluciones web.</p>
              </div>
            </li>
            <li class="card">
              <div class="career-when"><span>2022 – 2025</span></div>
              <div>
                <h3>Estrategia, negocio y diseño de soluciones</h3>
                <p>Investigación, consultoría, branding estratégico, comunicación, experiencias y dirección de proyectos.</p>
              </div>
            </li>
            <li class="card">
              <div class="career-when"><span>2025 – 2026</span></div>
              <div>
                <h3>Gestión de producto e innovación tecnológica</h3>
                <p>Discovery, planificación, historias de usuario, priorización, IA, coordinación técnica y QA.</p>
              </div>
            </li>
          </ol>
        </div>
      </div>
    </section>

    <section class="pl-sec sobre-texto">
      <div class="pl-inner">
        <div class="narrow">
          <p>Mi trabajo combina distintas disciplinas. Comencé desarrollando marcas y experiencias digitales, y con el tiempo fui incorporando investigación, estrategia de negocio y gestión de producto. Esta trayectoria me ha permitido participar en proyectos desde diferentes perspectivas: entender un problema, encontrar oportunidades, definir qué vale la pena construir y trabajar junto a equipos creativos y técnicos para llevarlo a la realidad.</p>
          <p>Me interesa especialmente ese punto donde el diseño se encuentra con el negocio y la tecnología. Donde una buena idea necesita dirección, una marca necesita encontrar su propósito o un producto digital necesita resolver algo que realmente importa.</p>
          <p>Creo en el diseño como una herramienta para pensar, conectar y construir. Por eso, más que aplicar una fórmula, me gusta entender el contexto de cada proyecto, encontrar la dirección adecuada y construir soluciones que tengan sentido para las personas y los negocios.</p>
          <ul class="sobre-tags" aria-label="Habilidades">
            <li>Discovery</li>
            <li>Historias de usuario</li>
            <li>Gestión de backlog</li>
            <li>Priorización</li>
            <li>Planificación de producto</li>
            <li>Scrum</li>
            <li>Kanban</li>
            <li>Spec-driven</li>
            <li>Branding estratégico</li>
            <li>UX/UI</li>
            <li>Diseño web</li>
            <li>IA aplicada</li>
            <li>Figma</li>
            <li>Jira</li>
          </ul>
        </div>
      </div>
    </section>
''')
