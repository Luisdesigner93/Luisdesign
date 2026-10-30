# Caso Sustentando (2022 – hoy): identidad y web, comunicación B2B, diseño para sus servicios, rediseño web y stand Inofood 2026.
# EDITAR: confirmar la descripción del rubro del cliente y sumar imágenes del sitio nuevo y del stand.
_su = next(pr for pr in PROJECTS if pr['slug'] == 'sustentando')
_su_desc = 'Caso de estudio: identidad de marca, sitio web, comunicación B2B y diseño gráfico para Sustentando, desde 2022.'
page('proyectos/sustentando.html', 'Sustentando: identidad, sitio web y comunicación B2B para una consultora · Luis Vicencio',
     _su_desc, current='proyectos', ogtype='article', **case_seo(_su, _su_desc),
     contact=False, html_class='motion inicio', extra_css=['css/inicio.css'], cta_title='¿Buscas un aliado para <strong>hacer crecer tu marca</strong>?',
     cta_lead='Conversemos sobre la etapa en que está tu empresa y veamos juntos por dónde partir.',
     body=case_intro(_su, _su['summary'],
        case_facts(_su))
     + case_detail('Sustentando: de un logotipo a una empresa <strong>consolidada en su comunicación</strong>.', [
        ('necesidades', 'Entender las <strong>necesidades</strong>',
         '<p class="lead">Todo partió por entender qué necesitaba Sustentando en ese momento, no por lo que podía ofrecerle.</p>'
         '<p>Sustentando es una consultora chilena que acompaña a empresas en calidad e inocuidad. En 2022 su prioridad era presentarse de forma profesional: un logotipo, presentaciones comerciales y un sitio web. Diseñé una identidad simple y sólida, pensada como base para lo que vendría.</p>'),
        ('escalar', 'Escalar el <strong>servicio</strong>',
         '<p class="lead">A medida que la empresa crecía, fuimos sumando capas de trabajo según lo que su equipo necesitaba.</p>'
         '<p>Primero, una estrategia de comunicación B2B para LinkedIn, con plantillas por nivel para que el equipo publicara de forma constante y consistente.</p>'
         '<p>Luego, el diseño de los materiales que acompañan sus propios servicios: presentaciones, brochures y señalética de seguridad y calidad para sus clientes.</p>'
         '<p>Hoy rediseñamos su sitio web y diseñé su stand para Inofood 2026.</p>'),
        ('aliado', 'Un aliado <strong>dentro del equipo</strong>',
         '<p class="lead">La confianza de sus clientes la gana Sustentando con su servicio; mi trabajo es que ese servicio se vea y se perciba con la calidad que tiene.</p>'
         '<p>Para lograrlo me involucro como un integrante más del equipo: detecto sus necesidades y carencias, y las resuelvo con diseño y comunicación. El resultado es una empresa consolidada comunicacionalmente, con un valor percibido relevante para sus clientes.</p>'
         '<p>En una consultoría B2B, el cliente decide por la percepción que tiene de un proveedor que todavía no conoce. La comunicación en LinkedIn le ha traído a Sustentando nuevos clientes, y su equipo sigue confiando en mí como alguien que resuelve lo que necesitan en cada etapa.</p>'),
         # EDITAR: pedir a Sustentando una frase corta sobre el trabajo (testimonio)
     ]) + case_nav(_su))
