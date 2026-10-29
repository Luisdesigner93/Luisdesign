# Sobre mí (sobre-mi.html): historia completa, aprendizajes, trayectoria, formación y CV.
# Historia: versiones de tools/narrativa/02-landing-marcas.md y 03-landing-producto-digital.md, combinadas sin repetir frases.
# La trayectoria y la formación vienen del inicio (HOME_TRAYECTORIA en pages/1_index.py).
_career = HOME_TRAYECTORIA[HOME_TRAYECTORIA.index('<ol class="career">'):HOME_TRAYECTORIA.index('</ol>') + len('</ol>')]
_formacion = HOME_TRAYECTORIA[HOME_TRAYECTORIA.index('<div class="benefits">'):HOME_TRAYECTORIA.rindex('</div>\n        </div>')]
# EDITAR: nombre exacto del curso de Product Owner y Scrum en Coursera, institución que lo dicta y año (es un curso, no una certificación)
_formacion += '''  <div><strong>Product Owner y Scrum</strong><span>Curso en línea, Coursera.</span></div>
            </div>'''
_arrow = '<svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg>'

_aprendizajes = [
    ('Yomecontrolo', 'proyectos/yomecontrolo.html', 'Este proyecto me mostró que una buena estrategia de marca necesita herramientas de producto para llegar a producción. Por eso me formé en Product Owner y Scrum, y hoy acompaño las dos etapas.'),
    ('Bytequest', 'proyectos/bytequest.html', 'Aprendí a reconocer las alertas tempranas de un proyecto: prioridades difusas, decisiones sin responsable claro y expectativas sin acordar. Hoy las reviso desde el primer día.'),
]

page('sobre-mi.html', 'Sobre mí · Luis Vicencio, diseñador y Product Owner',
     'Luis Vicencio es diseñador y Product Owner en Chile, especializado en branding, diseño web, UX/UI y gestión de productos digitales con Scrum.',
     current='sobre', extra_css=['css/home-v2.css', 'css/inicio.css'], contact=False, html_class='motion inicio',
     jsonld=[person_ld(alumniOf=[{'@type': 'CollegeOrUniversity', 'name': n} for n in ('Universidad de Valparaíso', 'Politecnico di Milano', 'Universidad del Desarrollo')],
                       knowsAbout=['Branding', 'Identidad visual', 'Diseño web', 'UX/UI', 'Product Owner', 'Scrum'])],
     body=f'''    <!-- HISTORIA -->
    <section class="pl-sec pl-sobre pl-dark about" aria-labelledby="historia-title">
      <div class="pl-inner">
        <div class="two-col about-grid">
          <figure class="portrait">
            <img src="img/marca/luis-vicencio-retrato.png" width="750" height="900" alt="Retrato de Luis Vicencio" loading="lazy" decoding="async">
          </figure>
          <div class="about-text">
            <h2 class="pl-title" id="historia-title">De la marca al producto, <strong>proyecto a proyecto</strong>.</h2>
            <p class="pl-lead">Soy Luis Vicencio, diseñador de la Universidad de Valparaíso, con estudios de Product Design for Innovation en el Politecnico di Milano, un diplomado en Branding Estratégico y formación en Product Owner y Scrum.</p>
            <p class="pl-lead">Cada proyecto me dejó una herramienta nueva: empecé diseñando identidades, sumé la estrategia de marca y hoy también lidero productos digitales. Me mueve ayudar a que las empresas crezcan, que su marca se viva por dentro y por fuera, y hacerlo en colaboración con otros creadores y con los propios clientes.</p>
            <p class="pl-lead">En Yomecontrolo aprendí que una buena estrategia de marca necesita herramientas de producto para llegar a producción. Hoy acompaño las dos etapas: le doy un norte al producto y lo llevo paso a paso, entregable a entregable, hasta que cada entrega cumple lo esperado.</p>
            <!-- EDITAR: sumar el botón "Descargar CV" (btn btn-primary con download) cuando Luis entregue el PDF -->
            <div class="about-links">
              <a class="link-arrow" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank">LinkedIn<span class="sr-only"> (se abre en una pestaña nueva)</span> {_arrow}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- LO QUE ME LLEVÉ -->
    <section class="pl-sec pl-sobre pl-light" aria-labelledby="aprendizajes-title">
      <div class="pl-inner">
        <div class="section-head center">
          <p class="pl-mono">Aprendizajes</p>
          <h2 class="pl-title" id="aprendizajes-title">Lo que <strong>me llevé</strong>.</h2>
        </div>''' + ''.join(f'''
        <figure class="pd-learned">
          <figcaption><a href="{href}">{name}</a></figcaption>
          <blockquote><p>{text}</p></blockquote>
        </figure>''' for name, href, text in _aprendizajes) + f'''
      </div>
    </section>

    <!-- TRAYECTORIA Y FORMACIÓN -->
    <section class="pl-sec pl-sobre pl-light" id="trayectoria" aria-labelledby="trayectoria-title">
      <div class="pl-inner">
        <div class="narrow">
          <div class="section-head">
            <p class="pl-mono">Trayectoria</p>
            <h2 class="pl-title" id="trayectoria-title">Más de 7 años entre <strong>marca, experiencia y producto</strong>.</h2>
          </div>
          {_career}
          <h2 class="pl-title about-subtitle" id="formacion-title">Formación</h2>
          {_formacion}
        </div>
      </div>
    </section>

    <!-- CONTACTO (sin línea fluor) -->
    <section class="pl-sec pl-sobre pl-light pl-contact" id="contacto" aria-labelledby="contacto-title">
      <div class="pl-inner pl-center">
        <h2 class="pl-display" id="contacto-title">Tu próximo proyecto <strong>empieza acá</strong>.</h2>
        <p class="pl-lead">Cuéntame en qué etapa está tu marca o tu producto y te respondo con una propuesta de alcance, plazos y presupuesto.</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-chat"/></svg>Escríbeme por WhatsApp<span class="sr-only"> (se abre en una pestaña nueva)</span></a>
          <a class="btn btn-outline" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-user"/></svg>LinkedIn<span class="sr-only"> (se abre en una pestaña nueva)</span></a>
        </div>
      </div>
    </section>
''')
