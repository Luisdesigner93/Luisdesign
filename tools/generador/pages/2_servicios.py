def service(num, sid, title_html, lead, text, includes, deliverables, plain):
    items = ''.join(f'\n            <li><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-check"/></svg>{i}</li>' for i in includes)
    tags = ''.join(f'<li class="tag">{d}</li>' for d in deliverables)
    cls = 'panel panel-plain section service' if plain else 'panel section service'
    return f'''
    <section class="{cls}" id="{sid}" aria-labelledby="{sid}-title">
      <div class="container two-col">
        <div class="section-head">
          <span class="numtag">{num}</span>
          <h2 class="heading" id="{sid}-title">{title_html}</h2>
          <p class="lead">{lead}</p>
          {text}
        </div>
        <div class="service-detail">
          <h3>Qué incluye</h3>
          <ul class="card checklist">{items}
          </ul>
          <div class="card deliverables">
            <h3>Entregables</h3>
            <ul class="tag-list">{tags}</ul>
          </div>
        </div>
      </div>
    </section>
'''


body = '''    <section class="hero-shell" aria-labelledby="page-title">
      <div class="shell-body frame-grid page-hero">
        <div class="container">
          <ol class="breadcrumb" aria-label="Ruta"><li><a href="./">Inicio</a></li><li aria-current="page">Servicios</li></ol>
          <span class="tag tag-eyebrow">Servicios</span>
          <h1 class="display" id="page-title">Marca, producto y web <strong>con un mismo criterio</strong>.</h1>
          <p class="lead">Puedes contratar un servicio puntual o el proyecto completo. En ambos casos trabajas directamente conmigo, desde la estrategia hasta la entrega.</p>
          <nav aria-label="Servicios en esta página">
            <ul class="service-index">
              <li><a href="#branding"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-target"/></svg></span>Branding estratégico</a></li>
              <li><a href="#ux-ui"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-pen"/></svg></span>UX/UI y diseño de producto</a></li>
              <li><a href="#product-owner"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-kanban"/></svg></span>Product Owner</a></li>
              <li><a href="#web"><span class="icon-key" aria-hidden="true"><svg class="icon"><use href="img/icons.svg#i-shield"/></svg></span>Sitios web y ecommerce</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </section>
'''

body += service('01', 'branding', 'Branding <strong>estratégico</strong>',
    'Cuando todos dicen lo mismo, el cliente elige lo más barato. Tu marca es la razón para elegirte a ti.',
    '<p>Una marca sólida trabaja en tres niveles: la <strong>estrategia</strong> define quién eres, para quién y por qué deberían elegirte; la <strong>identidad</strong> hace que eso se vea y se reconozca a la primera; y la <strong>marca</strong> es lo que tus clientes terminan pensando y sintiendo de ti.</p>'
    '<p class="benefit-title">Lo que ganas al diferenciarte</p>'
    '<ul class="benefit-list"><li><strong>Ser elegido</strong>, no solo encontrado, entre opciones parecidas.</li>'
    '<li><strong>Cobrar lo que vales</strong>: el valor percibido justifica tu precio.</li>'
    '<li><strong>Atraer a los clientes correctos</strong>, los que valoran lo que haces.</li>'
    '<li><strong>Crecer con coherencia</strong>, sin partir de cero en cada proyecto.</li></ul>'
    '<p>Para lograrlo combino research y discovery con metodología de branding: detectamos juntos las brechas de posicionamiento que importan y las convierto en una identidad con argumentos.</p>',
    ['Research de mercado, competencia y público objetivo',
     'Diagnóstico de brechas de posicionamiento',
     'Plataforma de marca: propósito, propuesta de valor y tono',
     'Identidad visual: logotipo, color, tipografía y aplicaciones',
     'Manual de marca para tu equipo y proveedores'],
    ['Diagnóstico', 'Estrategia de marca', 'Identidad visual', 'Manual de marca', 'Packaging de productos', 'Wayfinding'], True)

body += service('02', 'ux-ui', 'UX/UI y <strong>diseño de producto</strong>',
    'Si tu producto es difícil de usar, tus clientes lo abandonan. Diseño experiencias que se entienden a la primera.',
    '<p>Un producto digital que la gente no entiende no se usa, no se compra o genera costos. El diseño UX/UI resuelve eso antes de que cueste caro.</p>'
    '<p class="benefit-title">Lo que ganas con un buen diseño</p>'
    '<ul class="benefit-list"><li><strong>Más conversiones</strong>: tus usuarios logran lo que vinieron a hacer, sin abandonar.</li><li><strong>Menos riesgo</strong>: evitas desarrollar funciones que nadie va a usar.</li><li><strong>Menos soporte</strong>: una interfaz clara reduce consultas, errores y reclamos.</li><li><strong>Más confianza</strong>: un producto cuidado transmite la calidad de tu negocio.</li></ul>'
    '<p>Para lograrlo partimos juntos por las necesidades reales de tus usuarios, validamos con prototipos antes de construir y diseño interfaces coherentes con tu marca.</p>',
    ['Discovery con usuarios y stakeholders',
     'Arquitectura de información y flujos de usuario',
     'Wireframes y prototipos navegables',
     'Diseño de interfaces para escritorio y móvil',
     'Sistema de diseño con componentes reutilizables'],
    ['Flujos', 'Prototipo', 'Diseño de interfaces', 'Sistema de diseño'], False)

