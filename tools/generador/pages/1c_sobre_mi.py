# Sobre mí (sobre-mi.html y en/sobre-mi.html): nombre, etiquetas, bajada, foto con ancho máximo del contenido y texto de presentación.
# Contenido: texto de presentación indicado por Luis. Etiquetas tomadas del CV. La versión en inglés es una traducción pendiente de revisión de Luis.

_SOBRE_ALT = {'es-CL': 'sobre-mi.html', 'en': 'en/sobre-mi.html', 'x-default': 'sobre-mi.html'}
_SOBRE_JSONLD = [person_ld(alumniOf=[{'@type': 'CollegeOrUniversity', 'name': n} for n in ('Universidad de Valparaíso', 'Politecnico di Milano', 'Universidad del Desarrollo')],
                           knowsAbout=['Branding', 'Identidad visual', 'Diseño web', 'UX/UI', 'Product Owner', 'Scrum'])]

_SOBRE_ES = dict(
    nombre='Luis Vicencio', rol='Diseñador y Product Owner', lugar='Región de Valparaíso, Chile',
    bajada='Soy Luis, diseñador y consultor en estrategia de marca y producto digital. Desde hace más de 7 años trabajo con negocios, equipos y organizaciones para transformar ideas y necesidades en marcas, experiencias y soluciones digitales.',
    foto_alt='Retrato de Luis Vicencio', etapas_intro='Mi experiencia se puede entender como una evolución en tres etapas:',
    etapas=[('2017 – 2022', 'Diseño, identidad y experiencias digitales', 'Construcción de marcas, comunicación visual, UX/UI y soluciones web.'),
            ('2022 – 2025', 'Estrategia, negocio y diseño de soluciones', 'Investigación, consultoría, branding estratégico, comunicación, experiencias y dirección de proyectos.'),
            ('2025 – 2026', 'Gestión de producto e innovación tecnológica', 'Discovery, planificación, historias de usuario, priorización, IA, coordinación técnica y QA.')],
    parrafos=['Mi trabajo combina distintas disciplinas. Comencé desarrollando marcas y experiencias digitales, y con el tiempo fui incorporando investigación, estrategia de negocio y gestión de producto. Esta trayectoria me ha permitido participar en proyectos desde diferentes perspectivas: entender un problema, encontrar oportunidades, definir qué vale la pena construir y trabajar junto a equipos creativos y técnicos para llevarlo a la realidad.',
              'Me interesa especialmente ese punto donde el diseño se encuentra con el negocio y la tecnología. Donde una buena idea necesita dirección, una marca necesita encontrar su propósito o un producto digital necesita resolver algo que realmente importa.',
              'Creo en el diseño como una herramienta para pensar, conectar y construir. Por eso, más que aplicar una fórmula, me gusta entender el contexto de cada proyecto, encontrar la dirección adecuada y construir soluciones que tengan sentido para las personas y los negocios.'],
    habilidades='Habilidades',
    tags=['Discovery', 'Historias de usuario', 'Gestión de backlog', 'Priorización', 'Planificación de producto', 'Scrum', 'Kanban', 'Spec-driven', 'Branding estratégico', 'UX/UI', 'Diseño web', 'IA aplicada', 'Figma', 'Jira'],
    titulo='Sobre mí · Luis Vicencio, diseñador y Product Owner',
    desc='Luis Vicencio es diseñador y Product Owner en Chile, especializado en branding, diseño web, UX/UI y gestión de productos digitales con Scrum.',
)

