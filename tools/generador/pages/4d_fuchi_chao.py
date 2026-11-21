# Caso Fuchi Chao para Citrex. Composición editorial del Figma «Portfolio» (nodo 344:398), con las clases lab-* de css/inicio.css
# (variantes lab-fc-*). El texto del caso es el del diseño; la ficha viene de 0_data.py.
# Las imágenes caso-* salen de la carpeta del portafolio; tras cambiarlas, ejecutar webp.py antes de build.py.
_fc = next(pr for pr in PROJECTS if pr['slug'] == 'fuchi-chao')
_FC_IMG = {
    'portada': ('caso-01-portada.jpg', 2000, 1374, 'Botella de detergente anti olores Fuchi Chao sobre una manta rosada, junto al logotipo.'),
    'tenencia': ('caso-02-tenencia.jpg', 2000, 1125, 'Mujer con audífonos junto a un perro y el mensaje: te queremos dar una tenencia feliz, libre de olores molestos.'),
    'paleta': ('caso-03-paleta.jpg', 2000, 1610, 'Paleta de colores de Fuchi Chao: naranjo, turquesa, rosado, violeta, azul violeta y dos tonos claros.'),
    'linea': ('caso-04-linea.jpg', 2000, 2000, 'Detergente, eliminador de olores y jabón anti olores Fuchi Chao sobre fondo rosado.'),
    'manual': ('caso-05-manual.jpg', 2000, 1260, 'Páginas del manual de identidad de Fuchi Chao dispuestas en perspectiva.'),
    'simbolo': ('caso-06-simbolo.jpg', 2000, 1000, 'Construcción del símbolo de gato junto a un gato y un perro ilustrados con corbata y lentes, y publicaciones de la marca.'),
    'logotipo': ('caso-07-logotipo.jpg', 2000, 1013, 'Versiones del logotipo con su área de resguardo, etiqueta del eliminador de olores e íconos de uso.'),
    'post': ('caso-09-a.jpg', 2000, 2000, 'Publicación de Instagram de Fuchi Chao con recomendaciones para mascotas en verano.'),
    'afiche': ('caso-09-b.jpg', 2000, 2000, 'Afiches de Fuchi Chao en la calle mientras una persona pasa con su perro.'),
    'niveles': ('caso-10-niveles.jpg', 1400, 506, 'Publicaciones para los cuatro niveles de comunicación: corporativo, soluciones, nuestra tribu y responsabilidad.'),
    'redes': ('caso-11-redes.jpg', 2000, 1125, 'Tres teléfonos con el perfil y publicaciones de Instagram de Fuchi Chao.'),
    'personajes': ('caso-12-personajes.jpg', 2000, 1812, 'Perro con pañuelo y gato con corona ilustrados sobre fondo turquesa.'),
    'etiqueta': ('caso-13-etiqueta.jpg', 2000, 1559, 'Envase del jabón anti olores junto a su etiqueta extendida con medidas.'),
    'giro-jabon': ('caso-giro-jabon.gif', 600, 600, 'Botella de jabón anti olores Fuchi Chao girando sobre fondo rosado.'),
    'giro-eliminador': ('caso-giro-eliminador.gif', 600, 600, 'Botella de eliminador de olores Fuchi Chao girando sobre fondo rosado.'),
    'giro-detergente': ('caso-giro-detergente.gif', 600, 600, 'Botella de detergente anti olores Fuchi Chao girando sobre fondo rosado.'),
}


def _fc_fig(key, cls='', lazy=True, mitad=False):
    name, w, h, alt = _FC_IMG[key]
    return f'<figure class="lab-fig{(" " + cls) if cls else ""}">{img_tag(img("fuchi-chao", name, w, h, alt, ""), "lab-img-half" if mitad else "lab-img", lazy=lazy)}</figure>'


_fc_chips = ''.join(f'<li>{t}</li>' for t in [*_fc['tags'], 'Comunicación'])
_fc_body = f'''    <section class="lab-head" aria-labelledby="page-title">
      <div class="lab-wide">
        {case_ruta(_fc)}
        <h1 class="lab-title" id="page-title">{_fc['title']}</h1>
        <p class="lab-lead">Branding para una tenencia feliz sin olores molestos.</p>
        <div class="lab-meta">
          <ul class="case-chips" aria-label="Disciplinas">{_fc_chips}</ul>
          <p class="lab-year"><span class="sr-only">Año: </span>{_fc['year']}</p>
        </div>
      </div>
    </section>

    <article class="lab-case lab-wide" aria-label="Detalle del caso">
      <div class="lab-fc-hero">{_fc_fig('portada', lazy=False)}<div class="lab-fc-giros">{_fc_fig('giro-jabon', lazy=False, mitad=True)}{_fc_fig('giro-eliminador', lazy=False, mitad=True)}</div></div>
      <div class="lab-split lab-fc-intro">
        <div class="lab-text">
          <p>¿Cómo llevar un producto de una línea industrial al contexto doméstico, aumentando su valor percibido y conectándolo con las necesidades de un nuevo consumidor?</p>
          <p>Ese fue el desafío detrás de Fuchi Chao. La oportunidad estaba en transformar una solución funcional en una marca cercana, capaz de conectar con el mundo de los petlovers. Así nació una propuesta que deja de hablar únicamente de las propiedades del producto para conectar con algo más cotidiano: la convivencia, el cuidado y el bienestar de quienes comparten su vida con mascotas.</p>
        </div>
        {_fc_fig('tenencia')}
      </div>
      {_fc_fig('paleta', 'lab-fc-85')}
      {_fc_fig('linea', 'lab-fc-76 lab-fc-izq')}
      {_fc_fig('manual', 'lab-fc-76 lab-fc-der')}
      {_fc_fig('simbolo')}
      {_fc_fig('logotipo')}
      <div class="lab-pair lab-pair-tp lab-pair-tp-c">{_fc_fig('post', mitad=True)}{_fc_fig('afiche', mitad=True)}</div>
      {_fc_fig('niveles')}
      {_fc_fig('redes')}
      <div class="lab-pair lab-pair-tp lab-fc-par-a">{_fc_fig('etiqueta', mitad=True)}{_fc_fig('personajes', mitad=True)}</div>
      <div class="lab-pair lab-pair-tp lab-fc-par-b">{_fc_fig('giro-jabon', mitad=True)}{_fc_fig('giro-detergente', mitad=True)}</div>
    </article>
'''

_fc_desc = 'Caso de estudio: naming, identidad, etiquetas y estrategia de marca de Fuchi Chao, la línea de productos para mascotas de Citrex.'
page('proyectos/fuchi-chao.html', 'Fuchi Chao: naming, identidad y estrategia de marca para productos de mascotas · Luis Vicencio',
     _fc_desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'],
     **case_seo(_fc, _fc_desc), body=_fc_body + case_nav(_fc))
