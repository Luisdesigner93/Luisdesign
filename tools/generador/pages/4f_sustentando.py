# Caso Sustentando (2022 – hoy): identidad y web, comunicación B2B, diseño para sus servicios, rediseño web y stand Inofood 2026.
# EDITAR: confirmar la descripción del rubro del cliente y sumar imágenes del sitio nuevo y del stand.
_su = next(pr for pr in PROJECTS if pr['slug'] == 'sustentando')
page('proyectos/sustentando.html', 'Sustentando · Caso · Luis Vicencio',
     'Caso de estudio: identidad de marca, sitio web, comunicación B2B y diseño gráfico para Sustentando, desde 2022.',
     current='proyectos', ogtype='article',
     cta_title='¿Buscas un aliado para <strong>hacer crecer tu marca</strong>?',
     cta_lead='Conversemos sobre la etapa en que está tu empresa y veamos juntos por dónde partir.',
     body=case_intro(_su, _su['summary'],
        [('Cliente', _su['client']), ('Año', _su['year']), ('Rol', _su['role'])])
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
         '<p>Para lograrlo me involucro como un integrante más del equipo: detecto sus necesidades y carencias, y las resuelvo con diseño y comunicación. El resultado es una empresa consolidada comunicacionalmente, con un valor percibido relevante para sus clientes.</p>'),
     ]) + case_nav(_su))
