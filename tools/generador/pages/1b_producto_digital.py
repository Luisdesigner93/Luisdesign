# Landing Producto digital (producto-digital.html) y su versión en inglés (en/digital-product.html).
# Textos de tools/narrativa/03-landing-producto-digital.md. La traducción al inglés está pendiente de revisión de Luis.
# Los textos usan {p} para las rutas (lo completa page() según la carpeta de cada versión).

ES = dict(
    path='producto-digital.html',
    title='Luis Vicencio · Product Owner y estrategia de marca para productos digitales',
    desc='Product Owner externo con Scrum y estrategia de marca para empresas de software, startups y áreas de innovación. Me sumo a tu equipo por un período o por proyecto.',
    other=('en/digital-product.html', 'English version', 'en'),
    eyebrow='Luis Vicencio · Producto digital',
    h1='Marca y producto, <strong>con un mismo norte</strong>.',
    lead='Product Owner y estratega de marca para empresas de software, startups y áreas de innovación. Me sumo a tu equipo para que lo que construyes tenga un norte claro, prioridades ordenadas y entregas que cumplen lo esperado.',
    btn_main='Agendemos una conversación', btn_cases='Ver casos',
    proof_label='Han confiado en mí',
    problem_eyebrow='¿Te suena?',
    problem_h2='Un buen equipo técnico no basta <strong>si nadie ordena el camino</strong>.',
    problems=['El cliente pide una cosa y el equipo entrega otra.',
              'Los requerimientos llegan difusos y el desarrollo se alarga.',
              'Nadie tiene claro qué construir primero ni por qué.',
              'Hay muchas ideas con IA, pero ninguna llega a producción.',
              'El producto funciona, pero no tiene identidad y nadie lo entiende a la primera.'],
    problem_close='Mi trabajo es ser el puente entre tu negocio, tu cliente y tu equipo técnico.',
    roles_eyebrow='Servicios',
    roles_h2='Tres roles que normalmente <strong>contratas por separado</strong>.',
    includes='Incluye', cases_label='Casos',
    roles=[
        ('Product Owner',
         'Represento a tu negocio frente al equipo técnico. Traduzco lo que el cliente necesita en historias de usuario claras, ordeno el backlog y reviso que cada entrega cumpla lo esperado.',
         'comprensión del negocio, historias de usuario, roadmap y backlog priorizado, ceremonias Scrum, QA de cada historia, gestión de expectativas e informes de avance. También coordino células especializadas dentro del equipo de desarrollo de tu cliente.',
         [('Legisnova', 'bytequest'), ('Auditor de llamadas', 'bytequest'), ('Asistente virtual multiagente', 'bytequest')]),
        ('Estrategia de marca para productos',
         'Un producto sin identidad se explica peor y se vende peor. Defino el propósito, la voz y la identidad del producto o de la empresa que lo construye, para que el equipo y los usuarios tengan el mismo norte.',
         'Brand Compass, naming, identidad visual, voz y sitio web.',
         [('marca de Bytequest', 'bytequest'), ('Yomecontrolo', 'yomecontrolo')]),
        ('UX/UI y prototipos con IA',
         'Diseño la experiencia y la llevo a un prototipo funcional con desarrollo asistido por IA, para validar antes de invertir en desarrollo. Después lo traspaso a tu equipo para producción.',
         'flujos, prototipos navegables o funcionales, diseño de interfaces y traspaso al equipo de desarrollo.',
         [('AuditorWeb', 'auditorweb'), ('sitio y plataforma de Legisnova', 'bytequest'), ('web app de Yomecontrolo', 'yomecontrolo')]),
    ],
    fit_yes_label='Es para ti si', fit_yes='tienes un equipo de desarrollo (propio o externo) y necesitas a alguien que ordene, priorice y le dé identidad al producto.',
    fit_no_label='No es para ti si', fit_no='buscas un programador que construya la versión final de tu producto. Yo defino, diseño, prototipo y dirijo; la programación la hace tu equipo de desarrollo o uno que armemos juntos.',
    method_eyebrow='Método', method_h2='Scrum, con los pies <strong>en el negocio</strong>.',
    method_lead='Desde el inicio acordamos prioridades, responsables y entregables, y reviso las señales de alerta en cada sprint para corregir el rumbo a tiempo.',
    step_label='Paso', steps_label='Pasos del método',
    steps=[('Comprender el negocio', 'Me reúno con tu equipo y con tu cliente para entender quiénes son los usuarios, qué necesitan y qué se espera del producto.'),
           ('Definir', 'Escribo las historias de usuario, armo el roadmap y priorizamos juntos qué se construye primero.'),
           ('Construir por sprints', 'El equipo entrega avances en ciclos cortos; yo coordino, despejo bloqueos y mantengo informadas a todas las partes.'),
           ('Revisar', 'Hago QA de cada historia de usuario: no se da por terminada hasta que cumple lo esperado.'),
           ('Ajustar', 'En cada revisión vemos lo construido, aprendemos y corregimos el rumbo.')],
    learned_label='Lo que me llevé',
    learned='Aprendí a reconocer las alertas tempranas de un proyecto: prioridades difusas, decisiones sin responsable claro y expectativas sin acordar. Hoy las reviso desde el primer día.',
    cases_eyebrow='Proyectos', cases_h2='Productos con IA para <strong>organizaciones exigentes</strong>.',
    featured_tag='Caso destacado',
    featured_text='Creé la marca de la empresa y lideré el producto de soluciones con IA como Legisnova, la agenda legislativa del Congreso en un solo lugar; un auditor que analiza llamadas de emergencia según protocolo; y un asistente virtual multiagente para una institución del sistema de justicia, entre otras.',
    see_case='Ver caso completo', see_project='Ver proyecto', pending_img='Imagen pendiente',
    cards=[('Legisnova', 'bytequest', 'Propuse los planes Parlamentario e Independiente, escribí las historias de usuario y aseguré con QA cada entrega.', ['Product Owner', 'QA', 'Prototipo con IA']),
           ('Yomecontrolo', 'yomecontrolo', 'Estrategia, experiencia y diseño del MVP de una startup de salud preventiva. La marca sigue en uso.', ['Marca', 'UX/UI', 'Producto']),
           ('AuditorWeb 21.719', 'auditorweb', 'Producto propio: la Ley 21.719 convertida en un informe automático y accionable.', ['Producto', 'UX/UI', 'IA'])],
    all_projects='Ver todos los proyectos',
    modes_eyebrow='Modalidad', modes_h2='Cómo trabajamos <strong>juntos</strong>.',
    modes=[('Por período', 'me integro a tu equipo durante un tiempo definido como Product Owner o líder de marca y producto.'),
           ('Por proyecto', 'tomo un producto o una etapa (discovery, MVP, lanzamiento) con alcance y entregables cerrados.'),
           # EDITAR: sumar "con reuniones presenciales en [ciudad] cuando el proyecto lo pide" cuando Luis defina la ciudad
           ('Remoto', 'en español o inglés.')],
    about_eyebrow='Sobre mí', about_h2='Diseñador con <strong>mirada de producto</strong>.',
    about=['Soy Luis Vicencio, diseñador de la Universidad de Valparaíso, con estudios de Product Design for Innovation en el Politecnico di Milano y formación en Product Owner y Scrum. Empecé diseñando marcas y, proyecto a proyecto, sumé la estrategia y el liderazgo de producto.',
           'En Yomecontrolo aprendí que una buena estrategia de marca necesita herramientas de producto para llegar a producción. Hoy acompaño las dos etapas: le doy un norte al producto y lo llevo paso a paso, entregable a entregable, hasta que cada entrega cumple lo esperado.'],
    portrait_alt='Retrato de Luis Vicencio',
    brand_link='¿Buscas una marca para tu pyme?', home='./', about_link='Ver mi trayectoria',
    faq_h2='Preguntas <strong>frecuentes</strong>.',
    faq=[('¿Qué hace un Product Owner externo?', 'Representa a tu negocio frente al equipo técnico: define qué se construye, en qué orden y revisa que cada entrega cumpla lo esperado, sin que tengas que contratar a alguien a tiempo completo.'),
         ('¿Trabajas con mi equipo de desarrollo?', 'Sí. Me integro a tu equipo o al de tu cliente, como lo hice coordinando una célula de IA dentro del equipo de un cliente de Bytequest.'),
         ('¿Programas?', 'Diseño y construyo prototipos funcionales con desarrollo asistido por IA para validar ideas rápido. El desarrollo para producción lo hace tu equipo.'),
         ('¿Tienes experiencia con IA?', 'Sí: lideré productos con asistentes multiagente, análisis automático de llamadas, resúmenes con IA y automatizaciones. Además trabajo con desarrollo guiado por especificaciones (spec-driven): escribo especificaciones claras para que tu equipo y las herramientas de IA construyan exactamente lo acordado.'),
         ('¿Firmas acuerdos de confidencialidad?', 'Sí. Por eso algunos casos se muestran sin el nombre del cliente.')],
    cta_title='Conversemos sobre <strong>tu producto</strong>.',
    cta_lead='Cuéntame en qué etapa está tu producto y qué necesita tu equipo. Te respondo con una propuesta de modalidad, alcance y plazos.',
    email_label='Escríbeme a contacto@luisdesign.cl',
    subject='Producto digital: [empresa] · [etapa del producto]',
    new_tab='(se abre en una pestaña nueva)',
)

