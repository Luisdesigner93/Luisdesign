# cats: categorías del filtro de Proyectos ('marcas', 'producto'); landing: a qué landing lleva el botón final del caso.
# Orden de aparición (por relevancia; Khronos al final por ser propuesta). status: estado del proyecto en la ficha.
# images: (archivo, ancho, alto, alt, leyenda, encajar). encajar=True muestra la imagen completa (envases, piezas recortadas).
def img(slug, name, w, h, alt, caption, fit=False):
    return dict(src=f'img/proyectos/{slug}/{name}', w=w, h=h, alt=alt, caption=caption, fit=fit)

PROJECTS = [
    dict(slug='fuchi-chao', cats=['marcas'], landing='marcas', title='Fuchi Chao', mark='Fc', kind='Productos para mascotas · Naming, identidad y estrategia', year='2021 y 2023', featured=True,
         summary='De una fórmula industrial a una marca que los petlovers hacen suya. Naming, identidad y etiquetas en 2021; estrategia de marca en 2023. Hoy está en tiendas veterinarias, plataformas en línea y exposiciones de mascotas.',
         tags=['Naming', 'Identidad', 'Packaging', 'Estrategia'], role='Naming, identidad, etiquetas y estrategia de marca', client='Citrex', status='Marca en el mercado',
         images=[img('fuchi-chao', '01.jpg', 1397, 1400, 'Detergente, eliminador de olores y jabón anti olores Fuchi Chao sobre fondo rosado.', 'Línea de productos.'),
                 img('fuchi-chao', '04.jpg', 2000, 896, 'Construcción del logotipo de Fuchi Chao en tres versiones con su área de resguardo.', 'Construcción del logotipo.'),
                 img('fuchi-chao', '02.jpg', 2000, 1132, 'Tres teléfonos con el perfil y publicaciones de Instagram de Fuchi Chao.', 'Redes sociales.'),
                 img('fuchi-chao', '03.jpg', 2000, 1128, 'Envase del jabón anti olores Fuchi Chao junto a su etiqueta extendida con medidas.', 'Etiqueta del jabón anti olores.')]),
    dict(slug='bytequest', cats=['producto'], landing='producto', title='Bytequest', mark='Bq', kind='Marca y producto · Soluciones con IA', year='2025 – 2026', featured=True, en_portafolio=False,
         summary='Marca y producto con un mismo criterio: la identidad de Bytequest y tres productos de IA para organizaciones con procesos complejos.',
         tags=['Product Owner', 'QA', 'Marca'], role='Líder de Innovación y Productos (Brand Manager y Product Owner)', client='Bytequest SpA', status='Prototipos y plataforma en pruebas',
         placeholders=('Marca de Bytequest.', 'Pantallas de Legisnova.'), images=[]),
    dict(slug='lab502', cats=['marcas'], landing='marcas', title='LAB*502', mark='L*', kind='Laboratorio fotográfico · Estrategia e identidad', year='2023', featured=True,
         summary='De una tienda de insumos a un laboratorio creativo con propósito: una marca que le dio al norte una forma de mirarse.',
         tags=['Estrategia', 'Identidad'], role='Estrategia, experiencia de marca, líneas de negocio, identidad y plantillas para redes', client='LAB*502 (antes Taller 502), Iquique', status='Marca en uso',
         images=[img('lab502', '01.webp', 1600, 900, 'Servicios de LAB*502 con cuatro líneas: fotografía de eventos, experiencias análogas, studio fotográfico y editorial 502.', 'Soluciones y servicios.'),
                 img('lab502', '02.webp', 1600, 900, 'Logotipo de LAB*502 con la tipografía Archimoto y el asterisco como constante, en distintas composiciones sobre fondos azul, amarillo, turquesa y magenta.', 'Arquitectura de marca: el logotipo.'),
                 img('lab502', '03.webp', 1400, 788, 'Plantillas para redes de la línea de soluciones: fotografía de eventos y experiencias análogas.', 'Plantillas de niveles: soluciones.'),
                 img('lab502', '04.webp', 1600, 900, 'Construcción del símbolo: el número 502 con la o reemplazada por un marco que contiene un asterisco.', 'La construcción del símbolo.'),
                 img('lab502', '05.webp', 1600, 900, 'Reducción del isotipo a tamaños menores, manteniendo el asterisco dentro del marco.', 'Reducción y adaptabilidad.'),
                 img('lab502', '06.webp', 600, 1066, 'Página de visión de LAB*502 con la frase «Redistribuir los ejes artísticos al norte de Chile» sobre una fotografía del norte.', 'Visión: redistribuir los ejes artísticos.'),
                 img('lab502', '07.webp', 1400, 788, 'Plantillas para redes de la línea corporativa con fotografías en blanco y azul.', 'Plantillas de niveles: corporativo.'),
                 img('lab502', '08.webp', 1920, 1080, 'Afiche de turismo fotográfico en Iquique con la frase «¿Quieres disfrutar del turismo y la fotografía análoga al mismo tiempo?».', 'Turismo fotográfico.'),
                 img('lab502', '09.webp', 1600, 900, 'Plantillas para redes de la línea de exploración: un tutorial de composición y el proceso de una sesión.', 'Plantillas de niveles: exploración.'),
                 img('lab502', '10.webp', 1920, 1080, 'Bolsas de papel kraft con el logotipo LAB*502, el eslogan «Luz, arte y norte» y un sticker con el isotipo.', 'Aplicaciones de marca.')]),
    dict(slug='bowraps', cats=['marcas'], landing='marcas', title='Bowraps', mark='Bw', kind='Comida saludable · Naming e identidad visual', year='2022', featured=False,
         summary='Naming e identidad visual para una marca de wraps y bowls frescos, hoy en funcionamiento en Viña del Mar.',
         tags=['Naming', 'Identidad', 'Aplicaciones'], role='Naming, logotipo, identidad visual y aplicaciones, en colaboración con Claudio Almeyda Godoy', client='Bowraps', status='Marca en uso',
         images=[img('bowraps', '13.webp', 1600, 1599, 'Letrero circular de Bowraps con el isotipo en verde lima sobre fondo verde oscuro.', 'Letrero del local.'),
                 img('bowraps', '01.webp', 1600, 900, 'Mockups de uniformes, delantal y gorras con el logotipo de Bowraps en verde lima.', 'Uniformes y accesorios.'),
                 img('bowraps', '02.webp', 1600, 900, 'Logotipo horizontal de Bowraps con el eslogan Fresh wraps & bowls sobre fondo claro.', 'Logotipo.'),
                 img('bowraps', '03.webp', 1600, 958, 'Construcción del logotipo de Bowraps sobre una retícula de medidas.', 'Construcción del logotipo.'),
                 img('bowraps', '04.webp', 1600, 2171, 'Piezas de la identidad de Bowraps: naming, imagotipo, uso del color y aplicaciones.', 'Sistema de identidad.'),
                 img('bowraps', '05.webp', 1600, 1114, 'Aplicaciones de Bowraps en su local y en sus piezas gráficas.', 'Aplicaciones en el local.'),
                 img('bowraps', '06.webp', 1600, 900, 'Pieza gráfica de Bowraps con la pregunta «¿y tú qué team eliges?» y los hashtags #teamwraps y #teambowls.', 'Campaña #teamwraps y #teambowls.'),
                 img('bowraps', '07.webp', 1600, 796, 'Piezas de Bowraps: menú con código QR, stickers y etiquetas con el eslogan «team wraps o team bowls?».', 'Menú y stickers.'),
                 img('bowraps', '08.webp', 1600, 901, 'Menú de Bowraps con bowls de vegan, falafel y atún, con sus precios.', 'Menú de bowls.'),
                 img('bowraps', '09.webp', 1600, 447, 'Fotografías de verduras frescas usadas en la línea gráfica de Bowraps.', 'Ingredientes frescos.'),
                 img('bowraps', '10.webp', 1600, 1555, 'Menús digitales de Bowraps para teléfono: wraps, bowls, agregados y arma tu personalizado.', 'Menús digitales.'),
                 img('bowraps', '11.webp', 1600, 1694, 'Pantallas del local de Bowraps con el menú de wraps y de agregados.', 'Pantallas del local.'),
                 img('bowraps', '12.webp', 1600, 1712, 'Fachada de Bowraps con el nombre en letras blancas sobre fondo verde.', 'Fachada del local.')]),
    dict(slug='sustentando', cats=['marcas'], landing='marcas', title='Sustentando', mark='Su', kind='Consultoría en calidad · Branding y web', year='2022 – 2026', featured=True,
         summary='Desde 2022 acompaño a Sustentando como aliado estratégico. Partimos por entender sus necesidades y fuimos escalando el servicio hasta consolidar una comunicación que eleva el valor percibido de su trabajo.',
         tags=['Identidad', 'Web', 'Comunicación B2B'], role='Identidad, web, comunicación B2B y diseño gráfico', client='Sustentando', status='Aliado desde 2022',
         images=[img('sustentando', '01.jpg', 1600, 899, 'Piezas de Sustentando con los servicios de implementación, cursos, gestión de proveedores y proyectos de cultura y calidad.', 'Sistema de piezas para los servicios de Sustentando.'),
                 img('sustentando', '02.jpg', 1200, 1200, 'Logotipo de Sustentando sobre piezas gráficas y el sitio web en un teléfono.', 'Identidad y sitio web en móvil.'),
                 img('sustentando', '05.png', 800, 575, 'Llaveros, carpeta y piezas impresas de Sustentando OTEC.', 'Aplicaciones de marca para Sustentando OTEC.', True),
                 img('sustentando', '04.jpg', 1600, 899, 'Página de artículo del sitio web de Sustentando.', 'Página de artículo del sitio web.'),
                 img('sustentando', '03.jpg', 1600, 899, 'Plantillas de redes sociales de Sustentando organizadas por nivel de comunicación.', 'Plantillas de redes sociales por nivel de comunicación.'),
                 img('sustentando', '06.jpg', 1000, 939, 'Publicación de Sustentando en LinkedIn sobre un curso de auditores internos de calidad.', 'Publicación para LinkedIn.')]),
    dict(slug='yomecontrolo', cats=['producto'], landing='producto', title='Yomecontrolo', mark='Ym', kind='Salud preventiva · Marca y UX/UI', year='2023 – 2024', featured=True,
         summary='Estrategia, experiencia y expresión de marca para Yomecontrolo, una startup chilena de salud preventiva. Una marca que deja atrás la carga negativa de ir al médico y acompaña a las personas a cuidar su salud mucho antes de que llegue la enfermedad.',
         tags=['Marca', 'UX/UI', 'Producto'], role='Estrategia de marca, identidad y UX/UI', client='Yomecontrolo', status='Marca en uso · MVP no implementado',
         images=[img('yomecontrolo', '05.jpg', 1672, 941, 'Sitio de Yomecontrolo en un portátil junto a la tarjeta de resultado de la calculadora de edad del corazón.', 'Calculadora de edad del corazón.'),
                 img('yomecontrolo', '06.jpg', 1629, 966, 'Logotipo de Yomecontrolo con el tagline “vivir más y mejor” sobre fondo celeste.', 'Logotipo.'),
                 img('yomecontrolo', '07.jpg', 906, 1736, 'Teléfono con la pantalla “Controla tus indicadores de salud” de la web app de Yomecontrolo.', 'Web app: indicadores de salud.'),
                 img('yomecontrolo', '08.jpg', 1122, 1402, 'Ícono de Yomecontrolo en la pantalla de inicio de un teléfono.', 'Acceso directo en el teléfono.')]),
    dict(slug='auditorweb', cats=['producto'], landing='producto', title='AuditorWeb 21.719', mark=None, kind='Producto digital', year='2026', featured=True, en_portafolio=False,
         summary='Auditor automatizado que revisa 30 controles de cumplimiento de la Ley de Protección de Datos Personales y entrega un plan de acción priorizado.',
         tags=['Producto', 'UX/UI', 'IA'], images=[], role='Producto, UX/UI y desarrollo asistido con IA', client='Producto propio'),
    dict(slug='uvenergy', cats=['marcas'], landing='marcas', title='Uvenergy', mark='UV', kind='Energía solar y eólica · Identidad y web', year='2023 y 2025', featured=False,
         summary='Una marca que acompañó a Uvenergy desde su lanzamiento hasta su consolidación en la ingeniería de energías renovables.',
         tags=['Identidad', 'Web'], role='Identidad de marca, presentación comercial, sitio web con blog y rediseño', client='Uvenergy', status='Marca en uso',
         # EDITAR: imágenes de la identidad, la presentación y las dos versiones del sitio
         images=[img('uvenergy', '01.jpg', 1600, 899, 'Página de artículo del sitio web de Uvenergy sobre el mantenimiento de plantas fotovoltaicas.', 'Página de artículo del sitio web.')]),
    dict(slug='botes-salvavidas', cats=['marcas'], landing='marcas', title='Botes Salvavidas de Valparaíso', mark='BS', kind='Comunicación · Web y redes', year='2023 y 2025', featured=False,
         summary='Una estrategia de comunicación para que Valparaíso reconozca la labor de rescate que los Botes Salvavidas cumplen cada día.',
         tags=['Comunicación', 'Web', 'Redes'], role='Estrategia de comunicación, sitio web, redes sociales y logo del centenario', client='Botes Salvavidas de Valparaíso',
         images=[img('botes-salvavidas', '04.webp', 1600, 1230, 'Mockup de Instagram de Botes Salvavidas con tres piezas para redes: alertas en el mar, voluntariado y socios.', 'Piezas para redes sociales.'),
                 img('botes-salvavidas', '03.webp', 919, 1711, 'Logotipo conmemorativo del centenario de los Botes Salvavidas: el número 100 en naranja, rojo y azul, con la leyenda Desde 1925 y el nombre CV Bote Salvavidas Valparaíso.', 'Logotipo del centenario.')]),
    dict(slug='khronos', cats=['marcas'], landing='marcas', title='Cerveza Khronos', mark='Kh', kind='Cerveza artesanal · Rebranding y packaging', year='2023', featured=True,
         summary='Rebranding para una cervecería artesanal nacida en las bierfest. Buscamos el sentido de su nombre en su raíz griega, khronos, tiempo, y lo convertimos en el concepto que guía la marca: tómate el tiempo.',
         tags=['Propuesta', 'Estrategia', 'Packaging'], role='Estrategia, concepto, identidad y packaging', client='Cervecería Khronos', status='Propuesta de rebranding, no implementada', proposal=True,
         # EDITAR: sumar las nuevas imágenes del proyecto a medida que estén listas
         images=[img('khronos', '05.jpg', 1672, 941, 'Logotipo de Cerveza Khronos con el tagline “Tómate el tiempo” en blanco sobre un muro naranja.', 'Logotipo.'),
                 img('khronos', '01.jpg', 1672, 941, 'Cuatro botellas de Cerveza Khronos flotando: American Pale Ale, Stout, IPA y Golden Ale.', 'Línea de cervezas.'),
                 img('khronos', '02.jpg', 1254, 1254, 'Fila de botellas Khronos con etiquetas de colores para cada variedad.', 'Un color por variedad.'),
                 img('khronos', '03.jpg', 1254, 1254, 'Botella de Cerveza Khronos Stout sobre un bloque de piedra.', 'Etiqueta Stout.'),
                 img('khronos', '04.jpg', 1254, 1254, 'Botella de Cerveza Khronos American Pale Ale con el tagline “Tómate el tiempo” sobre fondo naranja.', 'Etiqueta American Pale Ale.')]),
]

