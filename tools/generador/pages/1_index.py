# Sección de proyectos del inicio (landing Marcas): Fuchi Chao destacado + arco curvo de imágenes en perspectiva.
# Cada tarjeta: (enlace, nombre, línea bajo el nombre, etiquetas, imagen o None si falta). Textos de tools/narrativa/02-landing-marcas.md
_more_cases = [
    ('proyectos/lab502.html', 'LAB*502', 'De una tienda de insumos a un laboratorio fotográfico con propósito, que ganó un fondo cultural con su estrategia.', ['Estrategia', 'Identidad'], None),
    ('proyectos/sustentando.html', 'Sustentando', 'Cuatro años como aliado: de un logotipo a una consultora que consigue clientes por LinkedIn.', ['Identidad', 'Web', 'Comunicación B2B'], ('sustentando/02.jpg', 1200, 1200)),
    ('proyectos/uv-energy.html', 'Uvenergy', 'Una pyme de energía renovable que nació con marca en 2023 y la hizo crecer en 2025.', ['Identidad', 'Web'], ('uv-energy/01.jpg', 1600, 899)),
    ('proyectos/botes-salvavidas.html', 'Botes Salvavidas de Valparaíso', 'Una comunicación que pone al centro su labor de rescate.', ['Comunicación', 'Web', 'Redes'], ('botes-salvavidas/01.jpg', 864, 1080)),
    ('proyectos.html#logofolio', 'Bowraps', 'Naming e identidad visual para una marca de wraps y bowls que sigue vigente en Viña del Mar.', ['Naming', 'Identidad visual'], None),
    ('proyectos/khronos.html', 'Cerveza Khronos', 'Propuesta de rebranding: un nombre que encontró su sentido en "Tómate el tiempo".', ['Propuesta', 'Estrategia', 'Packaging'], ('khronos/04.jpg', 1254, 1254)),
]


def _more_card(href, name, line, tags, img):
    # EDITAR: LAB*502 y Bowraps usan un marcador hasta tener sus imágenes en alta
    media = (f'<img src="img/proyectos/{img[0]}" width="{img[1]}" height="{img[2]}" alt="" loading="lazy" decoding="async">' if img
             else '<div class="media-ph" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-image"/></svg>Imagen pendiente</div>')
    # Al pasar el mouse (o enfocar) la tarjeta muestra sus etiquetas arriba y el nombre, la línea y el enlace abajo
    return f'''
          <li>{media}
            <div class="more-info"><ul class="more-tags">{''.join(f'<li>{t}</li>' for t in tags)}</ul><div class="more-foot"><div><strong>{name}</strong><p>{line}</p></div><a class="more-go" href="{href}" aria-label="Ver proyecto: {name}"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a></div></div></li>'''


_more_arc = ''.join(_more_card(*m) for m in _more_cases)
HOME_MORE = f'''
    <!-- PROYECTOS: caso destacado + arco curvo de imágenes movido por el scroll y las flechas -->
    <section class="section more" id="proyectos" aria-labelledby="more-title">
      <div class="container more-head">
        <span class="tag tag-eyebrow">Proyectos</span>
        <h2 class="heading v2-big" id="more-title">Marcas con <strong>historia propia</strong>.</h2>
      </div>
      <div class="container">
        <article class="feat-case">
          <img src="img/proyectos/fuchi-chao/01.jpg" width="1397" height="1400" alt="Línea de productos Fuchi Chao" loading="lazy" decoding="async">
          <div class="feat-case-text">
            <span class="tag">Caso destacado</span>
            <h3 class="card-title">Fuchi Chao</h3>
            <p>De una fórmula industrial a una marca que los petlovers hacen suya. Naming, identidad y etiquetas en 2021; estrategia de marca en 2023. Hoy está en tiendas veterinarias, plataformas en línea y exposiciones de mascotas.</p>
            <a class="link-arrow" href="proyectos/fuchi-chao.html">Ver caso completo<span class="sr-only">: Fuchi Chao</span> <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
          </div>
        </article>
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
      <div class="container more-foot-cta">
        <a class="btn btn-primary" href="proyectos.html">Ver todos los proyectos <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
      </div>
    </section>
'''

