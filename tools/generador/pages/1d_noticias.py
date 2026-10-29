# Noticias: cada tema del inicio (y de la antigua landing de producto digital) es una página propia en noticias/
# (español) y en en/noticias/ (inglés). Los textos en español vienen de las secciones que se retiraron de la landing
# de producto digital y de "¿Cuándo es momento de trabajar tu marca?" (_momentos en 1_index.py). Se listan en el bloque
# Blog del inicio (1a_inicio.py). La versión en inglés está pendiente de revisión de Luis.

_noticias_proyecto = {'Legisnova': 'proyectos/bytequest.html', 'Yomecontrolo': 'proyectos/yomecontrolo.html',
                      'AuditorWeb 21.719': 'proyectos/auditorweb.html'}

_ES = dict(inicio='Inicio', noticias='Noticias', volver='Volver a las noticias', autor='Autor', categoria='Categoría', lang='es')
_EN = dict(inicio='Home', noticias='News', volver='Back to news', autor='Author', categoria='Category', lang='en')

# Imagen de portada de las noticias que ya la tienen (archivo en img/noticias/<slug>.webp), con texto alternativo por idioma
_IMAGEN_PORTADA = {
    'cuando-trabajar-tu-marca': {
        'es': 'Silueta de perfil de una persona frente a un disco naranja, con paneles de vidrio translúcido y la sombra de una hoja.',
        'en': 'Profile silhouette of a person in front of a large orange disc, with translucent glass panels and the shadow of a leaf.',
    },
    'metodo-scrum': {
        'es': 'Persona cruzando una secuencia de bloques de piedra y paneles de vidrio, unidos por una cinta naranja.',
        'en': 'A person stepping across a sequence of stone blocks and glass panels, joined by an orange ribbon.',
    },
}


def _noticia(slug, titulo, bajada, cuerpo, etiqueta, idioma=_ES):
    """Página de una noticia con el mismo formato que la política de privacidad: encabezado, índice y texto."""
    en = idioma['lang'] == 'en'
    path = f'en/noticias/{slug}.html' if en else f'noticias/{slug}.html'
    # Desde en/noticias/ el inicio en inglés es {p}en/index.html; desde noticias/ es {p}index.html
    inicio_href = '{p}en/index.html' if en else '{p}index.html'
    noticias_href = inicio_href + '#blog'
    alt = _IMAGEN_PORTADA.get(slug, {}).get(idioma['lang'])
    figura = (f'\n          <figure class="noticia-portada"><img src="{{p}}img/noticias/{slug}.webp" width="1672" height="941" alt="{alt}"></figure>' if alt else '')
    # Composición: enlace de vuelta a la izquierda; título, bajada y datos a la derecha; imagen a ancho completo debajo
    body = f'''
    <section class="hero-shell" aria-labelledby="page-title">
      <div class="shell-body frame-grid page-hero noticia-hero">
        <div class="container">
          <div class="noticia-cabecera">
            <a class="link-arrow noticia-volver" href="{noticias_href}">&larr; {idioma['volver']}</a>
            <div>
              <h1 class="noticia-h1" id="page-title">{titulo}</h1>
              <p class="lead">{bajada}</p>
              <dl class="noticia-meta">
                <div><dt>{idioma['autor']}</dt><dd>Luis Vicencio</dd></div>
                <div><dt>{idioma['categoria']}</dt><dd>{etiqueta}</dd></div>
              </dl>
            </div>
          </div>{figura}
        </div>
      </div>
    </section>

    <section class="panel panel-plain section" aria-label="{'Content of the news item' if en else 'Contenido de la noticia'}">
      <div class="container">
        <div class="narrow prose">
{cuerpo}
          <p><a class="link-arrow" href="{noticias_href}">{idioma['volver']}</a></p>
        </div>
      </div>
    </section>
'''
    alternos = {'es-CL': f'noticias/{slug}.html', 'en': f'en/noticias/{slug}.html', 'x-default': f'noticias/{slug}.html'}
    cta = dict(cta_title='Let’s talk about <strong>your project</strong>.',
               cta_lead='Tell me what stage your brand or product is at, and I will reply with a proposal for scope, timelines and budget.') if en else {}
    page(path, f'{titulo} · Luis Vicencio', bajada, body=body, current='noticias', contact=True,
         lang=idioma['lang'], alternates=alternos if en else {'es-CL': f'noticias/{slug}.html', 'en': f'en/noticias/{slug}.html', 'x-default': f'noticias/{slug}.html'}, **cta)


