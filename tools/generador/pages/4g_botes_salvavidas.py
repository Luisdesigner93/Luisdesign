# Caso Botes Salvavidas de Valparaíso (2023). Texto de tools/narrativa/01-narrativa-y-casos.md ("Caso redactado: Botes Salvavidas de Valparaíso").
# EDITAR: confirmar con David (@lascatasdelcata) cómo quiere ser mencionado; por ahora no se nombra.
# EDITAR: imágenes de redes, web y logo del centenario.
_bs = next(pr for pr in PROJECTS if pr['slug'] == 'botes-salvavidas')
case_page(_bs, 'Botes Salvavidas de Valparaíso: estrategia de comunicación, sitio web y redes sociales · Luis Vicencio',
    'Caso de estudio: estrategia de comunicación, sitio web con donaciones, redes sociales y logo del centenario de los Botes Salvavidas de Valparaíso.',
    _bs['summary'],
    'Botes Salvavidas de Valparaíso: <strong>estrategia de comunicación</strong>, sitio web y redes sociales.', [
    ('contexto', 'Contexto y <strong>desafío</strong>',
     '<p class="lead">En Valparaíso, muchas personas asociaban a los Botes Salvavidas solo con su restaurante. Su labor principal, el rescate en el mar, se confundía con la de la Armada, y la comunidad no veía el trabajo diario que hacen por ella.</p>'
     '<p>A eso se sumaba una comunicación que no se veía moderna. El primer pedido fue una página web que permitiera recibir donaciones, pero el desafío de fondo era otro: que se supiera quiénes son y qué hacen.</p>'),
    ('estrategia', 'La <strong>estrategia</strong>',
     '<p class="lead">Antes de diseñar el sitio, definimos una estrategia de comunicación centrada en su acción diaria de rescate y en su aporte a la comunidad. Esa estrategia orientó todo lo que vino después: el tono, los contenidos y la forma de mostrarse.</p>'
     '<p>Fue un trabajo en colaboración. Junto a un realizador audiovisual armamos las propuestas de comunicación y grabamos contenidos, y construimos la parte visual a partir del material de varios fotógrafos que habían registrado la labor de los Botes.</p>'
     '<!-- EDITAR: qué mensajes principales definieron y qué diferenciaba su labor de la de la Armada; qué opciones visuales se exploraron -->'),
    ('solucion', 'La <strong>solución</strong>',
     '<ul><li><strong>Redes sociales:</strong> material visual dinámico y claro, que muestra los rescates y el trabajo de los voluntarios.</li>'
     '<li><strong>Sitio web:</strong> la misma estrategia llevada a la web, con un espacio para donar.</li>'
     '<li><strong>Logo del centenario:</strong> una identidad para celebrar sus 100 años.</li></ul>'),
    ('resultado', '<strong>Resultado</strong>',
     '<p class="lead">Los Botes Salvavidas pasaron a tener una comunicación moderna y coherente entre redes y web, que pone su labor de rescate al centro y abre un canal directo para recibir donaciones.</p>'
     '<!-- EDITAR (opcional): una frase de alguien de la institución, o un dato como seguidores o donaciones recibidas por la web -->'),
    ],
    cta_title='¿Tu organización necesita <strong>que se entienda lo que hace</strong>?',
    cta_lead='Conversemos sobre tu comunicación y definamos juntos qué contar y cómo.')
