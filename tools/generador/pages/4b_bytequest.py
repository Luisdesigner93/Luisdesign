# Caso Bytequest (2025 – 2026): marca de la empresa y liderazgo de producto de tres soluciones con IA.
# Texto de tools/narrativa/01-narrativa-y-casos.md ("Caso redactado: Bytequest").
# No se nombra a la institución de justicia ni al cliente de emergencias, ni el nombre interno del asistente.
_bq = next(pr for pr in PROJECTS if pr['slug'] == 'bytequest')
case_page(_bq, 'Bytequest: marca y liderazgo de producto para soluciones de IA · Luis Vicencio',
    'Caso de estudio: la marca de Bytequest y el liderazgo de producto de Legisnova, un auditor de llamadas con IA y un asistente virtual multiagente.',
    _bq['summary'],
    'Bytequest: <strong>marca y liderazgo de producto</strong> para soluciones de IA.', [
    ('contexto', 'Contexto y <strong>desafío</strong>',
     '<p class="lead">Bytequest desarrolla software a la medida para organizaciones con procesos complejos y alta exigencia de calidad. El desafío era doble: entregar productos confiables integrándose a la lógica de cada cliente, y darle a la empresa y a sus nuevas soluciones una identidad clara.</p>'),
    ('marca', 'La <strong>marca</strong>',
     # EDITAR: revisar que la frase sobre "la célula" refleje la intención de Luis
     '<p class="lead">Creé la marca de Bytequest: estrategia, logotipo, identidad visual y sitio web (<a href="https://bytequest.cl" rel="noopener noreferrer" target="_blank">bytequest.cl<span class="sr-only"> (se abre en una pestaña nueva)</span></a>).</p>'
     '<p>La estrategia posiciona a la empresa como especialistas en IA aplicada a problemas reales, con una voz ambiciosa y cercana que juega con su nombre: «Descubre el byte que convierte tus procesos en oportunidades y tu empresa en leyenda». La idea de Bytequest como «la célula que hackea el potencial de tu negocio» ordenó también la forma de trabajar: equipos especializados que se integran a la operación de cada cliente. Esa definición sirvió como norte para presentar a la empresa y su catálogo de soluciones, desde el auditor de atención con IA hasta los multiagentes conversacionales.</p>'),
    ('productos', 'Los <strong>productos</strong>',
     '<ul><li><strong>Legisnova:</strong> plataforma que reúne la agenda legislativa del Congreso en un solo lugar. Traduje la forma de trabajar de parlamentarios, equipos y periodistas en historias de usuario, propuse los planes Parlamentario e Independiente, aseguré con QA que cada historia cumpliera lo esperado y diseñé y construí con IA el sitio de inscripción y la plataforma interna. Hoy está en etapa de pruebas.</li>'
     '<li><strong>Auditor de llamadas:</strong> para un servicio privado de emergencias que auditaba sus llamadas una por una. Coordiné la célula de IA dentro del equipo del cliente hasta un prototipo que transcribe, analiza y reporta llamadas según el protocolo.</li>'
     '<li><strong>Asistente virtual multiagente:</strong> para una institución pública del sistema de justicia, un asistente que responde consultas, informa el estado de causas y orienta los siguientes pasos, como alternativa a la atención presencial. Planifiqué el producto y gestioné las expectativas del cliente.</li></ul>'),
    ('como', 'Cómo <strong>trabajé</strong>',
     '<p class="lead">Fui el puente entre el negocio, el cliente y el equipo técnico: comprensión del negocio, historias de usuario, planificación por etapas con Scrum, QA de cada entrega y coordinación de células de IA, incluso dentro de equipos de desarrollo de los propios clientes.</p>'),
    ('resultado', '<strong>Resultado</strong>',
     # EDITAR (opcional): una frase de la dirección de Bytequest sobre el aporte de Luis
     '<p class="lead">Una marca con identidad propia y tres productos de IA llevados desde una idea difusa hasta prototipos funcionales y una plataforma en pruebas, con expectativas claras para cada cliente.</p>'),
    ('aprendizaje', 'Lo que <strong>me llevé</strong>',
     '<p class="lead">Aprendí a reconocer las alertas tempranas de un proyecto: prioridades difusas, decisiones sin responsable claro y expectativas sin acordar. Hoy las reviso desde el primer día.</p>'),
    ],
    facts=[('Rol', _bq['role']), ('Período', _bq['year']), ('Equipo', 'Hasta 7 personas'), ('Metodología', 'Scrum y discovery'), ('Estado', _bq['status'])],
    cta_title='¿Tu proyecto de software necesita <strong>un Product Owner</strong>?',
    cta_lead='Ordenemos prioridades, coordinemos al equipo y aseguremos la calidad de cada entrega.')