AUDITOR_ART = '''<div class="mini-window">
                <div class="mini-bar"><i></i><i></i><i></i><span></span></div>
                <div class="mini-report">
                  <div class="mini-gauge"><span>78</span></div>
                  <div class="mini-lines"><span class="sk sk-w80"></span><span class="sk sk-w60"></span><span class="sk sk-w40"></span><div class="mini-pills"><span>Cumple</span><span>Art. 14 ter</span></div></div>
                </div>
              </div>'''


def img_tag(im, cls='', lazy=True):
    c = (cls + (' fit-contain' if im['fit'] else '')).strip()
    src, w, h, alt = im['src'], im['w'], im['h'], im['alt']
    return (f'<img src="{{p}}{src}" width="{w}" height="{h}" alt="{alt}"'
            + (f' class="{c}"' if c else '') + (' loading="lazy"' if lazy else '') + ' decoding="async">')


def project_art(pr, lazy=True):
    if pr['images']:
        return img_tag(pr['images'][0], lazy=lazy)
    if pr['mark'] is None:
        return AUDITOR_ART
    # EDITAR: reemplazar por una imagen del proyecto (<img src="..." alt="" width height>)
    return f'''<div class="ph-art"><span class="ph-mark">{pr['mark']}</span><span class="sk-stack"><span class="sk sk-w80"></span><span class="sk sk-w55"></span></span></div>'''