# EDITAR: traducción propuesta por Claude; Luis debe revisarla antes de publicar
EN = dict(
    path='en/digital-product.html',
    title='Luis Vicencio · Fractional Product Owner & Brand Strategist for Digital Products',
    desc='Fractional Product Owner with Scrum and brand strategist for software companies, startups and innovation teams. I join your team for a set period or per project.',
    other=('producto-digital.html', 'Versión en español', 'es'),
    eyebrow='Luis Vicencio · Digital product',
    h1='Brand and product, <strong>pointing the same way</strong>.',
    lead='Product Owner and brand strategist for software companies, startups and innovation teams. I join your team so that what you build has a clear direction, well-ordered priorities and deliveries that meet expectations.',
    btn_main='Let’s schedule a call', btn_cases='See case studies',
    proof_label='Trusted by',
    problem_eyebrow='Sound familiar?',
    problem_h2='A good tech team isn’t enough <strong>if no one sets the path</strong>.',
    problems=['The client asks for one thing and the team delivers another.',
              'Requirements arrive vague and development drags on.',
              'No one is sure what to build first, or why.',
              'There are plenty of AI ideas, but none reach production.',
              'The product works, but it has no identity and no one gets it at first sight.'],
    problem_close='My job is to be the bridge between your business, your client and your tech team.',
    roles_eyebrow='Services',
    roles_h2='Three roles you would normally <strong>hire separately</strong>.',
    includes='Includes', cases_label='Cases',
    roles=[
        ('Product Owner',
         'I represent your business in front of the tech team. I turn what the client needs into clear user stories, order the backlog and check that every delivery meets expectations.',
         'business understanding, user stories, roadmap and prioritized backlog, Scrum ceremonies, QA of every story, expectation management and progress reports. I also coordinate specialized cells inside your client’s development team.',
         [('Legisnova', 'bytequest'), ('Call auditor', 'bytequest'), ('Multi-agent virtual assistant', 'bytequest')]),
        ('Brand strategy for products',
         'A product without an identity is harder to explain and harder to sell. I define the purpose, voice and identity of the product or of the company behind it, so the team and the users share the same direction.',
         'Brand Compass, naming, visual identity, voice and website.',
         [('Bytequest brand', 'bytequest'), ('Yomecontrolo', 'yomecontrolo')]),
        ('UX/UI and AI-assisted prototypes',
         'I design the experience and take it to a working prototype with AI-assisted development, to validate before investing in development. Then I hand it over to your team for production.',
         'flows, clickable or working prototypes, interface design and handover to the development team.',
         [('AuditorWeb', 'auditorweb'), ('Legisnova website and platform', 'bytequest'), ('Yomecontrolo web app', 'yomecontrolo')]),
    ],
    fit_yes_label='It’s for you if', fit_yes='you have a development team (in-house or external) and need someone to organize, prioritize and give the product an identity.',
    fit_no_label='It’s not for you if', fit_no='you are looking for a programmer to build the final version of your product. I define, design, prototype and lead; the coding is done by your development team or one we put together.',
    method_eyebrow='Method', method_h2='Scrum, with both feet <strong>in the business</strong>.',
    method_lead='From day one we agree on priorities, owners and deliverables, and I check the warning signs every sprint to correct course in time.',
    step_label='Step', steps_label='Method steps',
    steps=[('Understand the business', 'I meet with your team and your client to understand who the users are, what they need and what is expected from the product.'),
           ('Define', 'I write the user stories, build the roadmap and we prioritize together what gets built first.'),
           ('Build in sprints', 'The team delivers progress in short cycles; I coordinate, clear blockers and keep everyone informed.'),
           ('Review', 'I QA every user story: it isn’t done until it meets expectations.'),
           ('Adjust', 'At every review we look at what was built, learn and correct course.')],
    learned_label='What I took away',
    learned='I learned to spot a project’s early warning signs: fuzzy priorities, decisions without a clear owner and expectations no one agreed on. Today I check for them from day one.',
    cases_eyebrow='Projects', cases_h2='AI products for <strong>demanding organizations</strong>.',
    featured_tag='Featured case',
    featured_text='I created the company’s brand and led AI products such as Legisnova, Chile’s legislative agenda in one place; an auditor that analyzes emergency calls against protocol; and a multi-agent virtual assistant for an institution of the justice system, among others.',
    see_case='See full case (Spanish)', see_project='See project', pending_img='Image pending',
    cards=[('Legisnova', 'bytequest', 'I proposed the Parliamentary and Independent plans, wrote the user stories and secured every delivery with QA.', ['Product Owner', 'QA', 'AI prototype']),
           ('Yomecontrolo', 'yomecontrolo', 'Strategy, experience and MVP design for a preventive health startup. The brand is still in use.', ['Brand', 'UX/UI', 'Product']),
           ('AuditorWeb 21.719', 'auditorweb', 'My own product: Chile’s Law 21.719 turned into an automatic, actionable report.', ['Product', 'UX/UI', 'AI'])],
    all_projects='See all projects',
    modes_eyebrow='Engagement', modes_h2='How we <strong>work together</strong>.',
    modes=[('For a set period', 'I join your team for a defined time as Product Owner or brand and product lead.'),
           ('Per project', 'I take on a product or a stage (discovery, MVP, launch) with a closed scope and deliverables.'),
           ('Remote', 'in Spanish or English.')],
    about_eyebrow='About', about_h2='A designer with <strong>a product mindset</strong>.',
    about=['I’m Luis Vicencio, a designer from Universidad de Valparaíso, with studies in Product Design for Innovation at Politecnico di Milano and training as a Product Owner and in Scrum. I started out designing brands and, project by project, added strategy and product leadership.',
           'At Yomecontrolo I learned that a good brand strategy needs product tools to reach production. Today I support both stages: I give the product a direction and take it step by step, deliverable by deliverable, until every delivery meets expectations.'],
    portrait_alt='Portrait of Luis Vicencio',
    brand_link='Looking for a brand for your small business? (Spanish)', home='../', about_link='See my background (Spanish)',
    faq_h2='Frequently asked <strong>questions</strong>.',
    faq=[('What does a fractional Product Owner do?', 'They represent your business in front of the tech team: they define what gets built and in what order, and check that every delivery meets expectations, without you having to hire someone full time.'),
         ('Do you work with my development team?', 'Yes. I join your team or your client’s, as I did coordinating an AI cell inside the team of a Bytequest client.'),
         ('Do you code?', 'I design and build working prototypes with AI-assisted development to validate ideas quickly. Production development is done by your team.'),
         ('Do you have experience with AI?', 'Yes: I led products with multi-agent assistants, automatic call analysis, AI summaries and automations. I also work with spec-driven development: I write clear specifications so your team and AI tools build exactly what was agreed.'),
         ('Do you sign confidentiality agreements?', 'Yes. That is why some cases are shown without the client’s name.')],
    cta_title='Let’s talk about <strong>your product</strong>.',
    cta_lead='Tell me what stage your product is at and what your team needs. I’ll reply with a proposal for engagement, scope and timeline.',
    email_label='Email me at contacto@luisdesign.cl',
    subject='Digital product: [company] · [product stage]',
    new_tab='(opens in a new tab)',
)

