# Piloto (piloto.html, noindex, sin enlace en el menú): identidad con una línea continua que nace de la firma "luis"
# del logo y recorre el sitio (referencia: dakshgajjar.com). Textos entregados por Luis el 2026-10-27, con correcciones de forma.
# Cada sección tiene su tramo de línea: un SVG que ocupa la sección (viewBox de escritorio y de móvil, estirado sin
# deformar el grosor) y que se dibuja con el scroll (css/piloto.css). Los tramos se unen al centro, en el borde de cada sección.
# La línea es de color destacador (verde amarillo flúor, --pl-line en css/piloto.css).

# Trazo de la firma "luis" (la "i" va sin punto, por diseño) sobre el logo cuadrado (img/marca/logo-luy-cuadrado.png, 560 × 560):
# en el orden del boceto de Luis: la l baja; u, u, i son lazos angostos (sube en diagonal hasta la punta y baja casi vertical);
# la s baja, hace el lazo bajo la línea base y la cola cruza hacia arriba a la derecha (viewBox 55 55 480 420). Grosor: el de la línea, --pl-stroke en css/piloto.css.
_FIRMA = ('M160 78 L152 90 L141 110 L132 130 L123 150 L115 170 L108 190 L102 210 L97 230 L93 250 L89 270 L86 290 L84 310 L82 330 L82 350 L82 372 L84 388 L90 393 L97 388 L108 368 L119 347 L130 326 L140 306 L151 286 L162 265 L173 244 L184 224 L188 214 L184 232 L180 250 L175 270 L172 290 L170 310 L170 330 L169 350 L169 372 L171 388 L177 393 L184 388 L194 368 L205 347 L216 326 L226 306 L236 286 L247 265 L258 244 L268 224 L272 214 L269 232 L265 250 L260 270 L257 290 L255 310 L255 330 L254 350 L254 372 L256 388 L262 393 L269 388 L280 368 L290 347 L300 326 L311 306 L322 286 L332 265 L342 244 L353 224 L357 214 L353 232 L349 250 L344 270 L341 290 L339 310 L339 330 L338 350 L338 372 L340 388 L346 393 L353 388 L363 369 L373 349 L384 330 L394 311 L404 291 L414 272 L425 253 L435 233 L445 214 L449 203 L443 222 L439 240 L435 260 L432 280 L431 300 L430 330 L430 360 L431 385 L433 405 L434 428 L428 445 L414 452 L400 446 L393 432 L397 418 L410 405 L431 390 L456 371 L470 361 L484 350 L499 340 L509 333')


def _hilo(desk, mob, cls='', extra=''):
    """Tramo de línea de una sección: un SVG para escritorio (1440 × 1000) y otro para móvil (375 × 1000)."""
    def svg(view, paths, media):
        return (f'<svg class="pl-thread pl-thread-{media} {cls}" viewBox="{view}" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
                + ''.join(f'<path d="{d}" pathLength="1" vector-effect="non-scaling-stroke"/>' for d in paths) + extra + '</svg>')
    return svg('0 0 1440 1000', desk, 'desk') + svg('0 0 375 1000', mob, 'mob')


_arrow = '<svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg>'

# 1. HERO (oscuro): la línea entra desde arriba y se entrelaza con el titular
# Sin firma: la línea entra arriba a la izquierda y hace un lazo grande antes del titular (boceto de Luis),
# baja por el borde izquierdo, pasa bajo "QUE" y cruza el titular con tres lazos angostos (como la u y la i del logo);
# luego rodea el final de "DESEAN" con otro lazo, cierra con un lazo como el de la s y la cola sale al centro.
# Se dibuja con el scroll y una punta redondeada marca el avance (js/main.js, initPilotThread).
_hero_desk = ('M170 0 C130 60 60 120 52 210 C45 290 40 360 70 410 C110 470 250 450 300 380 C340 320 300 255 230 262 '
              'C150 270 90 340 75 430 C60 520 50 600 60 680 C70 760 200 790 300 760 C340 748 360 760 375 740 '
              'C410 640 470 460 500 360 C512 322 518 330 508 380 C495 470 480 620 490 720 C496 790 545 800 570 740 '
              'C605 640 665 460 695 360 C707 322 713 330 703 380 C690 470 675 620 685 720 C691 790 740 800 765 740 '
              'C800 640 860 460 890 360 C902 322 908 330 898 380 C888 450 880 540 880 600 C880 640 960 560 1040 600 '
              'C1090 630 1070 710 990 712 C920 714 885 680 885 740 C885 800 880 860 850 860 C815 860 815 810 850 800 '
              'C960 775 1110 760 1150 840 C1190 930 1000 960 860 965 C790 968 720 970 720 1000')