def project_card(pr, heading='h3'):
    tags = ''.join(f'<li class="tag">{t}</li>' for t in pr['tags'])
    return f'''          <a class="card project" href="{{p}}proyectos/{pr['slug']}.html">
            <div class="project-art" aria-hidden="true">
              {project_art(pr)}
            </div>
            <div class="project-body">
              <span class="eyebrow-text">{pr['kind']} · {pr['year']}</span>
              <{heading} class="title">{pr['title']}</{heading}>
              <p>{pr['summary']}</p>
              <div class="project-meta">
                <ul class="tag-list" aria-label="Disciplinas">{tags}</ul>
                <span class="link-arrow">Ver caso <svg class="icon" aria-hidden="true"><use href="{{p}}img/icons.svg#i-arrow"/></svg></span>
              </div>
            </div>
          </a>
'''


def _caso_vecino(pr, etiqueta, lado):
    """Tarjeta de proyecto vecino: imagen lateral difuminada hacia el texto (mismo efecto que el blog). Sin imagen, solo texto."""
    texto = '<div class="caso-texto"><span>' + etiqueta + '</span><strong>' + pr['title'] + '</strong></div>'
    foto = ''
    if pr['images']:
        im = pr['images'][0]
        foto = ('<figure class="caso-foto"><img src="{p}' + im['src'] + '" width="' + str(im['w']) + '" height="' + str(im['h'])
                + '" alt="' + im['alt'] + '" loading="lazy" decoding="async"></figure>')
    contenido = foto + texto if lado == 'izq' else texto + foto
    clase = 'card caso-vecino caso-vecino-' + lado + (' con-foto' if foto else '')
    return '<a class="' + clase + '" href="' + pr['slug'] + '.html">' + contenido + '</a>'


