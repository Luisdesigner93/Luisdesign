_aw = dict(PROJECTS[0], placeholders=('Inicio de AuditorWeb con el analizador y la cuenta regresiva a la entrada en vigencia.',
                                      'Informe: puntaje general y resultado por área.',
                                      'Plan de acción priorizado y detalle de cada control.'))
page('proyectos/auditorweb.html', 'AuditorWeb 21.719 · Caso · Luis Vicencio',
     'Caso de estudio: AuditorWeb 21.719, un auditor automatizado de cumplimiento con la Ley de Protección de Datos Personales de Chile.',
     current='proyectos', ogtype='article',
     cta_title='¿Quieres saber cómo está <strong>tu sitio</strong>?',
     cta_lead='Te ayudo a interpretar el informe y a corregir las brechas, desde la política de privacidad hasta las cabeceras de seguridad.',
     body=case_intro(_aw,
        'Una herramienta gratuita que analiza cualquier sitio web y muestra, en segundos, qué tan preparado está para la nueva Ley de Protección de Datos Personales de Chile.',
        [('Tipo', 'Producto propio'), ('Año', '2026'), ('Rol', 'Producto, UX/UI y desarrollo asistido con IA')],
        # EDITAR: confirmar la URL pública del auditor
        '\n          <a class="btn btn-primary case-action" href="https://auditorweb.luisdesign.cl" rel="noopener">Probar AuditorWeb <svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-external"/></svg></a>')
     + case_detail('AuditorWeb: <strong>la Ley 21.719</strong> convertida en un informe accionable.', [
        ('contexto', 'Contexto y <strong>desafío</strong>',
         '<p class="lead">La Ley 21.719 rige desde el 1 de diciembre de 2026 y aplica a toda organización que trate datos de personas en Chile. La mayoría de las empresas no sabe por dónde empezar.</p>'
         '<p>El sitio web suele ser el primer punto de recolección de datos: formularios, cookies, analítica, chat. Revisarlo a mano exige conocer la ley y saber leer cabeceras HTTP, scripts de terceros y políticas de privacidad.</p>'
         '<p>El desafío fue traducir ese conocimiento en una revisión automática, comprensible para personas no técnicas y útil a la vez para los equipos que deben corregir las brechas.</p>'),
        ('rol', 'Mi <strong>rol</strong>',
         '<p>Lideré el producto de punta a punta: desde la definición de qué revisar hasta el diseño del informe y la construcción, apoyándome en herramientas de inteligencia artificial para el desarrollo.</p>'
         + case_rows([('Producto', 'Discovery de las obligaciones de la ley y priorización de los controles con mayor impacto.'),
                      ('UX/UI', 'Diseño de la experiencia, del informe y de la identidad visual de la herramienta.'),
                      ('Desarrollo y QA', 'Construcción asistida con IA, pruebas unitarias y revisión de seguridad.')])),
        ('proceso', 'El <strong>proceso</strong>',
         '<p class="lead">De un texto legal a 30 controles que una máquina puede verificar.</p>'
         + case_steps([('Discovery', 'Análisis de la ley y de las obligaciones que se pueden observar desde el exterior de un sitio.'),
                       ('Definición', '30 controles en 5 áreas, cada uno con su artículo de referencia, su peso y su recomendación.'),
                       ('Diseño', 'Un informe con puntaje, semáforo por área y plan de acción ordenado por impacto.'),
                       ('Desarrollo y QA', 'Construcción con Node.js, pruebas unitarias y revisión de seguridad antes del lanzamiento.')])),
        ('solucion', 'La <strong>solución</strong>',
         '<p class="lead">Se ingresa una URL y se obtiene un informe con puntaje de 0 a 100, resultado por área y un plan de acción priorizado.</p>'
         '<p>Cada control muestra la evidencia encontrada y una recomendación concreta, para que tanto la gerencia como el equipo técnico sepan qué hacer. El informe se puede exportar a PDF.</p>'
         '<ul><li>Descarga segura de los sitios, con protección contra SSRF y límites de tiempo y tamaño.</li>'
         '<li>Informe construido sin insertar HTML de terceros y con una política de seguridad de contenidos estricta.</li>'
         '<li>No se registran las URLs analizadas, no se usan cookies de seguimiento y la tipografía es autoalojada.</li></ul>'),
        ('resultados', 'Resultados y <strong>aprendizajes</strong>',
         '<p class="lead">Una herramienta que evalúa privacidad y seguridad tenía que ser, ella misma, un buen ejemplo.</p>'
         + case_stats([('30', 'controles automáticos, cada uno vinculado a una obligación de la ley.'),
                       ('5', 'áreas: transparencia, derechos, consentimiento y cookies, seguridad y terceros.'),
                       ('0', 'cookies de seguimiento. El auditor cumple lo que revisa.')])
         + case_quote('La mejor forma de explicar una ley compleja es mostrarle a cada empresa qué le falta a su propio sitio.', 'Aprendizaje del proyecto')),
     ]) + case_nav(PROJECTS[0]))