# En móvil los lazos terminan bajo el titular y la línea baja por el borde derecho, sin tapar la bajada
_hero_mob = ('M50 0 C40 70 20 140 30 200 C40 260 160 250 155 190 C150 130 60 160 55 250 C50 330 80 360 80 420 C80 480 86 560 96 640 C102 700 126 720 145 670 C160 630 178 560 190 520 '
             'C196 500 196 510 190 540 C182 590 178 650 184 700 C190 750 215 760 232 710 C246 670 262 600 272 560 '
             'C278 540 278 550 272 580 C264 630 262 690 270 740 C276 780 300 790 330 770 C362 750 368 800 364 860 '
             'C358 930 250 935 200 955 C190 965 187.5 985 187.5 1000')
PILOTO_HERO = f'''
    <!-- PILOTO · HERO -->
    <section class="pl-sec pl-dark pl-hero" aria-labelledby="pl-hero-title">
      {_hilo([_hero_desk], [_hero_mob], 'pl-thread-back')}
      <div class="pl-inner">
        <h1 class="pl-display" id="pl-hero-title">Diseño marcas que desean moverse</h1>
        <p class="pl-lead">Soy un diseñador de productos digitales construyendo estrategias, identidad y experiencias en torno a tu servicio.</p>
      </div>
      {_hilo([_hero_desk], [_hero_mob], 'pl-thread-front')}
      <span class="pl-head" aria-hidden="true"></span>
      <p class="pl-hint" aria-hidden="true">Sigue la línea</p>
    </section>
'''

# 2. EL MUNDO DE LAS IDEAS (claro): el collage actual; la línea pasa por detrás de los productos
_ideas = HOME_IDEAS
_ini = _ideas.index('          <p>Una idea vale'); _fin = _ideas.index('          <a class="btn btn-outline ideas-cta"')
_ideas = _ideas[:_ini] + '          <p>Se trata de conectar tu marca con sus usuarios y su entorno para definir tendencias.</p>\n' + _ideas[_fin:]
_ideas = _ideas.replace('<section class="panel panel-plain ideas"', '<section class="panel panel-plain ideas pl-sec pl-ideas"', 1)
_ideas = _ideas.replace('      <div class="ideas-stage">', '      ' + _hilo(['M720 0 C720 160 560 240 620 400 C680 560 860 560 820 720 C780 860 720 900 720 1000'],
                                                                    ['M187.5 0 C187.5 140 120 220 150 380 C180 540 260 600 220 760 C200 860 187.5 900 187.5 1000']) + '\n      <div class="ideas-stage">', 1)
PILOTO_IDEAS = _ideas

# 3. SISTEMAS (claro): la línea se abre en un óvalo con un punto por disciplina (en móvil, dos columnas)
_disciplinas = ['Branding', 'Identidad', 'UX Research', 'Productos digitales', 'AI workflow', 'Colaboración']
_caps_desk = ['M720 0 V170 A440 330 0 0 1 720 830 V1000', 'M720 170 A440 330 0 0 0 720 830']
_caps_mob = ['M187.5 0 V330 C187.5 370 320 360 320 410 V860 C320 910 187.5 900 187.5 940 V1000',
             'M187.5 330 C187.5 370 55 360 55 410 V860 C55 910 187.5 900 187.5 940']
PILOTO_SISTEMAS = f'''
    <!-- PILOTO · SISTEMAS -->
    <section class="pl-sec pl-light pl-caps" aria-labelledby="pl-caps-title">
      {_hilo(_caps_desk, _caps_mob)}
      <h2 class="pl-title pl-caps-title" id="pl-caps-title">Diseño sistemas que identifican y reducen la brecha que separa a tu negocio de tu público.</h2>
      <ul class="pl-caps-list" role="list">''' + ''.join(f'''
        <li class="pl-cap pl-cap-{i}"><span class="pl-dot" aria-hidden="true"></span>{d}</li>''' for i, d in enumerate(_disciplinas, 1)) + '''
      </ul>
    </section>
'''

# 4. PORTAFOLIO (claro): el carrusel actual; la línea baja por el costado y vuelve al centro
PILOTO_PORTAFOLIO = f'''
    <!-- PILOTO · PORTAFOLIO -->
    <section class="pl-sec pl-light more pl-folio" id="proyectos" aria-labelledby="pl-folio-title">
      {_hilo(['M720 0 C720 90 1290 60 1290 220 C1290 420 980 560 980 760 C980 900 720 880 720 1000'],
             ['M187.5 0 C187.5 60 345 60 345 160 V820 C345 920 187.5 900 187.5 1000'])}
      <h2 class="pl-display pl-folio-title" id="pl-folio-title">Portafolio</h2>
      <div class="more-stage">
        <div class="more-nav" hidden>
          <button class="more-prev" type="button" aria-label="Proyecto anterior">{_arrow}</button>
          <button class="more-next" type="button" aria-label="Proyecto siguiente">{_arrow}</button>
        </div>
        <ul class="more-arc" aria-label="Proyectos">{_more_arc}
        </ul>
      </div>
      <div class="pl-inner pl-center"><a class="btn btn-primary" href="proyectos.html">Ver todos los proyectos {_arrow}</a></div>
    </section>
'''