def case_nav(pr):
    # Los proyectos con en_portafolio=False no aparecen como vecinos (el propio caso sí conserva su lugar)
    lista = [x for x in PROJECTS if x.get('en_portafolio', True) or x['slug'] == pr['slug']]
    i = [x['slug'] for x in lista].index(pr['slug'])
    prev, nxt = lista[i - 1], lista[(i + 1) % len(lista)]
    tarjetas = _caso_vecino(prev, 'Proyecto anterior', 'izq') + _caso_vecino(nxt, 'Proyecto siguiente', 'der')
    return ('    <section class="panel panel-plain section" aria-label="Otros proyectos">\n'
            '      <div class="container">\n'
            '        <nav class="case-nav" aria-label="Más proyectos">' + tarjetas + '</nav>\n'
            '      </div>\n'
            '    </section>\n')


# ---- Caso de estudio: composición minimalista (referencia: wama.com.br/cases) ----
# Arriba: columna fija con título, datos, disciplinas y resumen; a la derecha, las imágenes apiladas.
# Abajo: el detalle del caso en una sola columna de lectura.

def case_media(pr, placeholders=()):
    """Imágenes apiladas del caso. Sin imágenes: la portada ilustrada y marcadores (EDITAR)."""
    if pr['images']:
        return ''.join(f'\n            <figure>{img_tag(im, lazy=i > 0)}</figure>' for i, im in enumerate(pr['images']))
    out = f'\n            <figure class="case-art" aria-hidden="true">{project_art(pr, lazy=False)}</figure>'
    # EDITAR: reemplazar los marcadores por <img src="..." alt="..." width="..." height="..." loading="lazy">
    out += ''.join(f'\n            <figure><div class="media-ph" role="img" aria-label="Imagen pendiente: {c}"><svg class="icon" aria-hidden="true"><use href="{{p}}img/icons.svg#i-image"/></svg>{c}</div></figure>'
                   for c in placeholders)
    return out