# Testimonios: preparados pero fuera del build hasta tener las frases (prioridad: Sustentando, Fuchi Chao/Citrex y Uvenergy).
# EDITAR: completar foto, nombre, cargo, empresa y frase, y sumar HOME_TESTIMONIOS al body después de HOME_MORE.
_testimonios = [('Sustentando', ''), ('Fuchi Chao (Citrex)', ''), ('Uvenergy', '')]
HOME_TESTIMONIOS = '''
    <!-- TESTIMONIOS -->
    <section class="panel panel-plain section" id="testimonios" aria-labelledby="testimonios-title">
      <div class="container">
        <div class="section-head center">
          <h2 class="heading" id="testimonios-title">Lo que dicen quienes <strong>trabajaron conmigo</strong>.</h2>
        </div>
        <ul class="feature-grid testimonios" role="list">''' + ''.join(f'''
          <li class="card"><blockquote><p>{frase}</p></blockquote><p><strong>Nombre</strong> · Cargo, {empresa}</p></li>''' for empresa, frase in _testimonios) + '''
        </ul>
      </div>
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
          <p>Una idea vale cuando llega a la vida de las personas: en una etiqueta, en una vitrina, en una pantalla. Pero entre la idea y lo que la gente vive suele haber una brecha, y ahí es donde trabajo.</p>
          <p>Una marca con propósito no le dice a la gente "cómprame". Le dice "voy hacia allá, ¿vienes conmigo?". Cuando ese norte está claro, los clientes dejan de compararte por precio y empiezan a elegirte porque creen en lo mismo que tú.</p>
          <a class="btn btn-outline ideas-cta" href="#contacto">Conversemos <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
        </div>
        <a class="ideas-pill" href="proyectos.html">
          <span class="ideas-pill-btn"><span class="ideas-pill-label">Ver portafolio</span><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></span>
          <img src="img/proyectos/khronos/02.jpg" width="1254" height="1254" alt="" loading="lazy" decoding="async">
        </a>
      </div>
    </section>
'''

# ---- Secciones de la landing Marcas (textos de tools/narrativa/02-landing-marcas.md) ----
_arrow = '<svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg>'
_check = '<svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-check"/></svg>'
_ext = ' rel="noopener noreferrer" target="_blank"'
_wa_sr = '<span class="sr-only"> (WhatsApp, se abre en una pestaña nueva)</span>'
# Enlaces de casos (LAB*502 se crea en la fase 4; Bowraps vive en Logofolio)
_case = {
    'Uvenergy': 'proyectos/uv-energy.html', 'Uvenergy (2023)': 'proyectos/uv-energy.html', 'Uvenergy (2025)': 'proyectos/uv-energy.html',
    'Fuchi Chao (2021)': 'proyectos/fuchi-chao.html', 'Fuchi Chao (2023)': 'proyectos/fuchi-chao.html',
    'Sustentando': 'proyectos/sustentando.html', 'Khronos (propuesta)': 'proyectos/khronos.html', 'LAB*502': 'proyectos/lab502.html',
    'Botes Salvavidas de Valparaíso': 'proyectos/botes-salvavidas.html', 'Bowraps': 'proyectos.html#logofolio',
}


def _cases(names):
    return ' · '.join(f'<a href="{_case[n]}">{n}</a>' for n in names)


