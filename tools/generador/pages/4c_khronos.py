# Contenido basado en el brandbook publicado en Behance (behance.net/gallery/231002797/Cerveza-Khronos).
# Rebranding 2023: el nombre lo eligió el cliente; el proyecto le dio sentido desde su raíz y un concepto que guía la marca.
_kh = next(pr for pr in PROJECTS if pr['slug'] == 'khronos')
page('proyectos/khronos.html', 'Cerveza Khronos · Caso · Luis Vicencio',
     'Caso de estudio: rebranding de Cerveza Khronos, una cervecería artesanal de Chile. Concepto de marca, identidad visual y packaging.',
     current='proyectos', ogtype='article',
     cta_title='¿Tu marca necesita <strong>una idea propia</strong>?',
     cta_lead='Conversemos sobre tu producto y encontremos juntos el concepto que lo distinga.',
     body=case_intro(_kh,
        'Rebranding para una cervecería artesanal nacida en las bierfest. Buscamos el sentido de su nombre en su raíz griega, <em>khronos</em>, tiempo, y lo convertimos en el concepto que guía la marca: tómate el tiempo.',
        [('Cliente', _kh['client']), ('Año', _kh['year']), ('Rol', _kh['role'])])
     + case_detail('Cerveza Khronos: un nombre que encontró <strong>su sentido</strong>.', [
        ('contexto', 'Contexto y <strong>desafío</strong>',
         '<p class="lead">Khronos nació en 2013 recorriendo ferias y bierfest, antes incluso de producir su propia cerveza. Desde 2015 elabora sus variedades y las ha mejorado con constancia hasta estandarizar su calidad.</p>'
         '<p>La cervecería ya tenía nombre y una marca en uso, pero el nombre no tenía un significado detrás ni una idea que orientara cómo comunicar. En ferias y góndolas llenas de etiquetas artesanales parecidas, eso la dejaba sin un argumento propio.</p>'
         '<p>El desafío del rebranding fue darle sentido al nombre y convertirlo en un concepto capaz de direccionar todas las decisiones de la marca.</p>'),
        ('solucion', 'La <strong>solución</strong>',
         '<p class="lead">Un reloj de arena que también se lee como la O del nombre: el tiempo queda dentro de la marca.</p>'
         '<p>La identidad usa el concepto del tiempo para hablar de momentos inolvidables, compartidos y sin apuro. El tagline «Tómate el tiempo» lo convierte en una invitación directa que se repite en cada pieza: tómate el tiempo de explorar, de disfrutar, de una más.</p>'
         '<ul><li>Logotipo con el símbolo integrado y versiones para fondos claros, oscuros y de color.</li>'
         '<li>Etiquetas con un color por variedad (American Pale Ale, IPA, Golden Ale, Stout, Barley Wine y Berries Pale Ale) y una misma estructura de información.</li>'
         '<li>Aplicaciones para ferias: stand, stickers y piezas para concursos en redes sociales.</li></ul>'),
     ]) + case_nav(_kh))