def case_intro(pr, summary, facts, actions=''):
    rows = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in facts)
    chips = ''.join(f'<li>{t}</li>' for t in pr['tags'])
    return f'''    <section class="case-intro" aria-labelledby="page-title">
      <div class="container case-intro-grid">
        <div class="case-aside">
          <ol class="breadcrumb" aria-label="Ruta"><li><a href="{{home}}">Inicio</a></li><li><a href="{{home}}#proyectos">Proyectos</a></li><li aria-current="page">{pr['title']}</li></ol>
          <h1 class="case-title" id="page-title">{pr['title']}</h1>
          <dl class="case-meta">{rows}</dl>
          <ul class="case-chips" aria-label="Disciplinas">{chips}</ul>
          <p class="case-summary">{summary}</p>{actions}
        </div>
        <div class="case-media">{case_media(pr, pr.get('placeholders', ('Imagen del proyecto', 'Imagen del proyecto')))}
        </div>
      </div>
    </section>
'''


def case_rows(items):
    """Lista de responsabilidades: nombre y descripción."""
    return '<dl class="case-rows">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items) + '</dl>'


def case_steps(items):
    return '<ol class="case-steps">' + ''.join(f'<li><strong>{k}</strong><span>{v}</span></li>' for k, v in items) + '</ol>'


