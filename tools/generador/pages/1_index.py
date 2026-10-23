# Sección de proyectos del inicio: arco curvo de imágenes en perspectiva (referencia: galería cóncava de portafolio).
# Un proyecto por tarjeta, sin repetir (solo los que tienen imágenes)
_more_imgs = [('khronos', 'khronos/04.jpg', 1254, 1254), ('sustentando', 'sustentando/02.jpg', 1200, 1200), ('yomecontrolo', 'yomecontrolo/07.jpg', 906, 1736),
              ('fuchi-chao', 'fuchi-chao/01.jpg', 1397, 1400), ('botes-salvavidas', 'botes-salvavidas/01.jpg', 864, 1080), ('uv-energy', 'uv-energy/01.jpg', 1600, 899)]
_by_slug = {pr['slug']: pr for pr in PROJECTS}


def _more_card(slug, f, w, h):
    pr = _by_slug[slug]
    # Al pasar el mouse (o enfocar) la tarjeta muestra sus etiquetas arriba y el nombre con su enlace abajo
    return f'''
          <li><img src="img/proyectos/{f}" width="{w}" height="{h}" alt="" loading="lazy" decoding="async">
            <div class="more-info"><ul class="more-tags">{''.join(f'<li>{t}</li>' for t in pr['tags'])}</ul><div class="more-foot"><strong>{pr['title']}</strong><a class="more-go" href="proyectos/{slug}.html" aria-label="Ver proyecto: {pr['title']}"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a></div></div></li>'''


_more_arc = ''.join(_more_card(*m) for m in _more_imgs)
_more_steps = ''.join(f'<li><span>+{i:02d}</span>{t}</li>' for i, t in enumerate(['Estrategia y planificación', 'Diseño y desarrollo', 'Lanzamiento', 'Acompañamiento continuo'], 1))
HOME_MORE = f'''
    <!-- PROYECTOS: arco curvo de imágenes movido por el scroll y las flechas -->
    <section class="section more" id="proyectos" aria-labelledby="more-title">
      <div class="container more-head">
        <span class="tag tag-eyebrow">Proyectos</span>
        <h2 class="heading v2-big" id="more-title">Proyectos destacados <strong>y trabajo creativo</strong></h2>
        <p class="lead">Marcas, packaging y productos digitales diseñados para crecer.</p>
        <a class="btn btn-primary" href="proyectos.html">Ver todos los proyectos <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
      </div>
      <div class="more-stage">
        <!-- Flechas para recorrer el carrusel (main.js las muestra cuando el carrusel está activo) -->
        <div class="more-nav" hidden>
          <button class="more-prev" type="button" aria-label="Proyecto anterior"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></button>
          <button class="more-next" type="button" aria-label="Proyecto siguiente"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></button>
        </div>
        <ul class="more-arc" aria-label="Proyectos">{_more_arc}
        </ul>
      </div>
      <ol class="container more-steps">{_more_steps}</ol>
    </section>
'''

# Sección "ideas": frase gigante en tres líneas con un collage de productos al centro (referencia: hero editorial con collage).
# «de las ideas» y «en los» van en dos piezas: en móvil el teléfono nace entre «de las» e «ideas» y la cerveza entre «en» y «los»,
# y las separan al crecer (el eliminador nace entre «del día» y «a día», que ya son piezas separadas).
_ideas_lines = [('El mundo', '<span class="ideas-w1">de las</span><span class="ideas-split"></span><span class="ideas-w2">ideas</span>'), ('<span class="ideas-w1">en</span><span class="ideas-split"></span><span class="ideas-w2">los</span>', 'productos'), ('del día', 'a día')]
_ideas_title = ''.join(f'<span class="ideas-line"><span>{a}</span><span class="ideas-gap" aria-hidden="true"></span><span>{b}</span></span>' for a, b in _ideas_lines)
HOME_IDEAS = f'''
    <!-- IDEAS: frase gigante con collage de productos diseñados -->
    <section class="panel panel-plain ideas" aria-labelledby="ideas-title">
      <div class="ideas-stage">
        <h2 class="ideas-title" id="ideas-title">{_ideas_title}</h2>
        <div class="ideas-collage" aria-hidden="true">
          <img class="ideas-item ideas-item-phone" src="img/collage/yomecontrolo-telefono.png" width="514" height="900" alt="" loading="lazy" decoding="async">
          <img class="ideas-item ideas-item-spray" src="img/collage/fuchi-chao-eliminador.png" width="343" height="1000" alt="" loading="lazy" decoding="async">
          <img class="ideas-item ideas-item-beer" src="img/collage/khronos-stout.png" width="263" height="900" alt="" loading="lazy" decoding="async">
        </div>
      </div>
      <div class="container ideas-foot">
        <div class="ideas-intro">
          <p>Llevo ideas a productos que la gente usa todos los días: marcas, envases y experiencias digitales con un mismo criterio, desde la estrategia hasta la entrega.</p>
          <a class="btn btn-outline ideas-cta" href="#contacto">Conversemos <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
        </div>
        <a class="ideas-pill" href="proyectos.html">
          <span class="ideas-pill-btn"><span class="ideas-pill-label">Ver portafolio</span><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></span>
          <img src="img/proyectos/khronos/02.jpg" width="1254" height="1254" alt="" loading="lazy" decoding="async">
        </a>
        <!-- EDITAR: reemplazar "9 casos publicados" por la cantidad total de proyectos realizados -->
        <dl class="ideas-stats">
          <div><dt>+7</dt><dd>Años de experiencia</dd></div>
          <div><dt>9</dt><dd>Casos publicados</dd></div>
        </dl>
      </div>
    </section>
'''