# 3. ¿Cuándo es momento de trabajar tu marca?
_momentos = [
    ('Cuando nace', 'Vas a lanzar un negocio, un producto o una línea nueva y quieres partir bien.', ['Uvenergy (2023)', 'Fuchi Chao (2021)']),
    ('Cuando crece', 'Sumaste servicios, clientes o equipo, y tu marca ya no cuenta todo lo que haces.', ['Fuchi Chao (2023)', 'Uvenergy (2025)', 'Sustentando']),
    ('Cuando compite', 'Te comparan solo por precio o te confunden con la competencia.', ['Khronos (propuesta)']),
    ('Cuando cambia el rumbo', 'Tu negocio se transforma, entra a un mercado nuevo o busca financiamiento.', ['LAB*502']),
    ('Cuando no te reconocen', 'La gente no sabe bien qué haces o te confunde con otros.', ['Botes Salvavidas de Valparaíso']),
]
HOME_MOMENTOS = '''
    <!-- ¿CUÁNDO ES MOMENTO DE TRABAJAR TU MARCA? -->
    <section class="panel section momentos" id="momentos" aria-labelledby="momentos-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">Antes de empezar</span>
          <h2 class="heading" id="momentos-title">¿Cuándo es momento de <strong>trabajar tu marca</strong>?</h2>
          <p class="lead">No hace falta esperar a que algo falle. Hay momentos en que invertir en tu marca rinde más que en cualquier otra cosa.</p>
        </div>
        <ol class="momentos-grid">''' + ''.join(f'''
          <li class="card momento"><span class="momento-num">{i:02d}</span><h3 class="card-title">{t}</h3><p>{d}</p><p class="momento-casos">{_cases(c)}</p></li>''' for i, (t, d, c) in enumerate(_momentos, 1)) + f'''
        </ol>
        <p class="momentos-cierre">¿Te reconociste en uno de estos momentos? <a class="link-arrow" href="#contacto">Conversemos {_arrow}</a></p>
      </div>
    </section>
'''

# 4. Servicios: dos niveles con imagen y el detalle debajo (opción B elegida; el diseño se trabajará después)
_servicios = [
    dict(t='Identidad visual', img=('fuchi-chao/02.jpg', 2000, 1132), tags=['Naming', 'Identidad'],
         para='Tu negocio ya sabe quién es y necesita verse a la altura.',
         si='estás por abrir, tienes un producto que llega a góndola o tu imagen actual quedó atrás.',
         no='solo buscas un logo rápido y barato.',
         inc='conversación inicial, naming si hace falta, logotipo, paleta, tipografía, aplicaciones (etiquetas, packaging, papelería, redes) y manual de uso.',
         casos=['Bowraps', 'Fuchi Chao (2021)'], btn='Quiero mi identidad visual'),
    dict(t='Branding estratégico', img=('sustentando/02.jpg', 1200, 1200), tags=['Estrategia', 'Brand Compass'],
         para='Tu negocio necesita diferenciarse, crecer o cambiar de rumbo, y tu marca tiene que mostrar el camino.',
         si='te comparan por precio, sumaste líneas de negocio o tu equipo explica la empresa de formas distintas.',
         no='necesitas resultados para mañana: la estrategia toma tiempo y tu participación.',
         inc='research de mercado y competencia, Brand Compass (propósito, diferencial, personalidad y promesa), líneas de negocio, experiencia de marca (cómo se vive tu marca en cada punto de contacto, desde la vitrina hasta la atención), cultura interna (que tu equipo entienda la marca y la transmita), identidad visual y manual de marca.',
         casos=['LAB*502', 'Fuchi Chao (2023)', 'Uvenergy', 'Sustentando'], btn='Quiero trabajar mi estrategia'),
]


def _servicio(s):
    f, w, h = s['img']
    return f'''
          <article class="svc-level">
            <div class="svc-card">
              <img class="svc-card-img" src="img/proyectos/{f}" width="{w}" height="{h}" alt="" loading="lazy" decoding="async">
              <span class="svc-card-top"><ul class="svc-tags" aria-hidden="true">{''.join(f'<li>{t}</li>' for t in s['tags'])}</ul></span>
              <span class="svc-card-body"><h3 class="svc-card-title">{s['t']}</h3><span class="svc-card-desc">{s['para']}</span></span>
            </div>
            <div class="svc-level-detail">
              <dl class="svc-fit"><div><dt>Es para ti si</dt><dd>{s['si']}</dd></div><div><dt>No es para ti si</dt><dd>{s['no']}</dd></div></dl>
              <p><strong>Incluye:</strong> {s['inc']}</p>
              <p class="svc-casos"><span>Casos</span>{_cases(s['casos'])}</p>
              <a class="btn btn-primary" href="{WA_MARCAS}"{_ext}>{s['btn']}{_wa_sr} {_arrow}</a>
            </div>
          </article>'''