body += service('03', 'product-owner', 'Product Owner <strong>para tu proyecto</strong>',
    'Sin prioridades claras, el desarrollo se alarga y se desvía. Ordeno el camino para que construyamos lo que realmente importa.',
    '<p>Un Product Owner representa a tu negocio frente al equipo técnico. Hablo el idioma de tu empresa y el de los desarrolladores, para que tu inversión se convierta en un producto que funciona.</p>'
    '<p class="benefit-title">Lo que ganas con un Product Owner</p>'
    '<ul class="benefit-list"><li><strong>Visibilidad</strong>: sabes qué se hizo, qué falta y cuándo estará listo.</li><li><strong>Prioridades claras</strong>: se construye primero lo que más aporta a tu negocio.</li><li><strong>Presupuesto bien invertido</strong>: sin gastar en funciones que nadie usará.</li><li><strong>Calidad</strong>: cada entrega se revisa antes de llegar a tus clientes.</li></ul>'
    '<p>Para lograrlo definimos juntos el roadmap y las prioridades, y me encargo del día a día con el equipo: backlog, Scrum, control de calidad e informes de avance. Adapto la metodología al equipo para mejorar su rendimiento desde el primer sprint.</p>',
    ['Discovery de necesidades de negocio y de usuario',
     'Definición del roadmap y gestión del backlog',
     'Ceremonias Scrum con el equipo técnico',
     'QA de los entregables de desarrollo',
     'Informes de avance para cliente y stakeholders'],
    ['Roadmap', 'Backlog priorizado', 'Informes de avance', 'Registro de QA'], True)

body += service('04', 'web', 'Sitios web <strong>y ecommerce</strong>',
    'Un buen sitio guía a la persona hacia la acción: comprar, cotizar, agendar o escribirte. Diseñemos el tuyo.',
    '<p>Hoy tus clientes te buscan, comparan y deciden en internet antes de hablar contigo. Tu sitio es tu vitrina abierta todo el día: el lugar donde te encuentran, te evalúan y deciden comprarte.</p>'
    '<p class="benefit-title">Lo que ganas con un sitio propio</p>'
    '<ul class="benefit-list"><li><strong>Ser encontrado</strong> y tomado en serio cuando te buscan en Google.</li><li><strong>Vender las 24 horas</strong>, sin depender de horarios ni de responder mensaje por mensaje.</li><li><strong>Un espacio propio</strong>: en redes sociales decide el algoritmo; en tu sitio decides tú.</li><li><strong>Cumplir la Ley 21.719</strong>: cuidar los datos de tus visitantes genera confianza y evita multas.</li></ul>'
    '<p>Para lograrlo definimos juntos qué debe lograr tu sitio, diseño la experiencia y dirijo el desarrollo con el equipo técnico. Incluyo un diagnóstico de cumplimiento con <a href="proyectos/auditorweb.html">AuditorWeb</a>: no reemplaza una asesoría legal, pero resuelve lo que es visible desde la web.</p>',
    ['Estructura, contenidos y diseño del sitio o la tienda',
     'Coordinación del desarrollo y control de calidad',
     'Diagnóstico de cumplimiento de la Ley 21.719 con AuditorWeb',
     'Política de privacidad, cookies y consentimiento visibles y completos',
     'Revisión de seguridad: HTTPS, cabeceras y servicios de terceros'],
    ['Sitio publicado', 'Informe de cumplimiento', 'Plan de adecuación'], False)

body += '''
    <!-- PREGUNTAS -->
    <section class="panel panel-plain section" id="preguntas" aria-labelledby="faq-title">
      <div class="container">
        <div class="narrow">
          <div class="section-head center">
            <span class="tag tag-eyebrow">Preguntas frecuentes</span>
            <h2 class="heading" id="faq-title">Antes de <strong>empezar</strong>.</h2>
          </div>
          <div class="faq">
            <details class="card">
              <summary>¿Cuánto cuesta un proyecto?</summary>
              <p>Depende del alcance: si se trata de una marca nueva o de un rediseño, de la cantidad de pantallas o páginas y de las integraciones necesarias. Después de una primera conversación te envío una propuesta con alcance, plazos y valor cerrado.</p>
            </details>
            <details class="card">
              <summary>¿Cuánto tiempo toma?</summary>
              <p>Un proyecto de branding o un sitio corporativo suele tomar entre cuatro y ocho semanas, según la disponibilidad de contenidos y las rondas de revisión. Los proyectos de producto se organizan en sprints con entregas frecuentes.</p>
            </details>
            <details class="card">
              <summary>¿Puedes sumarte a mi equipo como Product Owner?</summary>
              <p>Sí. Puedo integrarme a un proyecto de software por un período definido, coordinando al equipo técnico con tu negocio y haciéndome cargo del backlog, el QA y los informes de avance.</p>
            </details>
            <details class="card">
              <summary>¿Quién desarrolla los sitios y productos?</summary>
              <p>Yo me encargo de la estrategia, el diseño y la dirección del proyecto, y el desarrollo lo realiza un equipo técnico que coordino. Si ya tienes un equipo, trabajo directamente con él.</p>
            </details>
            <details class="card">
              <summary>¿La adecuación a la Ley 21.719 incluye asesoría legal?</summary>
              <p>No. Me hago cargo de la parte técnica y de que la información exigida esté visible y bien implementada en tu sitio. Los textos legales definitivos y los procesos internos deben revisarse con un abogado especialista.</p>
            </details>
          </div>
        </div>
      </div>
    </section>
'''

page('servicios.html', 'Servicios · Luis Vicencio',
     'Branding estratégico, UX/UI y diseño de producto, Product Owner para proyectos de software, y sitios web y ecommerce preparados para la Ley 21.719.',
     current='servicios', body=body,
     cta_title='¿Qué servicio <strong>necesitas</strong>?',
     cta_lead='Escríbeme con una breve descripción de tu proyecto y te respondo con los siguientes pasos.')