# Sección «Cómo trabajo» retirada del inicio por ahora; se conserva aquí para volver a usarla.
HOME_PROCESO = '''    <!-- PROCESO -->
    <section class="panel section" id="proceso" aria-labelledby="proceso-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">Cómo trabajo</span>
          <h2 class="heading" id="proceso-title">Un proceso ágil, <strong>sin sorpresas</strong>.</h2>
        </div>
        <div class="steps-scroller" role="region" aria-label="Etapas del proceso" tabindex="0">
          <div class="steps">
            <article class="card step">
              <div><p class="step-eyebrow">Etapa uno</p><h3 class="title">Discovery</h3></div>
              <div class="step-art" aria-hidden="true">
                <div class="sk-stack"><span class="sk sk-input"></span><span class="sk sk-w80"></span><span class="sk sk-w55"></span></div>
              </div>
              <p>Validamos las necesidades del negocio y de los usuarios antes de diseñar.</p>
            </article>
            <article class="card step">
              <span class="connector" aria-hidden="true"><span><svg class="icon"><use href="img/icons.svg#i-arrow"/></svg></span></span>
              <div><p class="step-eyebrow">Etapa dos</p><h3 class="title">Estrategia</h3></div>
              <div class="step-art" aria-hidden="true">
                <div class="sk-stack sk-center"><span class="tag tag-sticker tilt-left">Posicionamiento</span><span class="sk sk-w60"></span></div>
              </div>
              <p>Definimos posicionamiento, alcance y prioridades en un backlog claro.</p>
            </article>
            <article class="card step">
              <span class="connector" aria-hidden="true"><span><svg class="icon"><use href="img/icons.svg#i-arrow"/></svg></span></span>
              <div><p class="step-eyebrow">Etapa tres</p><h3 class="title">Diseño</h3></div>
              <div class="step-art" aria-hidden="true">
                <div class="sk-stack sk-center"><span class="sk-swatches"><i></i><i></i><i></i><i></i></span><span class="tag">Prototipo</span></div>
              </div>
              <p>Marca, experiencia e interfaces, validadas con prototipos.</p>
            </article>
            <article class="card step">
              <span class="connector" aria-hidden="true"><span><svg class="icon"><use href="img/icons.svg#i-arrow"/></svg></span></span>
              <div><p class="step-eyebrow">Etapa cuatro</p><h3 class="title">Desarrollo y lanzamiento</h3></div>
              <div class="step-art" aria-hidden="true">
                <div class="sk-stack sk-center"><span class="tag tag-value">Sprint 3</span><span class="btn btn-primary is-static">QA aprobado</span></div>
              </div>
              <p>Sprints con el equipo técnico, control de calidad e informes de avance.</p>
            </article>
          </div>
        </div>
      </div>
    </section>
'''