HOME_SERVICIOS = '''
    <!-- SERVICIOS: dos niveles (identidad visual y branding estratégico) + complemento web -->
    <section class="panel section svc-levels" id="servicios" aria-labelledby="servicios-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">Servicios</span>
          <h2 class="heading" id="servicios-title">Dos formas de <strong>trabajar tu marca</strong>.</h2>
          <p class="lead">Puedes partir por la identidad y sumar estrategia cuando tu negocio lo necesite. Así lo hizo Fuchi Chao.</p>
        </div>
        <div class="svc-levels-grid">''' + ''.join(_servicio(s) for s in _servicios) + f'''
        </div>
        <div class="card svc-extra">
          <div>
            <h3 class="card-title">Complemento: sitios web y ecommerce</h3>
            <p>Tu marca también vive en internet. Diseño sitios y tiendas en línea que guían a tus clientes a escribirte o comprarte, e incluyo un diagnóstico de cumplimiento de la Ley 21.719 con AuditorWeb.</p>
            <p class="svc-casos"><span>Casos</span>{_cases(['Uvenergy', 'Botes Salvavidas de Valparaíso', 'Sustentando'])}</p>
          </div>
          <a class="btn btn-outline" href="{WA_MARCAS}"{_ext}>Conversemos sobre tu sitio{_wa_sr} {_arrow}</a>
        </div>
      </div>
    </section>
'''

# 5. Cómo trabajo: cinco pasos
_pasos = [
    ('Diferenciar', 'Investigo tu mercado y tu competencia, y con un Brand Compass definimos tu propósito, tu diferencial, tu personalidad y tu promesa.'),
    ('Colaborar', 'Trabajamos contigo y, cuando el proyecto lo pide, con fotógrafos, realizadores y otros creadores.'),
    ('Innovar', 'Convierto la estrategia en un concepto y en la experiencia que tus clientes deberían vivir con tu marca, de principio a fin. Luego te presento tres caminos visuales distintos para que elijas cómo quieres verte.'),
    ('Validar', 'Validamos el camino elegido principalmente contigo y, cuando el proyecto lo permite, también con tus clientes, antes de aplicarlo a todas las piezas.'),
    ('Cultivar', 'Llevamos la marca hacia adentro: tu equipo la entiende, la hace suya y la transmite en cada contacto con tus clientes. Te entrego un manual y plantillas para mantenerla viva, y puedo acompañarte mientras crece, como con Sustentando desde 2022.'),
]
HOME_PROCESO = '''
    <!-- CÓMO TRABAJO -->
    <section class="panel panel-plain section proceso" id="proceso" aria-labelledby="proceso-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">Método</span>
          <h2 class="heading" id="proceso-title">Cinco pasos para una marca <strong>que se elige</strong>.</h2>
          <p class="lead">Trabajo con las cinco disciplinas, porque una marca no es lo que tú dices que eres: es lo que tus clientes sienten.</p>
        </div>
        <div class="steps-scroller" role="region" aria-label="Pasos del método" tabindex="0">
          <ol class="steps">''' + ''.join(f'''
            <li class="card step"><p class="step-eyebrow">Paso {i:02d}</p><h3 class="title">{t}</h3><p>{d}</p></li>''' for i, (t, d) in enumerate(_pasos, 1)) + '''
          </ol>
        </div>
      </div>
    </section>
'''