def case_stats(items):
    return '<dl class="case-stats">' + ''.join(f'<div><dt>{n}</dt><dd>{t}</dd></div>' for n, t in items) + '</dl>'


def case_quote(text, cite):
    return f'<blockquote class="case-quote"><p>“{text}”</p><cite>{cite}</cite></blockquote>'


def case_detail(statement, sections):
    """sections: lista de (id, título, html). El título lleva <strong> en la palabra clave."""
    secs = ''.join(f'''
        <section class="case-sec" aria-labelledby="{sid}-title">
          <h2 class="case-sec-title" id="{sid}-title"><span class="numtag">{i:02d}</span>{title}</h2>
          <div class="case-text">{html}</div>
        </section>''' for i, (sid, title, html) in enumerate(sections, 1))
    return f'''
    <article class="case-detail" aria-label="Detalle del caso">
      <div class="container case-read">
        <p class="case-statement">{statement}</p>{secs}
      </div>
    </article>
'''


def case_facts(pr, *extra):
    """Ficha del caso: cliente, año, rol y estado (si lo tiene), más filas extra opcionales."""
    facts = [('Cliente', pr['client']), ('Año', pr['year']), ('Rol', pr['role'])] + list(extra)
    if pr.get('status'):
        facts.append(('Estado', pr['status']))
    return facts


# ---- SEO: imagen para compartir y datos estructurados (schema.org en JSON-LD) ----
# Frase de identidad de tools/narrativa/01-narrativa-y-casos.md ("Para que la IA te recomiende"), siempre igual.
IDENTIDAD = 'Luis Vicencio es diseñador y Product Owner en Chile, especializado en branding, diseño web, UX/UI y gestión de productos digitales con Scrum.'
PERFILES = ['https://www.linkedin.com/in/luisvicenciodesign', 'https://www.behance.net/LuisHVicencio']
TELEFONO = '+56958217041'
PERSON_ID = SITE + '#luis'


def person_ld(**extra):
    d = {'@context': 'https://schema.org', '@type': 'Person', '@id': PERSON_ID, 'name': 'Luis Vicencio', 'url': SITE,
         'jobTitle': 'Diseñador y Product Owner', 'description': IDENTIDAD, 'image': SITE + 'img/marca/luis-vicencio-retrato.png',
         'email': 'mailto:' + EMAIL, 'telephone': TELEFONO, 'sameAs': PERFILES,
         'address': {'@type': 'PostalAddress', 'addressCountry': 'CL'}}
    d.update(extra)
    return d


def service_ld(name, description, url, lang='es'):
    return {'@context': 'https://schema.org', '@type': 'Service', 'name': name, 'description': description, 'url': SITE + url,
            'serviceType': name, 'provider': {'@id': PERSON_ID}, 'areaServed': {'@type': 'Country', 'name': 'Chile'}, 'inLanguage': lang}


def faq_ld(items, lang='es'):
    import re as _re
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'inLanguage': lang,
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': _re.sub('<[^>]+>', '', a)}} for q, a in items]}


def case_og(pr):
    """Imagen para compartir del caso (img/og/<slug>.jpg si existe; si no, la general)."""
    return f"img/og/{pr['slug']}.jpg" if pr['images'] else None