_SOBRE_EN = dict(
    nombre='Luis Vicencio', rol='Designer and Product Owner', lugar='Valparaíso Region, Chile',
    bajada='I am Luis, a designer and consultant in brand strategy and digital products. For more than 7 years I have worked with businesses, teams and organizations to turn ideas and needs into brands, experiences and digital solutions.',
    foto_alt='Portrait of Luis Vicencio', etapas_intro='My experience can be understood as an evolution in three stages:',
    etapas=[('2017 – 2022', 'Design, identity and digital experiences', 'Brand building, visual communication, UX/UI and web solutions.'),
            ('2022 – 2025', 'Strategy, business and solution design', 'Research, consulting, strategic branding, communication, experiences and project leadership.'),
            ('2025 – 2026', 'Product management and technological innovation', 'Discovery, planning, user stories, prioritization, AI, technical coordination and QA.')],
    parrafos=['My work combines different disciplines. I started by developing brands and digital experiences, and over time I incorporated research, business strategy and product management. This path has allowed me to take part in projects from different perspectives: understanding a problem, finding opportunities, defining what is worth building, and working alongside creative and technical teams to bring it to life.',
              'I am especially interested in the point where design meets business and technology. Where a good idea needs direction, a brand needs to find its purpose, or a digital product needs to solve something that truly matters.',
              'I believe in design as a tool to think, connect and build. That is why, rather than applying a formula, I like to understand the context of each project, find the right direction and build solutions that make sense for people and businesses.'],
    habilidades='Skills',
    tags=['Discovery', 'User stories', 'Backlog management', 'Prioritization', 'Product planning', 'Scrum', 'Kanban', 'Spec-driven', 'Strategic branding', 'UX/UI', 'Web design', 'Applied AI', 'Figma', 'Jira'],
    titulo='About me · Luis Vicencio, designer and Product Owner',
    desc='Luis Vicencio is a designer and Product Owner in Chile, specializing in branding, web design, UX/UI and digital product management with Scrum.',
)


def _sobre_cuerpo(t):
    nombre, rol, lugar, bajada = t['nombre'], t['rol'], t['lugar'], t['bajada']
    foto_alt, etapas_intro, habilidades = t['foto_alt'], t['etapas_intro'], t['habilidades']
    etapas = ''.join(f'''
            <li class="card">
              <div class="career-when"><span>{cuando}</span></div>
              <div>
                <h3>{titulo}</h3>
                <p>{texto}</p>
              </div>
            </li>''' for cuando, titulo, texto in t['etapas'])
    parrafos = ''.join(f'\n          <p>{p}</p>' for p in t['parrafos'])
    tags = ''.join(f'\n            <li>{x}</li>' for x in t['tags'])
    return f'''    <section class="pl-sec sobre-intro frame-grid" aria-labelledby="sobre-titulo">
      <div class="pl-inner">
        <div class="sobre-cabecera">
          <h1 class="sobre-titulo" id="sobre-titulo">{nombre}</h1>
          <p class="sobre-rol">{rol}</p>
        </div>
        <ul class="sobre-meta">
          <li>{lugar}</li>
        </ul>
        <p class="sobre-bajada">{bajada}</p>
      </div>
    </section>

    <section class="pl-sec sobre-foto-sec">
      <div class="pl-inner">
        <div class="narrow">
          <figure class="sobre-foto">
            <img src="img/marca/luis-vicencio-escena.png" width="1536" height="1024" alt="{foto_alt}" loading="lazy" decoding="async">
          </figure>
        </div>
      </div>
    </section>

    <section class="pl-sec sobre-etapas" aria-labelledby="etapas-title">
      <div class="pl-inner">
        <div class="narrow">
          <p class="pl-lead sobre-etapas-intro" id="etapas-title">{etapas_intro}</p>
          <ol class="career">{etapas}
          </ol>
        </div>
      </div>
    </section>

    <section class="pl-sec sobre-texto">
      <div class="pl-inner">
        <div class="narrow">{parrafos}
          <ul class="sobre-tags" aria-label="{habilidades}">{tags}
          </ul>
        </div>
      </div>
    </section>
'''


_SOBRE_CSS = dict(current='sobre', extra_css=['css/home-v2.css', 'css/inicio.css'], contact=False, html_class='motion inicio',
                  alternates=_SOBRE_ALT, jsonld=_SOBRE_JSONLD)

page('sobre-mi.html', _SOBRE_ES['titulo'], _SOBRE_ES['desc'], body=_sobre_cuerpo(_SOBRE_ES), **_SOBRE_CSS)
page('en/sobre-mi.html', _SOBRE_EN['titulo'], _SOBRE_EN['desc'], body=_sobre_cuerpo(_SOBRE_EN), lang='en', **_SOBRE_CSS)