def _lista(items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


# ---------- Español ----------

# 1. Cuándo trabajar la marca
_momentos_html = ''.join(
    f'<h2>{titulo}</h2><p>{texto}</p>' + (f'<p class="muted">Proyectos: {", ".join(casos)}.</p>' if casos else '')
    for titulo, texto, casos in _momentos)
_noticia('cuando-trabajar-tu-marca', '¿Cuándo es momento de trabajar tu marca?',
         'Cuando nace tu negocio, cuando crece, cuando te comparan por precio, cuando cambia el rumbo o cuando la gente no sabe bien qué haces.',
         _momentos_html, 'Marca')

# 2. Problema: un buen equipo no basta si nadie ordena el camino (landing de producto digital)
_noticia('un-buen-equipo-no-basta', 'Un buen equipo técnico no basta si nadie ordena el camino',
         'Son señales que se repiten en productos digitales: el cliente pide una cosa, el equipo entrega otra y nadie tiene claro qué construir primero.',
         '<p>¿Te suena alguna de estas situaciones?</p>' + _lista([
             'El cliente pide una cosa y el equipo entrega otra.',
             'Los requerimientos llegan difusos y el desarrollo se alarga.',
             'Nadie tiene claro qué construir primero ni por qué.',
             'Hay muchas ideas con IA, pero ninguna llega a producción.',
             'El producto funciona, pero no tiene identidad y nadie lo entiende a la primera.']) +
         '<p>Mi trabajo es ser el puente entre tu negocio, tu cliente y tu equipo técnico.</p>',
         'Producto digital')

# 3. Servicios: tres roles que normalmente se contratan por separado
_noticia('tres-roles-de-producto', 'Tres roles que normalmente contratas por separado',
         'Product Owner, estrategia de marca para productos y UX/UI con prototipos con IA. Los tres en una misma persona, con un norte claro.',
         '<h2>Product Owner</h2><p>Represento a tu negocio frente al equipo técnico. Traduzco lo que el cliente necesita en historias de usuario claras, ordeno el backlog y reviso que cada entrega cumpla lo esperado.</p>'
         '<p class="muted">Incluye: comprensión del negocio, historias de usuario, roadmap y backlog priorizado, ceremonias Scrum, QA de cada historia, gestión de expectativas e informes de avance.</p>'
         '<h2>Estrategia de marca para productos</h2><p>Un producto sin identidad se explica peor y se vende peor. Defino el propósito, la voz y la identidad del producto o de la empresa que lo construye.</p>'
         '<p class="muted">Incluye: Brand Compass, naming, identidad visual, voz y sitio web.</p>'
         '<h2>UX/UI y prototipos con IA</h2><p>Diseño la experiencia y la llevo a un prototipo funcional con desarrollo asistido por IA, para validar antes de invertir en desarrollo. Después lo traspaso a tu equipo para producción.</p>'
         '<p class="muted">Incluye: flujos, prototipos navegables o funcionales, diseño de interfaces y traspaso al equipo de desarrollo.</p>',
         'Servicios')

# 4. Proceso: Scrum, con los pies en el negocio
_noticia('metodo-scrum', 'Scrum, con los pies en el negocio',
         'Desde el inicio acordamos prioridades, responsables y entregables, y reviso las señales de alerta en cada sprint para corregir el rumbo a tiempo.',
         '<ol>' + ''.join(f'<li><strong>{n}.</strong> {d}</li>' for n, d in [
             ('Comprender el negocio', 'Me reúno con tu equipo y con tu cliente para entender quiénes son los usuarios, qué necesitan y qué se espera del producto.'),
             ('Definir', 'Escribo las historias de usuario, armo el roadmap y priorizamos juntos qué se construye primero.'),
             ('Construir por sprints', 'El equipo entrega avances en ciclos cortos; yo coordino, despejo bloqueos y mantengo informadas a todas las partes.'),
             ('Revisar', 'Hago QA de cada historia de usuario: no se da por terminada hasta que cumple lo esperado.'),
             ('Ajustar', 'En cada revisión vemos lo construido, aprendemos y corregimos el rumbo.')]) + '</ol>'
         '<h2>Lo que me llevé</h2><p>Aprendí a reconocer las alertas tempranas de un proyecto: prioridades difusas, decisiones sin responsable claro y expectativas sin acordar. Hoy las reviso desde el primer día.</p>',
         'Método')

# 5. Casos: productos con IA para organizaciones exigentes
_noticia('productos-con-ia', 'Productos con IA para organizaciones exigentes',
         'Creé la marca y lideré el producto de soluciones con IA en Bytequest, Yomecontrolo y AuditorWeb, entre otros.',
         '<p>Creé la marca de la empresa y lideré el producto de soluciones con IA como Legisnova, la agenda legislativa del Congreso en un solo lugar; un auditor que analiza llamadas de emergencia según protocolo; y un asistente virtual multiagente para una institución del sistema de justicia, entre otras.</p>'
         + '<h2>Casos</h2>' + ''.join(
             f'<h3><a href="{{p}}{_noticias_proyecto[n]}">{n}</a></h3><p>{l}</p>' for n, l in [
                 ('Legisnova', 'Propuse los planes Parlamentario e Independiente, escribí las historias de usuario y aseguré con QA cada entrega.'),
                 ('Yomecontrolo', 'Estrategia, experiencia y diseño del MVP de una startup de salud preventiva. La marca sigue en uso.'),
                 ('AuditorWeb 21.719', 'Producto propio: la Ley 21.719 convertida en un informe automático y accionable.')]),
         'Casos')

# 6. Modalidad: cómo trabajamos juntos
_noticia('modalidad-de-trabajo', 'Cómo trabajamos juntos',
         'Puedo integrarme a tu equipo por un período, tomar un producto por proyecto o trabajar en remoto, en español o inglés.',
         _lista(['<strong>Por período:</strong> me integro a tu equipo durante un tiempo definido como Product Owner o líder de marca y producto.',
                 '<strong>Por proyecto:</strong> tomo un producto o una etapa (discovery, MVP, lanzamiento) con alcance y entregables cerrados.',
                 '<strong>Remoto:</strong> en español o inglés.']),
         'Modalidad')

# ---------- Inglés (en/noticias/) ----------

_noticia('cuando-trabajar-tu-marca', 'When is it time to work on your brand?',
         'When your business is born, when it grows, when you are compared on price, when your direction changes, or when people do not quite know what you do.',
         '<h2>When it is born</h2><p>You are about to launch a business, a product or a new line and want to start on the right foot.</p><p class="muted">Projects: Uvenergy (2023), Fuchi Chao (2021).</p>'
         '<h2>When it grows</h2><p>You added services, clients or team, and your brand no longer tells everything you do.</p><p class="muted">Projects: Fuchi Chao (2023), Uvenergy (2025), Sustentando.</p>'
         '<h2>When it competes</h2><p>People compare you only on price, or confuse you with the competition.</p><p class="muted">Projects: Khronos (proposal).</p>'
         '<h2>When direction changes</h2><p>Your business transforms, enters a new market or looks for funding.</p><p class="muted">Projects: LAB*502.</p>'
         '<h2>When people do not recognize you</h2><p>People do not quite know what you do, or confuse you with others.</p><p class="muted">Projects: Botes Salvavidas de Valparaíso.</p>',
         'Brand', _EN)

_noticia('un-buen-equipo-no-basta', 'A good tech team is not enough if no one sets the course',
         'These are signs that repeat in digital products: the client asks for one thing, the team delivers another, and no one is clear on what to build first.',
         '<p>Does any of this sound familiar?</p>' + _lista([
             'The client asks for one thing and the team delivers another.',
             'Requirements arrive vague and development drags on.',
             'No one is clear on what to build first, or why.',
             'Many AI ideas, but none reaches production.',
             'The product works, but it has no identity and people do not get it at first sight.']) +
         '<p>My job is to be the bridge between your business, your client and your tech team.</p>',
         'Digital product', _EN)

_noticia('tres-roles-de-producto', 'Three roles you usually hire separately',
         'Product Owner, brand strategy for products, and UX/UI with AI prototypes. All three in one person, with a clear direction.',
         '<h2>Product Owner</h2><p>I represent your business in front of the tech team. I turn what the client needs into clear user stories, order the backlog and check that every delivery meets expectations.</p>'
         '<p class="muted">Includes: understanding of the business, user stories, roadmap and prioritized backlog, Scrum ceremonies, QA of each story, expectation management and progress reports.</p>'
         '<h2>Brand strategy for products</h2><p>A product without identity is explained worse and sells worse. I define the purpose, voice and identity of the product or of the company that builds it.</p>'
         '<p class="muted">Includes: Brand Compass, naming, visual identity, voice and website.</p>'
         '<h2>UX/UI and AI prototypes</h2><p>I design the experience and take it to a functional prototype with AI-assisted development, to validate before investing in development. Then I hand it over to your team for production.</p>'
         '<p class="muted">Includes: flows, clickable or functional prototypes, interface design and handover to the development team.</p>',
         'Services', _EN)

_noticia('metodo-scrum', 'Scrum, grounded in the business',
         'From the start we agree on priorities, owners and deliverables, and I review warning signs in every sprint to correct course in time.',
         '<ol>' + ''.join(f'<li><strong>{n}.</strong> {d}</li>' for n, d in [
             ('Understand the business', 'I meet with your team and your client to understand who the users are, what they need and what is expected from the product.'),
             ('Define', 'I write the user stories, build the roadmap, and we prioritize together what gets built first.'),
             ('Build in sprints', 'The team delivers progress in short cycles; I coordinate, clear blockers and keep every party informed.'),
             ('Review', 'I QA every user story: it is not considered done until it meets expectations.'),
             ('Adjust', 'At each review we look at what was built, learn and correct course.')]) + '</ol>'
         '<h2>What I learned</h2><p>I learned to recognize the early warning signs of a project: vague priorities, decisions without a clear owner and expectations not agreed. Today I check them from day one.</p>',
         'Method', _EN)

_noticia('productos-con-ia', 'AI products for demanding organizations',
         'I created the brand and led the AI solutions product at Bytequest, Yomecontrolo and AuditorWeb, among others.',
         '<p>I created the company’s brand and led the AI solutions product, such as Legisnova, the legislative agenda of the Congress in one place; an auditor that analyzes emergency calls according to protocol; and a multi-agent virtual assistant for an institution in the justice system, among others.</p>'
         + '<h2>Cases</h2>' + ''.join(
             f'<h3><a href="{{p}}{_noticias_proyecto[n]}">{n}</a></h3><p>{l}</p>' for n, l in [
                 ('Legisnova', 'I proposed the Parliamentary and Independent plans, wrote the user stories and checked every delivery with QA.'),
                 ('Yomecontrolo', 'Strategy, experience and design of the MVP of a preventive health startup. The brand is still in use.'),
                 ('AuditorWeb 21.719', 'Own product: Law 21.719 turned into an automatic, actionable report.')]),
         'Cases', _EN)

_noticia('modalidad-de-trabajo', 'How we work together',
         'I can join your team for a period, take on a product per project, or work remotely, in Spanish or English.',
         _lista(['<strong>For a period:</strong> I join your team for a defined time as Product Owner or brand and product lead.',
                 '<strong>Per project:</strong> I take on a product or a stage (discovery, MVP, launch) with a closed scope and deliverables.',
                 '<strong>Remote:</strong> in Spanish or English.']),
         'Format', _EN)
