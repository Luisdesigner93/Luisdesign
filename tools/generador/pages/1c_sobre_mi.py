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
     current='sobre', extra_css='css/home-v2.css', body=f'''    <section class="hero-shell" aria-labelledby="page-title">
      <div class="shell-body frame-grid page-hero">
        <div class="container">
          <ol class="breadcrumb" aria-label="Ruta"><li><a href="./">Inicio</a></li><li aria-current="page">Sobre mí</li></ol>
          <span class="tag tag-eyebrow">Sobre mí</span>
          <h1 class="display" id="page-title">Llevo el mundo de las ideas <strong>a los productos del día a día</strong>.</h1>
        </div>
      </div>
    </section>

    <!-- HISTORIA -->
    <section class="panel panel-plain section about" aria-labelledby="historia-title">
      <div class="container">
        <div class="two-col about-grid">
          <!-- EDITAR: reemplazar por un retrato trabajando, no de estudio (opcional: video de 60 segundos) -->
          <figure class="portrait">
            <img src="img/marca/luis-vicencio-retrato.png" width="750" height="900" alt="Retrato de Luis Vicencio" loading="lazy" decoding="async">
          </figure>
          <div class="about-text">
            <h2 class="heading" id="historia-title">De la marca al producto, <strong>proyecto a proyecto</strong>.</h2>
            <p>Soy Luis Vicencio, diseñador de la Universidad de Valparaíso, con estudios de Product Design for Innovation en el Politecnico di Milano, un diplomado en Branding Estratégico y formación en Product Owner y Scrum.</p>
            <p>Cada proyecto me dejó una herramienta nueva: empecé diseñando identidades, sumé la estrategia de marca y hoy también lidero productos digitales. Me mueve ayudar a que las empresas crezcan, que su marca se viva por dentro y por fuera, y hacerlo en colaboración con otros creadores y con los propios clientes.</p>
            <p>En Yomecontrolo aprendí que una buena estrategia de marca necesita herramientas de producto para llegar a producción. Hoy acompaño las dos etapas: le doy un norte al producto y lo llevo paso a paso, entregable a entregable, hasta que cada entrega cumple lo esperado.</p>
            <!-- EDITAR: sumar el botón "Descargar CV" (btn btn-primary con download) cuando Luis entregue el PDF -->
            <div class="about-links">
              <a class="link-arrow" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank">LinkedIn<span class="sr-only"> (se abre en una pestaña nueva)</span> {_arrow}</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- LO QUE ME LLEVÉ -->
    <section class="panel section" aria-labelledby="aprendizajes-title">
      <div class="container">
        <div class="section-head center">
          <span class="tag tag-eyebrow">Aprendizajes</span>
          <h2 class="heading" id="aprendizajes-title">Lo que <strong>me llevé</strong>.</h2>
        </div>''' + ''.join(f'''
        <figure class="pd-learned">
          <figcaption><a href="{href}">{name}</a></figcaption>
          <blockquote><p>{text}</p></blockquote>
        </figure>''' for name, href, text in _aprendizajes) + f'''
      </div>
    </section>

    <!-- TRAYECTORIA Y FORMACIÓN -->
    <section class="panel panel-plain section" id="trayectoria" aria-labelledby="trayectoria-title">
      <div class="container">
        <div class="narrow">
          <div class="section-head">
            <span class="tag tag-eyebrow">Trayectoria</span>
            <h2 class="heading" id="trayectoria-title">Más de 7 años entre <strong>marca, experiencia y producto</strong>.</h2>
          </div>
          {_career}
          <h2 class="heading about-subtitle" id="formacion-title">Formación</h2>
          {_formacion}
        </div>
      </div>
    </section>

    <!-- DOS LANDINGS -->
    <section class="panel section" aria-labelledby="caminos-title">
      <div class="container">
        <div class="section-head center">
          <h2 class="heading" id="caminos-title">¿Por dónde <strong>empezamos</strong>?</h2>
          <div class="btn-row">
            <a class="btn btn-primary" href="./">Marcas para pymes {_arrow}</a>
            <a class="btn btn-outline" href="producto-digital.html">Producto digital</a>
          </div>
        </div>
      </div>
    </section>
''')