# 5. MARCA Y PRODUCTO (oscuro): la línea se vuelve ortogonal, con esquinas redondeadas (lenguaje de sistema)
PILOTO_PRODUCTO = f'''
    <!-- PILOTO · MARCA Y PRODUCTO -->
    <section class="pl-sec pl-dark pl-producto" aria-labelledby="pl-producto-title">
      {_hilo(['M720 0 V110 Q720 150 760 150 H1290 Q1330 150 1330 190 V810 Q1330 850 1290 850 H760 Q720 850 720 890 V1000'],
             ['M187.5 0 V60 Q187.5 90 217.5 90 H325 Q355 90 355 120 V880 Q355 910 325 910 H217.5 Q187.5 910 187.5 940 V1000'])}
      <div class="pl-inner">
        <h2 class="pl-title" id="pl-producto-title">Marca y producto en la misma dirección</h2>
        <p class="pl-lead">Product Owner y estratega de marca para pymes y startups. Me sumo a tu equipo para que lo que construyes tenga un norte claro, prioridades ordenadas y entregas que cumplan lo esperado.</p>
      </div>
    </section>
'''

# 6. LUIS VICENCIO (claro): la línea vuelve a escribir la firma
PILOTO_FIRMA = f'''
    <!-- PILOTO · FIRMA -->
    <section class="pl-sec pl-light pl-sign" aria-labelledby="pl-sign-title">
      {_hilo(['M720 0 C720 80 600 110 561 184', 'M972 504 C1060 560 1120 700 1040 860 C980 960 720 920 720 1000'],
             ['M187.5 0 C187.5 80 130 120 120 209', 'M295 456 C350 520 360 700 300 860 C260 940 187.5 930 187.5 1000'])}
      <svg class="pl-firma pl-firma-grande" viewBox="55 55 480 420" aria-hidden="true" focusable="false"><path d="{_FIRMA}" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
      <div class="pl-inner pl-center">
        <h2 class="pl-title" id="pl-sign-title">Luis Vicencio</h2>
        <p class="pl-mono">Diseñador digital.</p>
      </div>
    </section>
'''

# 7. CONTACTO (oscuro): la línea llega y empieza a moverse (una onda continua)
_onda = 'M0 50 ' + ' '.join(f'C{x + 45} 10 {x + 75} 90 {x + 120} 50' for x in range(0, 2880, 120))
PILOTO_CONTACTO = f'''
    <!-- PILOTO · CONTACTO -->
    <section class="pl-sec pl-dark pl-contact" id="contacto" aria-labelledby="pl-contact-title">
      {_hilo(['M720 0 V420'], ['M187.5 0 V380'])}
      <div class="pl-wave" aria-hidden="true"><svg viewBox="0 0 2880 100" preserveAspectRatio="none" focusable="false"><path d="{_onda}" vector-effect="non-scaling-stroke"/></svg></div>
      <div class="pl-inner pl-center">
        <h2 class="pl-display" id="pl-contact-title">¿Quieres dar movimiento a tu marca?</h2>
        <a class="btn btn-primary v2-btn-light" href="{WA_MARCAS}" rel="noopener noreferrer" target="_blank">Hablemos<span class="sr-only"> (WhatsApp, se abre en una pestaña nueva)</span> {_arrow}</a>
      </div>
    </section>
'''

# 8. BLOG (claro): EDITAR: artículos pendientes
PILOTO_BLOG = '''
    <!-- PILOTO · BLOG -->
    <section class="pl-sec pl-light pl-blog" id="blog" aria-labelledby="pl-blog-title">
      <div class="pl-inner">
        <h2 class="pl-title" id="pl-blog-title">Blog</h2>
        <p class="pl-lead">Información que puede ser de utilidad para tu negocio o para que me conozcas.</p>
        <!-- EDITAR: reemplazar por los artículos reales (título, bajada, fecha y enlace) -->
        <ul class="pl-blog-list" role="list">''' + ''.join('''
          <li class="card pl-post"><p class="pl-mono">Próximamente</p><p class="pl-post-title">Artículo pendiente</p></li>''' for _ in range(3)) + '''
        </ul>
      </div>
    </section>
'''

page('piloto.html', 'Piloto · Luis Vicencio', 'Prueba de identidad con una línea en movimiento.',
     noindex=True, contact=False, html_class='home motion v2 piloto', extra_css=['css/home-v2.css', 'css/piloto.css'],
     body=PILOTO_HERO + PILOTO_IDEAS + PILOTO_SISTEMAS + PILOTO_PORTAFOLIO + PILOTO_PRODUCTO + PILOTO_FIRMA
     + PILOTO_CONTACTO + PILOTO_BLOG + HOME_PREGUNTAS)
