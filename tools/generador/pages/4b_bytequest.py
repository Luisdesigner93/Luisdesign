_bq = next(pr for pr in PROJECTS if pr['slug'] == 'bytequest')
page('proyectos/bytequest.html', 'Bytequest · Caso · Luis Vicencio',
     'Caso de estudio: liderazgo de innovación y productos en Bytequest, como Product Owner y Brand Manager.',
     current='proyectos', ogtype='article',
     cta_title='¿Tu proyecto de software necesita <strong>un Product Owner</strong>?',
     cta_lead='Ordenemos prioridades, coordinemos al equipo y aseguremos la calidad de cada entrega.',
     # Contenido basado en el CV. EDITAR: agregar imágenes y validar qué se puede mostrar de cada producto
     body=case_intro(_bq,
        'Como Líder de Innovación y Productos, combiné la gestión de producto con Scrum y el desarrollo de marca para impulsar soluciones de software para el sector público y privado.',
        [('Rol', 'Product Owner y Brand Manager'), ('Período', '2025 – 2026'), ('Equipo', 'Hasta 7 personas'), ('Metodología', 'Scrum y discovery')])
     + case_detail('Bytequest: <strong>innovación y productos</strong> con mirada de negocio.', [
        ('contexto', 'Contexto y <strong>desafío</strong>',
         '<p class="lead">Bytequest desarrolla software a la medida para organizaciones con procesos complejos y alta exigencia de calidad.</p>'
         '<p>El desafío era doble: entregar productos confiables a clientes institucionales, integrándose a sus equipos y a su lógica de trabajo, y al mismo tiempo dar forma a nuevas propuestas tecnológicas con una identidad clara y un posicionamiento diferenciado.</p>'),
        ('rol', 'Mi <strong>rol</strong>',
         '<p>Fui el puente entre el negocio, el cliente y el equipo técnico: definí prioridades, aseguré la calidad de lo entregado y le di identidad a los nuevos productos.</p>'
         + case_rows([('Product Owner', 'Gestión del backlog, prioridades y alcance con el equipo técnico y el cliente, bajo Scrum.'),
                      ('Coordinación de equipos', 'Lideré un equipo de 7 personas y ajusté la metodología para mejorar el rendimiento de un equipo recién formado.'),
                      ('QA e informes', 'Control de calidad de los entregables e informes mensuales de avance para el cliente y los stakeholders internos.'),
                      ('Brand Manager', 'Identidades de marca construidas con research y discovery, para detectar brechas de posicionamiento antes del MVP.')])),
        ('proceso', 'El <strong>proceso</strong>',
         '<p class="lead">Discovery para decidir qué construir, Scrum para construirlo bien.</p>'
         + case_steps([('Discovery', 'Validación de las necesidades del negocio y de los usuarios con el cliente.'),
                       ('Backlog', 'Expectativas, alcance y prioridades acordadas con el equipo técnico y el cliente.'),
                       ('Sprints', 'Desarrollo iterativo con Scrum, adaptado al ritmo y la madurez del equipo.'),
                       ('QA y reporte', 'Revisión de cada entregable e informe mensual de avance.')])),
        ('solucion', 'Los <strong>productos</strong>',
         '<p class="lead">Un módulo de inteligencia artificial para la atención de víctimas por chatbot, con auditoría y observabilidad de la atención en call center, para una institución pública del sector justicia.</p>'
         '<p>Para este cliente nos integramos a la lógica de trabajo de una célula especializada. En paralelo impulsé el desarrollo de otros productos de software:</p>'
         '<ul><li>Una solución de uso legislativo.</li><li>Una plataforma de gestión de crisis para municipalidades.</li><li>Una herramienta de excelencia operacional con estructura de datos en grafos.</li></ul>'),
        ('resultados', 'Resultados y <strong>aprendizajes</strong>',
         case_stats([('7', 'personas coordinadas en el desarrollo de una propuesta tecnológica.'),
                     ('4', 'líneas de producto impulsadas: IA para atención, legislativo, gestión de crisis y excelencia operacional.'),
                     ('1', 'informe de avance mensual para el cliente y los stakeholders internos.')])),
     ]) + case_nav(_bq))
