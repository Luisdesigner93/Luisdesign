# Noticias: cada tema del inicio (y de la antigua landing de producto digital) es una página propia en noticias/
# (español) y en en/noticias/ (inglés). Los textos en español vienen de las secciones que se retiraron de la landing
# de producto digital y de "¿Cuándo es momento de trabajar tu marca?" (_momentos en 1_index.py). Se listan en el bloque
# Blog del inicio (1a_inicio.py). La versión en inglés está pendiente de revisión de Luis.

_noticias_proyecto = {'Legisnova': 'proyectos/bytequest.html', 'Yomecontrolo': 'proyectos/yomecontrolo.html',
                      'AuditorWeb 21.719': 'proyectos/auditorweb.html'}

_ES = dict(inicio='Inicio', noticias='Blog', volver='Volver al blog', autor='Autor', categoria='Categoría', lang='es')
_EN = dict(inicio='Home', noticias='Blog', volver='Back to blog', autor='Author', categoria='Category', lang='en')

# Imagen de portada de las noticias que ya la tienen (archivo en img/noticias/<slug>.webp), con texto alternativo por idioma
_IMAGEN_PORTADA = {
    'cuando-trabajar-tu-marca': {
        'es': 'Silueta de perfil de una persona entre paneles de vidrio translúcido y esmerilado, con un panel verde lima detrás.',
        'en': 'Profile silhouette of a person between translucent and frosted glass panels, with a lime green panel behind.',
    },
    'un-buen-equipo-no-basta': {
        'es': 'Cuatro personas reunidas alrededor de un computador sobre bloques de concreto, entre paneles de vidrio y un panel verde lima.',
        'en': 'Four people gathered around a laptop on concrete blocks, between glass panels and a lime green panel.',
    },
    'ley-21719-prepara-tu-web': {
        'es': 'Balanza de justicia, un computador y un documento sobre bloques de concreto, junto a paneles de vidrio y un panel verde lima.',
        'en': 'A justice scale, a laptop and a document on concrete blocks, beside glass panels and a lime green panel.',
    },
    'tres-roles-de-producto': {
        'es': 'Mano sosteniendo un lápiz frente a paneles de vidrio translúcido y uno verde lima.',
        'en': 'A hand holding a pencil in front of translucent glass panels and a lime green one.',
    },
    'metodo-scrum': {
        'es': 'Persona subiendo una escalera de bloques de concreto junto a paneles de vidrio y un arco verde lima con una flecha.',
        'en': 'A person climbing a staircase of concrete blocks beside glass panels and a lime green arc with an arrow.',
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

    <section class="panel panel-plain section" aria-label="{'Content of the article' if en else 'Contenido del artículo'}">
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

# 3. Servicios: artículo sobre el diseño más allá del diseño (negocio, marca y producto digital)
_noticia('tres-roles-de-producto', 'Diseñar va más allá de diseñar: negocio, marcas y productos digitales',
         'En todos esos casos, el diseño puede aportar mucho más que una solución visual.',
         '<p>Hay proyectos que parten con una buena idea, pero no saben muy bien cómo llevarla a la realidad. Otros tienen un equipo técnico capaz de construir casi cualquier cosa, pero necesitan definir qué vale la pena construir. Y también están los que tienen un buen producto, pero no logran comunicar por qué alguien debería elegirlo.</p><p>En todos esos casos, el diseño puede aportar mucho más que una solución visual.</p><p>Con el tiempo, mi trabajo como diseñador me ha llevado a involucrarme en distintas etapas de un proyecto: desde entender el negocio y definir una estrategia de marca, hasta organizar el desarrollo de un producto digital y diseñar la experiencia de quienes lo utilizan.</p><p>Esa combinación me permite abordar los proyectos desde una perspectiva más amplia, conectando las ideas con las personas que las necesitan y con los equipos que deben hacerlas realidad.</p><h2>Entender el problema antes de buscar la solución</h2><p>No siempre lo que un negocio necesita es una nueva web, una aplicación o una identidad visual. A veces, lo que falta es claridad: entender qué problema se quiere resolver, cuáles son las prioridades y qué camino tiene más sentido seguir.</p><p>Por eso, antes de pensar en soluciones, me interesa comprender el contexto. Qué busca el negocio, qué necesitan sus usuarios y qué condiciones existen para llevar una idea a la práctica.</p><p>Esta mirada también es parte de mi trabajo como Product Owner. En ese rol, conecto las necesidades del negocio con el equipo técnico, transformando ideas y objetivos en tareas concretas que se puedan desarrollar, probar y mejorar.</p><p>Trabajo con historias de usuario, roadmap y backlog priorizado, participo en las ceremonias Scrum y reviso las entregas para comprobar que respondan a lo definido. También ayudo a ordenar las expectativas y mantener al equipo enfocado en lo que realmente importa.</p><p>En pocas palabras, ayudo a que todos entiendan qué estamos construyendo, por qué lo hacemos y cuál es el siguiente paso.</p><h2>Darle sentido a lo que una marca quiere construir</h2><p>Una vez que entendemos el negocio y su propuesta, aparece otra pregunta: ¿cómo hacemos que las personas comprendan su valor?</p><p>Una marca no es solamente un logotipo o un sistema de colores. Es la forma en que una empresa o un producto se presenta, se diferencia y construye una relación con las personas. Cuando esa identidad no está bien definida, comunicar una buena idea puede volverse mucho más difícil.</p><p>Desde la estrategia de marca, trabajo en encontrar ese sentido y convertirlo en una dirección clara. Defino el propósito, el posicionamiento y los elementos que permiten expresar lo que hace diferente a un producto o a la empresa detrás de él.</p><p>Esto puede incluir un Brand Compass para orientar las decisiones de marca, el desarrollo de un nombre, la identidad visual, la voz y el tono de comunicación, e incluso el diseño de su sitio web.</p><p>La idea es que cada decisión tenga una razón de ser y que la marca no solo se vea bien, sino que también ayude a comunicar mejor lo que ofrece.</p><h2>Convertir las ideas en experiencias que podamos probar</h2><p>Cuando trabajamos con productos digitales, hay una distancia importante entre tener una idea y saber si realmente funciona para las personas que la van a utilizar.</p><p>El diseño UX/UI ayuda a reducir esa distancia. Me permite explorar cómo debería funcionar un producto, qué pasos necesita seguir una persona y cómo podemos hacer que la experiencia sea más intuitiva, útil y coherente con los objetivos del negocio.</p><p>Trabajo en los flujos de usuario, la estructura de navegación, el diseño de interfaces y los prototipos que permiten explorar una solución antes de desarrollarla por completo.</p><p>Además, incorporo herramientas de inteligencia artificial para llevar algunas de estas ideas a prototipos navegables o funcionales con mayor rapidez. Así podemos visualizar mejor la propuesta, probar alternativas y detectar oportunidades de mejora antes de comprometer más recursos en el desarrollo.</p><p>Una vez que tenemos una dirección clara, preparo el diseño y el traspaso al equipo técnico para que la solución pueda implementarse en producción.</p><h2>Una mirada que conecta las distintas partes del proyecto</h2><p>Mi trabajo no se limita a una sola etapa ni a una única disciplina. Me interesa entender cómo se relacionan el negocio, la marca, la experiencia de usuario y la tecnología, porque las decisiones que tomamos en un área terminan influyendo en las demás.</p><p>Esa perspectiva me permite colaborar con perfiles distintos, conversar tanto con personas de negocio como con equipos técnicos y ayudar a que las decisiones de diseño respondan a necesidades concretas.</p><p>No se trata de hacer de todo, sino de entender qué necesita cada proyecto y aportar desde el lugar donde puedo generar más valor: dando dirección a las ideas, convirtiéndolas en soluciones y ayudando a que lleguen a las personas para las que fueron pensadas.</p><p>Al final, diseñar también consiste en conectar las piezas para que las cosas funcionen mejor.</p>',
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

# 7. Normativa: prepara tu web ante la Ley 21.719
_noticia('ley-21719-prepara-tu-web', 'Ley 21.719 prepara tu web ante multas',
         'La Ley 21.719 está prevista para entrar en vigor a fines de 2026. Revisa formularios, cookies y avisos de privacidad de tu web antes de esa fecha.',
         '<p>La Ley 21.719 moderniza la Ley 19.628, la normativa vigente sobre datos personales en Chile. Cambia la forma en que las empresas recogen, usan y protegen la información de las personas, y eso incluye a tu web cada vez que recibe datos desde un formulario, una cookie o una herramienta de analítica.</p>'
         '<h2>Qué está previsto</h2><p>La ley se publicó en diciembre de 2024 y su entrada en vigor está prevista para el 1 de diciembre de 2026. También hay un proyecto que propone postergarla. Antes de planificar cambios, revisa el estado vigente en la Biblioteca del Congreso Nacional (bcn.cl).</p>'
         '<h2>Qué revisar en tu web</h2>' + _lista([
             '<strong>Formularios:</strong> pide solo los datos que necesitas y explica para qué los usas.',
             '<strong>Cookies y analítica:</strong> informa qué herramientas usas y pide consentimiento cuando corresponda.',
             '<strong>Aviso de privacidad:</strong> debe ser claro, fácil de encontrar y explicar cómo ejercer tus derechos.',
             '<strong>Derechos de las personas:</strong> acceso, rectificación, supresión, oposición y portabilidad, con un canal para responder.',
             '<strong>Proveedores:</strong> revisa qué servicios externos reciben datos de tus usuarios.']) +
         '<h2>Por dónde empezar</h2><p>Hago un inventario de los datos que recoge tu sitio, reviso los textos legales y ajusto la experiencia para que la privacidad sea parte del diseño y no un parche al final. Si quieres ver cómo abordé la ley en un producto propio, revisa <a href="{p}proyectos/auditorweb.html">AuditorWeb 21.719</a>.</p>'
         '<p class="muted">Esta nota es una orientación general y no reemplaza una asesoría legal.</p>',
         'Normativa')

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

_noticia('tres-roles-de-producto', 'Design goes beyond design: business, brands and digital products',
         'In all those cases, design can offer much more than a visual solution.',
         '<p>There are projects that start with a good idea, but do not quite know how to make it real. Others have a technical team capable of building almost anything, but need to define what is worth building. And there are those with a good product who cannot communicate why someone should choose it.</p><p>In all those cases, design can offer much more than a visual solution.</p><p>Over time, my work as a designer has led me to get involved in different stages of a project: from understanding the business and defining a brand strategy, to organizing the development of a digital product and designing the experience of the people who use it.</p><p>That combination lets me approach projects from a broader perspective, connecting ideas with the people who need them and with the teams that must make them real.</p><h2>Understand the problem before looking for the solution</h2><p>What a business needs is not always a new website, an app or a visual identity. Sometimes what is missing is clarity: understanding which problem needs to be solved, what the priorities are and which path makes the most sense to follow.</p><p>That is why, before thinking about solutions, I care about understanding the context. What the business is looking for, what its users need and what conditions exist to bring an idea into practice.</p><p>This view is also part of my work as a Product Owner. In that role, I connect the needs of the business with the technical team, turning ideas and goals into concrete tasks that can be developed, tested and improved.</p><p>I work with user stories, a roadmap and a prioritized backlog, take part in Scrum ceremonies and review deliveries to check that they meet what was defined. I also help order expectations and keep the team focused on what really matters.</p><p>In short, I help everyone understand what we are building, why we are building it and what the next step is.</p><h2>Give meaning to what a brand wants to build</h2><p>Once we understand the business and its proposal, another question appears: how do we help people understand its value?</p><p>A brand is not just a logo or a color system. It is the way a company or a product presents itself, sets itself apart and builds a relationship with people. When that identity is not well defined, communicating a good idea can become much harder.</p><p>Through brand strategy, I work on finding that meaning and turning it into a clear direction. I define the purpose, the positioning and the elements that express what makes a product, or the company behind it, different.</p><p>This can include a Brand Compass to guide brand decisions, naming, visual identity, voice and tone of communication, and even the design of its website.</p><p>The goal is for every decision to have a reason behind it, and for the brand not only to look good but also to help communicate better what it offers.</p><h2>Turn ideas into experiences we can test</h2><p>With digital products, there is an important gap between having an idea and knowing whether it really works for the people who will use it.</p><p>UX/UI design helps close that gap. It lets me explore how a product should work, which steps a person needs to follow, and how we can make the experience more intuitive, useful and consistent with the business goals.</p><p>I work on user flows, navigation structure, interface design and the prototypes that let us explore a solution before fully developing it.</p><p>I also use artificial intelligence tools to take some of these ideas to navigable or functional prototypes more quickly. That way we can see the proposal more clearly, test alternatives and spot opportunities for improvement before committing more resources to development.</p><p>Once we have a clear direction, I prepare the design and the handover to the technical team so the solution can be implemented in production.</p><h2>A view that connects the different parts of a project</h2><p>My work is not limited to a single stage or a single discipline. I care about how the business, the brand, the user experience and the technology relate, because the decisions we make in one area end up influencing the others.</p><p>That perspective lets me collaborate with different profiles, talk with both business people and technical teams, and help design decisions respond to concrete needs.</p><p>It is not about doing everything, but about understanding what each project needs and contributing from where I can add the most value: giving direction to ideas, turning them into solutions and helping them reach the people they were made for.</p><p>In the end, designing also means connecting the pieces so things work better.</p>',
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

_noticia('ley-21719-prepara-tu-web', 'Law 21.719 prepares your website for fines',
         'Law 21.719 is expected to take effect at the end of 2026. Review forms, cookies and privacy notices on your website before that date.',
         '<p>Law 21.719 modernizes Law 19.628, the current rule on personal data in Chile. It changes how companies collect, use and protect people’s information, and that includes your website every time it receives data through a form, a cookie or an analytics tool.</p>'
         '<h2>What is planned</h2><p>The law was published in December 2024, and its entry into force is planned for 1 December 2026. There is also a bill that proposes postponing it. Before planning changes, check the current status at the National Congress Library (bcn.cl).</p>'
         '<h2>What to review on your website</h2>' + _lista([
             '<strong>Forms:</strong> ask only for the data you need and explain what you use it for.',
             '<strong>Cookies and analytics:</strong> say which tools you use and ask for consent when needed.',
             '<strong>Privacy notice:</strong> it should be clear, easy to find and explain how to exercise your rights.',
             '<strong>People’s rights:</strong> access, rectification, erasure, objection and portability, with a channel to respond.',
             '<strong>Providers:</strong> check which external services receive your users’ data.']) +
         '<h2>Where to start</h2><p>I inventory the data your site collects, review the legal texts and adjust the experience so privacy is part of the design, not a patch at the end. If you want to see how I approached the law in an own product, check <a href="{p}proyectos/auditorweb.html">AuditorWeb 21.719</a>.</p>'
         '<p class="muted">This note is general guidance and does not replace legal advice.</p>',
         'Regulation', _EN)
