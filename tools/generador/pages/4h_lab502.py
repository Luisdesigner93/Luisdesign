# Caso LAB*502 (2023), Iquique. Texto de tools/narrativa/01-narrativa-y-casos.md ("Caso nuevo: LAB*502").
# EDITAR (opcional): nombre del fondo cultural, si se puede mencionar.
_lab = next(pr for pr in PROJECTS if pr['slug'] == 'lab502')
case_page(_lab, 'LAB*502: estrategia, líneas de negocio e identidad para un laboratorio fotográfico del norte de Chile · Luis Vicencio',
    'Caso de estudio: propósito, líneas de negocio, experiencia de marca e identidad de LAB*502, un laboratorio creativo de fotografía en Iquique.',
    _lab['summary'],
    'LAB*502: <strong>luz, arte y norte</strong>.', [
    ('contexto', 'Contexto y <strong>desafío</strong>',
     '<p class="lead">Taller 502 vendía insumos de fotografía y revelado en el norte de Chile, y además hacía fotografía. Pero su marca solo hablaba de la venta de insumos, y dejaba fuera todo lo demás que sabían hacer. Necesitaban una marca nueva, una historia nueva y un propósito que los ordenara.</p>'),
    ('estrategia', 'La <strong>estrategia</strong>',
     '<p class="lead">Les propuse un propósito ligado a su territorio: capturar y poner en valor el legado visual del norte junto a su comunidad.</p>'
     '<p>A partir de él definimos la experiencia esperada de la marca y ordenamos el negocio en cuatro líneas: fotografía de eventos, experiencias análogas, estudio fotográfico para pymes y Editorial 502.</p>'),
    ('identidad', 'La <strong>identidad</strong>',
     '<p class="lead">El nombre 502 ya existía. Lo transformamos de «taller» a «laboratorio» porque un lab expresaba mejor lo que buscaban: experimentar, crear y revelar.</p>'
     '<p>El asterisco es un destello fotográfico, y junto a una tipografía de carácter y un azul intenso construye una identidad moderna, con el lema «Luz, arte y norte». Sumamos plantillas para redes sociales por línea de negocio.</p>'),
    ('resultado', '<strong>Resultado</strong>',
     '<p class="lead">Con la estrategia en la mano, LAB*502 se adjudicó un fondo cultural que le dio años de vida: una maratón fotográfica para capturar el legado visual del norte, la misma idea que propusimos, llevada a su comunidad.</p>'
     '<p>La marca construyó una comunidad que la reconocía no solo en el nicho fotográfico, sino en todo el norte, y las líneas de negocio que supimos comunicar le trajeron clientes de forma constante.</p>'),
    ],
    cta_title='¿Tu negocio hace más de lo que <strong>tu marca cuenta</strong>?',
    cta_lead='Conversemos sobre tus líneas de negocio y encontremos juntos el propósito que las ordene.')