page('index.html', 'Luis Vicencio · Branding, UX/UI y producto digital',
     'Luis Vicencio, diseñador y Product Owner con más de 7 años en branding, UX/UI y producto digital. Ayudo a empresas y pymes a definir su marca y llevar sus productos a producción.',
     current='marcas', html_class='home motion v2', canonical='', extra_css='css/home-v2.css', body='''''' + HOME_HERO + HOME_MARQUEE + HOME_IDEAS + '''
    <!-- SERVICIOS: tarjetas verticales con imagen; la activa se expande -->
    <section class="panel section svc-v2" id="servicios" aria-labelledby="servicios-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">Servicios</span>
          <h2 class="heading" id="servicios-title">Diseño para que te <strong>elijan, te entiendan y te compren</strong>.</h2>
        </div>
        <div class="svc-row">
          <a class="svc-card" href="#servicios">
            <img class="svc-card-img" src="img/proyectos/khronos/04.jpg" width="1254" height="1254" alt="" loading="lazy" decoding="async">
            <span class="svc-card-top"><ul class="svc-tags" aria-hidden="true"><li>Estrategia</li><li>Identidad</li></ul><span class="svc-arrow" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-arrow"/></svg></span></span>
            <span class="svc-card-body">
              <span class="svc-card-title">Branding estratégico</span>
              <span class="svc-card-desc">Cuando todos dicen lo mismo, el cliente elige lo más barato. Tu marca es la razón para elegirte a ti.</span>
            </span>
          </a>
          <a class="svc-card" href="producto-digital.html">
            <img class="svc-card-img" src="img/proyectos/yomecontrolo/07.jpg" width="906" height="1736" alt="" loading="lazy" decoding="async">
            <span class="svc-card-top"><ul class="svc-tags" aria-hidden="true"><li>Research</li><li>Prototipos</li></ul><span class="svc-arrow" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-arrow"/></svg></span></span>
            <span class="svc-card-body">
              <span class="svc-card-title">UX/UI y diseño de producto</span>
              <span class="svc-card-desc">Si tu producto es difícil de usar, tus clientes lo abandonan. Diseño experiencias que se entienden a la primera.</span>
            </span>
          </a>
          <a class="svc-card" href="producto-digital.html">
            <img class="svc-card-img" src="img/marca/hero-fondo.jpg" width="2000" height="1333" alt="" loading="lazy" decoding="async">
            <span class="svc-card-top"><ul class="svc-tags" aria-hidden="true"><li>Scrum</li><li>Backlog</li></ul><span class="svc-arrow" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-arrow"/></svg></span></span>
            <span class="svc-card-body">
              <span class="svc-card-title">Product Owner para tu proyecto</span>
              <span class="svc-card-desc">Sin prioridades claras, el desarrollo se alarga y se desvía. Ordeno el camino para que construyamos lo que realmente importa.</span>
            </span>
          </a>
          <a class="svc-card" href="#servicios">
            <img class="svc-card-img" src="img/proyectos/sustentando/04.jpg" width="1600" height="899" alt="" loading="lazy" decoding="async">
            <span class="svc-card-top"><ul class="svc-tags" aria-hidden="true"><li>Ecommerce</li><li>Ley 21.719</li></ul><span class="svc-arrow" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-arrow"/></svg></span></span>
            <span class="svc-card-body">
              <span class="svc-card-title">Sitios web y ecommerce</span>
              <span class="svc-card-desc">Un buen sitio guía a la persona hacia la acción: comprar, cotizar, agendar o escribirte. Diseñemos el tuyo.</span>
            </span>
          </a>
        </div>
      </div>
    </section>

''' + HOME_MORE + '''

    <!-- SOBRE MÍ -->
    <section class="panel panel-plain section about" id="sobre-mi" aria-labelledby="sobre-title">
      <div class="container">
        <div class="two-col about-grid">
          <figure class="portrait">
            <img src="img/marca/luis-vicencio-retrato.png" width="750" height="900" alt="Retrato de Luis Vicencio" loading="lazy" decoding="async">
          </figure>
          <div class="about-text">
            <span class="tag tag-eyebrow">Sobre mí</span>
            <h2 class="heading" id="sobre-title">Diseñador con <strong>mirada de producto</strong>.</h2>
            <p class="lead">Mi aporte es proponer ideas orientadas a la estrategia del negocio, no solo a la ejecución. Aplico esa mirada tanto al definir una identidad de marca como al priorizar un backlog.</p>
            <p>Soy diseñador de la Universidad de Valparaíso, con estudios de Product Design for Innovation en el Politecnico di Milano y un diplomado en Branding Estratégico. He cofundado una agencia, asesorado a pymes en Chile, Argentina y Alemania, y liderado como Product Owner el desarrollo de productos de software con inteligencia artificial.</p>
            <div><button class="link-arrow" type="button" data-drawer-open="trayectoria" aria-haspopup="dialog" aria-controls="trayectoria">Ver mi trayectoria <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></button></div>
          </div>
        </div>
        <ul class="feature-list feature-grid" role="list">
            <li class="card"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-target"/></svg></span><div><strong>Estrategia primero</strong><span>Cada decisión de diseño responde a un objetivo de negocio concreto.</span></div></li>
            <li class="card"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-search"/></svg></span><div><strong>Discovery</strong><span>Research con usuarios y negocio para validar antes de invertir en construir.</span></div></li>
            <li class="card"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-kanban"/></svg></span><div><strong>Agilidad</strong><span>Scrum adaptado al equipo, con prioridades claras y entregas frecuentes.</span></div></li>
            <li class="card"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-check"/></svg></span><div><strong>Calidad</strong><span>QA de cada entregable e informes de avance transparentes para todos.</span></div></li>
        </ul>
      </div>
    </section>

    <!-- TRAYECTORIA: panel lateral que se abre desde "Ver mi trayectoria" -->
    <dialog class="drawer" id="trayectoria" aria-labelledby="trayectoria-title">
      <div class="drawer-inner">
        <header class="drawer-head">
          <div>
            <span class="tag tag-eyebrow">Trayectoria</span>
            <h2 class="heading" id="trayectoria-title">Más de 7 años entre <strong>marca, experiencia y producto</strong>.</h2>
          </div>
          <button class="btn btn-secondary drawer-close" type="button" data-drawer-close aria-label="Cerrar trayectoria">
            <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-close"/></svg>
          </button>
        </header>
        <div class="drawer-body">
            <ol class="career">
              <li class="card">
                <div class="career-when"><span>2025 – 2026</span></div>
                <div>
                  <h3>Líder de Innovación y Productos <span class="career-org">Brand Manager y Product Owner · Bytequest SpA</span></h3>
                  <p>Lideré como Product Owner, con Scrum, un módulo de IA para la atención por chatbot de víctimas, con auditoría y observabilidad de un call center, para una institución pública del sector justicia. Coordiné un equipo de 7 personas, realicé QA de los entregables e informes mensuales de avance, e impulsé productos de uso legislativo, gestión de crisis municipal y excelencia operacional.</p>
                </div>
              </li>
              <li class="card">
                <div class="career-when"><span>2022 – 2025</span></div>
                <div>
                  <h3>CEO cofundador <span class="career-org">Studio Dinoi</span></h3>
                  <p>Cofundé y lideré una agencia que integraba branding, desarrollo web, ecommerce y comunicación corporativa. Asesoré a pymes de rubros como cervecerías, asesorías legales, productos para mascotas, servicios B2B, productos químicos y fundaciones.</p>
                </div>
              </li>
              <li class="card">
                <div class="career-when"><span>2020 – actualidad</span><span class="tag tag-value">Actual</span></div>
                <div>
                  <h3>Diseñador freelance <span class="career-org">luisdesign.cl</span></h3>
                  <p>Comunicación digital, branding y diseño para pequeñas y medianas empresas de Chile, Argentina y Alemania.</p>
                </div>
              </li>
              <li class="card">
                <div class="career-when"><span>2019 – 2020</span></div>
                <div>
                  <h3>Diseñador de marcas y UX/UI <span class="career-org">Kimsa</span></h3>
                  <p>Identidad de marca y experiencia de usuario para los clientes de la startup.</p>
                </div>
              </li>
              <li class="card">
                <div class="career-when"><span>2018 – 2019</span></div>
                <div>
                  <h3>Diseñador y encargado de comunicaciones <span class="career-org">Waterman</span></h3>
                  <p>Línea comunicacional de la empresa y sistema de diseño para cada proyecto de seguridad acuática: diseño web, motion graphics y diseño gráfico.</p>
                </div>
              </li>
            </ol>
            <h3 class="drawer-subtitle">Formación académica</h3>
            <div class="benefits">
              <div><strong>Diseño</strong><span>Universidad de Valparaíso, titulado en 2017.</span></div>
              <div><strong>Product Design for Innovation</strong><span>Politecnico di Milano, Italia, intercambio de máster 2015 – 2016.</span></div>
              <div><strong>Branding Estratégico para la Nueva Economía</strong><span>Diplomado, Universidad del Desarrollo, 2022.</span></div>
            </div>
        </div>
      </div>
    </dialog>
''')