# 7. Sobre mí (versión corta) y preguntas frecuentes
HOME_SOBRE = '''
    <!-- SOBRE MÍ -->
    <section class="panel panel-plain section about" id="sobre-mi" aria-labelledby="sobre-title">
      <div class="container">
        <div class="two-col about-grid">
          <!-- EDITAR: reemplazar por un retrato trabajando, no de estudio (opcional: video de 60 segundos) -->
          <figure class="portrait">
            <img src="img/marca/luis-vicencio-retrato.png" width="750" height="900" alt="Retrato de Luis Vicencio" loading="lazy" decoding="async">
          </figure>
          <div class="about-text">
            <span class="tag tag-eyebrow">Sobre mí</span>
            <h2 class="heading" id="sobre-title">Llevo el mundo de las ideas <strong>a los productos del día a día</strong>.</h2>
            <!-- EDITAR: confirmar si se mantiene la mención a Argentina y Alemania -->
            <p>Soy Luis Vicencio, diseñador de la Universidad de Valparaíso, con estudios de Product Design for Innovation en el Politecnico di Milano y un diplomado en Branding Estratégico. He trabajado con marcas en Chile, Argentina y Alemania.</p>
            <p>Cada proyecto me dejó una herramienta nueva: empecé diseñando identidades, sumé la estrategia de marca y hoy también lidero productos digitales. Me mueve ayudar a que las empresas crezcan, que su marca se viva por dentro y por fuera, y hacerlo en colaboración con otros creadores y con los propios clientes.</p>
            <!-- "Ver mi trayectoria" abre el panel lateral hasta que exista sobre-mi.html (fase 5) -->
            <div class="about-links">
              <button class="link-arrow" type="button" data-drawer-open="trayectoria" aria-haspopup="dialog" aria-controls="trayectoria">Ver mi trayectoria ''' + _arrow + '''</button>
              <a class="link-arrow" href="producto-digital.html">¿Tienes un producto digital? Conoce cómo trabajo con equipos de software ''' + _arrow + '''</a>
            </div>
          </div>
        </div>
      </div>
    </section>
'''

_preguntas = [
    ('¿Cuándo es momento de trabajar mi marca?', 'Cuando nace tu negocio, cuando crece, cuando te comparan solo por precio, cuando cambia el rumbo o cuando la gente no sabe bien qué haces. Si te reconoces en alguno, es buen momento.'),
    ('¿Puedo partir solo con la identidad visual?', 'Sí. Muchas marcas parten por la identidad y suman estrategia cuando el negocio crece, como Fuchi Chao.'),
    ('¿Qué es un Brand Compass?', 'Una herramienta para definir el propósito, el diferencial, la personalidad y la promesa de tu marca. Es el norte que guía todo lo demás.'),
    ('¿Cuánto cuesta?', 'Depende del nivel y del alcance. Después de una primera conversación te envío una propuesta con alcance, plazos y valor cerrado.'),
    ('¿Cuánto demora?', 'Una identidad visual o un sitio corporativo suele tomar entre cuatro y ocho semanas, según los contenidos y las rondas de revisión. Un proyecto de branding estratégico toma más tiempo, según su alcance; lo definimos en la propuesta.'),
    ('¿Trabajas con otros creadores?', 'Sí. Cuando el proyecto lo pide, sumo fotógrafos, realizadores o diseñadores, y coordino el trabajo.'),
]
HOME_PREGUNTAS = '''
    <!-- PREGUNTAS FRECUENTES -->
    <section class="panel section" id="preguntas" aria-labelledby="faq-title">
      <div class="container">
        <div class="narrow">
          <div class="section-head center">
            <h2 class="heading" id="faq-title">Preguntas <strong>frecuentes</strong>.</h2>
          </div>
          <div class="faq">''' + ''.join(f'''
            <details class="card">
              <summary>{q}</summary>
              <p>{a}</p>
            </details>''' for q, a in _preguntas) + '''
          </div>
        </div>
      </div>
    </section>
'''

HOME_TRAYECTORIA = '''
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
'''

page('index.html', 'Luis Vicencio · Branding e identidad de marca para pymes en Chile',
     'Diseño marcas para pymes y empresas: estrategia, identidad visual, packaging y sitios web. Más de 7 años creando marcas que la gente quiere seguir.',
     current='marcas', html_class='home motion v2', canonical='', extra_css='css/home-v2.css',
     cta_title='Conversemos sobre <strong>tu marca</strong>.',
     cta_lead='Cuéntame en qué momento está tu negocio y qué sientes que tu marca no está logrando. Te respondo con una propuesta de alcance, plazos y presupuesto.',
     wa_href=WA_MARCAS, email_subject='',
     body=HOME_HERO + HOME_MARQUEE + HOME_IDEAS + HOME_MOMENTOS + HOME_SERVICIOS + HOME_PROCESO + HOME_MORE + HOME_SOBRE + HOME_TRAYECTORIA + HOME_PREGUNTAS)