_icon = lambda name: f'<svg class="icon" aria-hidden="true"><use href="{{p}}img/icons.svg#i-{name}"/></svg>'


def _case_link(slug):
    return '{p}proyectos/' + slug + '.html'


def _producto_body(t, mailto):
    arrow = _icon('arrow')
    other_path, other_label, other_lang = t['other']
    role_cards = ''.join(f'''
          <article class="card pd-role">
            <h3 class="card-title">{name}</h3>
            <p>{text}</p>
            <p class="pd-small"><strong>{t['includes']}:</strong> {inc}</p>
            <p class="svc-casos"><span>{t['cases_label']}</span>{' · '.join(f'<a href="{_case_link(s)}">{c}</a>' for c, s in cases)}</p>
          </article>''' for name, text, inc, cases in t['roles'])
    case_cards = ''.join(f'''
          <li class="card pd-case">
            <ul class="tag-list" aria-label="{t['cases_label']}">{''.join(f'<li class="tag">{g}</li>' for g in tags)}</ul>
            <h3 class="card-title">{name}</h3>
            <p>{line}</p>
            <a class="link-arrow" href="{_case_link(slug)}">{t['see_project']}<span class="sr-only">: {name}</span> {arrow}</a>
          </li>''' for name, slug, line, tags in t['cards'])
    return f'''    <!-- HERO -->
    <section class="v2-hero-shell" aria-labelledby="v2-title">
      <div class="v2-hero">
        <img class="v2-hero-bg" src="{{p}}img/marca/hero-fondo.jpg" width="2000" height="1333" alt="" decoding="async" fetchpriority="high">
        <div class="v2-hero-top">
          <span class="v2-eyebrow"><i aria-hidden="true"></i>{t['eyebrow']}</span>
          <h1 class="v2-hero-title" id="v2-title">{t['h1']}</h1>
          <p class="v2-hero-lead">{t['lead']}</p>
          <a class="pd-lang" href="{{p}}{other_path}" hreflang="{other_lang}" lang="{other_lang}">{other_label}</a>
        </div>
        <div class="v2-hero-bottom">
          <ul class="v2-hero-meta" aria-label="{t['proof_label']}">
            <li>+ Bytequest</li>
            <li>+ Legisnova</li>
            <li>+ Yomecontrolo</li>
            <li>+ AuditorWeb</li>
          </ul>
          <div class="v2-hero-cta">
            <div class="btn-row">
              <a class="btn btn-primary v2-btn-light" href="{mailto}">{t['btn_main']} {arrow}</a>
              <a class="btn v2-btn-ghost" href="#casos">{t['btn_cases']}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- EL PROBLEMA -->
    <section class="panel section" id="problema" aria-labelledby="problema-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">{t['problem_eyebrow']}</span>
          <h2 class="heading" id="problema-title">{t['problem_h2']}</h2>
        </div>
        <ul class="momentos-grid" role="list">{''.join(f"""
          <li class="card momento"><span class="momento-num">{i:02d}</span><p class="pd-signal">{x}</p></li>""" for i, x in enumerate(t['problems'], 1))}
        </ul>
        <p class="momentos-cierre">{t['problem_close']}</p>
      </div>
    </section>

    <!-- QUÉ HAGO -->
    <section class="panel panel-plain section" id="servicios" aria-labelledby="servicios-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">{t['roles_eyebrow']}</span>
          <h2 class="heading" id="servicios-title">{t['roles_h2']}</h2>
        </div>
        <div class="pd-roles">{role_cards}
        </div>
        <dl class="card svc-fit pd-fit"><div><dt>{t['fit_yes_label']}</dt><dd>{t['fit_yes']}</dd></div><div><dt>{t['fit_no_label']}</dt><dd>{t['fit_no']}</dd></div></dl>
      </div>
    </section>

    <!-- CÓMO TRABAJO -->
    <section class="panel section proceso" id="proceso" aria-labelledby="proceso-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">{t['method_eyebrow']}</span>
          <h2 class="heading" id="proceso-title">{t['method_h2']}</h2>
          <p class="lead">{t['method_lead']}</p>
        </div>
        <div class="steps-scroller" role="region" aria-label="{t['steps_label']}" tabindex="0">
          <ol class="steps">{''.join(f"""
            <li class="card step"><p class="step-eyebrow">{t['step_label']} {i:02d}</p><h3 class="title">{n}</h3><p>{d}</p></li>""" for i, (n, d) in enumerate(t['steps'], 1))}
          </ol>
        </div>
        <figure class="pd-learned">
          <figcaption>{t['learned_label']}</figcaption>
          <blockquote><p>{t['learned']}</p></blockquote>
        </figure>
      </div>
    </section>

    <!-- CASOS -->
    <section class="section more" id="casos" aria-labelledby="casos-title">
      <div class="container more-head">
        <span class="tag tag-eyebrow">{t['cases_eyebrow']}</span>
        <h2 class="heading v2-big" id="casos-title">{t['cases_h2']}</h2>
      </div>
      <div class="container">
        <article class="feat-case">
          <!-- EDITAR: imagen de la marca de Bytequest o pantallas de Legisnova (sin datos sensibles) -->
          <div class="media-ph pd-feat-ph" role="img" aria-label="{t['pending_img']}">{_icon('image')}{t['pending_img']}</div>
          <div class="feat-case-text">
            <span class="tag">{t['featured_tag']}</span>
            <h3 class="card-title">Bytequest</h3>
            <p>{t['featured_text']}</p>
            <a class="link-arrow" href="{_case_link('bytequest')}">{t['see_case']}<span class="sr-only">: Bytequest</span> {arrow}</a>
          </div>
        </article>
        <ul class="pd-cases" role="list">{case_cards}
        </ul>
        <!-- Testimonio pendiente: una frase de la dirección de Bytequest (no se publica hasta tenerla) -->
        <div class="more-foot-cta">
          <a class="btn btn-primary" href="{{p}}proyectos.html">{t['all_projects']} {arrow}</a>
        </div>
      </div>
    </section>

    <!-- MODALIDAD -->
    <section class="panel panel-plain section" id="modalidad" aria-labelledby="modalidad-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">{t['modes_eyebrow']}</span>
          <h2 class="heading" id="modalidad-title">{t['modes_h2']}</h2>
        </div>
        <div class="benefits pd-modes">{''.join(f"""
          <div><strong>{n}</strong><span>{d}</span></div>""" for n, d in t['modes'])}
        </div>
      </div>
    </section>

    <!-- SOBRE MÍ -->
    <section class="panel section about" id="sobre-mi" aria-labelledby="sobre-title">
      <div class="container">
        <div class="two-col about-grid">
          <figure class="portrait">
            <img src="{{p}}img/marca/luis-vicencio-retrato.png" width="750" height="900" alt="{t['portrait_alt']}" loading="lazy" decoding="async">
          </figure>
          <div class="about-text">
            <span class="tag tag-eyebrow">{t['about_eyebrow']}</span>
            <h2 class="heading" id="sobre-title">{t['about_h2']}</h2>
            <p>{t['about'][0]}</p>
            <p>{t['about'][1]}</p>
            <!-- EDITAR: sumar el botón "Descargar CV" cuando Luis entregue el PDF -->
            <div class="about-links">
              <a class="link-arrow" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank">LinkedIn<span class="sr-only"> {t['new_tab']}</span> {arrow}</a>
              <a class="link-arrow" href="{{p}}sobre-mi.html">{t['about_link']} {arrow}</a>
              <a class="link-arrow" href="{t['home']}">{t['brand_link']} {arrow}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- PREGUNTAS FRECUENTES -->
    <section class="panel panel-plain section" id="preguntas" aria-labelledby="faq-title">
      <div class="container">
        <div class="narrow">
          <div class="section-head center">
            <h2 class="heading" id="faq-title">{t['faq_h2']}</h2>
          </div>
          <div class="faq">{''.join(f"""
            <details class="card">
              <summary>{q}</summary>
              <p>{a}</p>
            </details>""" for q, a in t['faq'])}
          </div>
        </div>
      </div>
    </section>
'''


_alternates = {'es-CL': ES['path'], 'en': EN['path'], 'x-default': ES['path']}
for _t, _lang in ((ES, 'es'), (EN, 'en')):
    _mailto = f'mailto:{EMAIL}?subject=' + quote(_t['subject'])
    page(_t['path'], _t['title'], _t['desc'], body=_producto_body(_t, _mailto),
         current='producto', lang=_lang, alternates=_alternates, html_class='home motion v2', extra_css='css/home-v2.css',
         cta_title=_t['cta_title'], cta_lead=_t['cta_lead'],
         email_subject=_t['subject'], email_first=True, email_label=_t['email_label'],
         jsonld=[service_ld(name, text, _t['path'] + '#servicios', _lang) for name, text, _inc, _cases in _t['roles']] + [faq_ld(_t['faq'], _lang)])