def case_seo(pr, desc):
    """og:image y CreativeWork para la página de un caso."""
    og = case_og(pr)
    ld = {'@context': 'https://schema.org', '@type': 'CreativeWork', 'name': pr['title'], 'description': desc,
          'url': SITE + f"proyectos/{pr['slug']}.html", 'dateCreated': pr['year'][:4], 'creator': {'@id': PERSON_ID},
          'author': {'@type': 'Person', 'name': 'Luis Vicencio', 'url': SITE}, 'keywords': ', '.join(pr['tags']),
          'image': SITE + (og or 'img/og/general.jpg'), 'inLanguage': 'es'}
    if pr['client'] != 'Producto propio':
        ld['sourceOrganization'] = {'@type': 'Organization', 'name': pr['client']}
    return dict(og_image=og, og_alt=pr['images'][0]['alt'] if pr['images'] else None, jsonld=[ld])


def case_page(pr, title, desc, summary, statement, sections, facts=None, cta_title=None, cta_lead=None, actions=''):
    """Página de caso con la plantilla: ficha, secciones, botón a su landing y navegación."""
    page(f"proyectos/{pr['slug']}.html", title, desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio', extra_css=['css/inicio.css'],
         **case_seo(pr, desc), body=case_intro(pr, summary, facts or case_facts(pr), actions) + case_detail(statement, sections) + case_nav(pr))


# ---- Piezas del inicio (index.html; index-v2.html tiene las suyas en fragmentos/) ----
from urllib.parse import quote

# WhatsApp con mensaje precargado de la landing Marcas (texto de tools/narrativa/02-landing-marcas.md)
WA_MARCAS = 'https://wa.me/56958217041?text=' + quote('Hola Luis, tengo un negocio de [rubro] y me interesa [identidad visual / branding estratégico / sitio web]. Mi plazo es [plazo].')
_clients = ['Fuchi Chao', 'LAB*502', 'Sustentando', 'Uvenergy', 'Bytequest', 'Yomecontrolo', 'Bowraps', 'Botes Salvavidas']
# Logotipos para la cinta (nombre → (archivo, ancho, alto)); el resto se muestra como texto.
# EDITAR: idealmente reemplazar por SVG o PNG de mayor resolución (Khronos mide solo 56 × 25 px).
_client_logos = {'Cerveza Khronos': ('khronos.png', 56, 25), 'Sustentando': ('sustentando.png', 218, 64), 'Yomecontrolo': ('yomecontrolo.png', 156, 38)}


def _client_item(name):
    if name in _client_logos:
        f, w, h = _client_logos[name]
        return f'<li class="v2-marquee-logo"><img src="img/logos/{f}" width="{w}" height="{h}" alt="{name}" loading="lazy" decoding="async"></li>'
    return f'<li>{name}</li>'


_marquee = ''.join(_client_item(c) for c in _clients)
HOME_HERO = f'''    <!-- HERO -->
    <section class="v2-hero-shell" aria-labelledby="v2-title">
      <div class="v2-hero">
        <img class="v2-hero-bg" src="img/marca/hero-fondo.jpg" width="2000" height="1333" alt="" decoding="async" fetchpriority="high">
        <div class="v2-hero-top">
          <span class="v2-eyebrow"><i aria-hidden="true"></i>Luis Vicencio · Diseño de marca</span>
          <h1 class="v2-hero-title" id="v2-title">Marcas para pymes que quieren <strong>dejar huella</strong>.</h1>
          <p class="v2-hero-lead">Defino el propósito de tu marca y lo convierto en una identidad que invita a tus clientes a ir contigo. Branding estratégico, identidad visual y sitios web para pymes y empresas en Chile.</p>
        </div>
        <div class="v2-hero-bottom">
          <div class="v2-hero-cta">
            <div class="btn-row">
              <a class="btn btn-primary v2-btn-light" href="{WA_MARCAS}" rel="noopener noreferrer" target="_blank">Conversemos sobre tu marca<span class="sr-only"> (WhatsApp, se abre en una pestaña nueva)</span> <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
              <a class="btn v2-btn-ghost" href="{{home}}#proyectos">Ver proyectos</a>
            </div>
          </div>
        </div>
      </div>
    </section>

'''

HOME_MARQUEE = '''    <!-- CINTA DE CLIENTES -->
    <section class="v2-marquee" aria-label="Marcas con las que he trabajado">
      <p class="v2-marquee-lead">Han trabajado conmigo</p>
      <div class="v2-marquee-track">
        <ul>{marquee}</ul>
        <ul aria-hidden="true">{marquee}</ul>
      </div>
    </section>

'''.replace('{marquee}', _marquee)

