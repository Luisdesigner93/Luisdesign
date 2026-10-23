# Caso Yomecontrolo (2023 – 2024): estrategia, experiencia y expresión de marca, nueva identidad y UX/UI de la web app del MVP.
# Fuente: documentos de research, Brand Compass, experiencia de marca y visión creativa entregados por Luis.
_ym = next(pr for pr in PROJECTS if pr['slug'] == 'yomecontrolo')
_ym_desc = 'Caso de estudio: estrategia de marca, nueva identidad y UX/UI del MVP de Yomecontrolo, una startup chilena de salud preventiva.'
page('proyectos/yomecontrolo.html', 'Yomecontrolo: estrategia de marca, identidad y UX/UI para una startup de salud · Luis Vicencio',
     _ym_desc, current='proyectos', ogtype='article', **case_seo(_ym, _ym_desc),
     cta_title='¿Tu producto digital necesita <strong>una marca que conecte</strong>?',
     cta_lead='Conversemos sobre tu proyecto y definamos juntos la estrategia, la identidad y la experiencia.',
     body=case_intro(_ym, _ym['summary'],
        case_facts(_ym))
     + case_detail('Yomecontrolo: <strong>vivir más y mejor</strong>.', [
        ('contexto', 'Contexto y <strong>desafío</strong>',
         '<p class="lead">Yomecontrolo es una startup tecnológica chilena del área de la salud. Ofrece packs de exámenes preventivos, emite órdenes médicas y categoriza a cada paciente según su perfil de riesgo, con una meta clara: ayudar a las personas a vivir más y mejor.</p>'
         '<p>En Chile la salud es reactiva: las enfermedades se descubren tarde y muchas personas no terminan sus tratamientos. A eso se sumaban dos problemas de marca: el público la confundía con su competencia directa y todavía no lograba conectar con sus usuarios.</p>'
         '<p>El desafío fue separar la marca del peso negativo de ir al médico y convertir el autocuidado en algo amable y cercano.</p>'),
        ('metodologia', 'La <strong>metodología</strong>',
         '<p class="lead">Un proceso de branding por etapas, del descubrimiento a los puntos de contacto, en el que cada fase alimenta a la siguiente.</p>'
         + case_steps([('Research', 'Investigación de escritorio que cruzó marca, categoría, usuarios y tendencias, como la medicina predictiva, la telemedicina y los wearables, para encontrar oportunidades.'),
                       ('Estrategia', 'Con un Brand Compass, una herramienta para definir el norte de la marca, fijamos su propósito, diferencial, personalidad y promesa. El público principal: adultos de 30 a 50 años que gestionan la salud de su familia.'),
                       ('Experiencia de marca', 'Con diseño especulativo imaginamos cómo sería cuidarse en el futuro, para diseñar hoy la experiencia que lleva hacia allá; con diseño de servicios trazamos el viaje del usuario por cada punto de contacto.'),
                       # EDITAR (revisar): media línea propuesta para explicar «territorio de marca»
                       ('Visión creativa', 'Concepto, idea central y territorio de marca, es decir, el espacio propio desde donde la marca habla: la narrativa que guía la expresión antes de diseñar.'),
                       ('Identidad', 'Construcción de la nueva identidad visual a partir de esa narrativa.'),
                       ('Puntos de contacto', 'Diseño UX/UI de la web app del MVP de 2024: solicitud de exámenes en línea y medición del riesgo cardiovascular.')])),
        ('solucion', 'La <strong>solución</strong>',
         '<p class="lead">Una marca que funciona como un asistente clínico: acompaña el cuidado personal y familiar mucho antes de que llegue la enfermedad.</p>'
         '<p>Su propósito, «superar las barreras de la salud y empoderar a las personas», y una personalidad inteligente, confiable y empática se resumieron en una idea central: «Yo me controlo, hoy por un mejor mañana». A partir de ella diseñé la nueva identidad y la experiencia del MVP.</p>'
         '<ul><li>Nueva identidad visual, con el tagline «vivir más y mejor».</li>'
         '<li>Web app para solicitar exámenes preventivos en línea y medir el riesgo cardiovascular con la calculadora de edad del corazón.</li></ul>'),
        ('resultado', '<strong>Resultado</strong>',
         '<p class="lead">La nueva marca sigue en uso hasta hoy. El MVP diseñado (solicitud de exámenes en línea y calculadora de riesgo cardiovascular) no llegó a producción porque la empresa tomó otra dirección de producto, pero la estrategia, el propósito y la identidad siguen guiando su comunicación.</p>'),
        # EDITAR: testimonio de los fundadores (opcional)
        ('aprendizaje', 'Lo que <strong>me llevé</strong>',
         '<p class="lead">Este proyecto me mostró que una buena estrategia de marca necesita herramientas de producto para llegar a producción. Por eso me formé en Product Owner y Scrum, y hoy acompaño las dos etapas.</p>'),
     ]) + case_landing(_ym) + case_nav(_ym))
