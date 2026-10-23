# Caso Fuchi Chao para Citrex, en dos etapas: nacer con una marca (2021) y crecer con un propósito (2023).
# Texto de tools/narrativa/01-narrativa-y-casos.md ("Caso Fuchi Chao reescrito en dos etapas").
# EDITAR (opcional): capturas de petlovers o influencers con permiso, un dato (tiendas, seguidores) y una frase de las fundadoras de Citrex
_fc = next(pr for pr in PROJECTS if pr['slug'] == 'fuchi-chao')
case_page(_fc, 'Fuchi Chao: naming, identidad y estrategia de marca para productos de mascotas · Luis Vicencio',
    'Caso de estudio: naming, identidad, etiquetas y estrategia de marca de Fuchi Chao, la línea de productos para mascotas de Citrex.',
    _fc['summary'],
    'Fuchi Chao: todo el cariño por tu mascota, <strong>sin la parte fuchi</strong>.', [
    ('nacer', 'Nacer con <strong>una marca</strong> (2021)',
     '<p class="lead">Citrex quería llevar su experiencia en eliminación de olores al mundo de las mascotas. Creé el nombre, el logotipo y las etiquetas: una marca cercana que habla como hablamos en Chile, donde «fuchi» es la forma tierna de decir que algo huele mal.</p>'),
    ('crecer', 'Crecer con <strong>un propósito</strong> (2023)',
     '<p class="lead">La marca estaba en el mercado, pero no había claridad sobre qué la movía ni cómo comunicarlo. Con un Brand Compass definimos su propósito, el norte de la marca, y a su comunidad.</p>'
     '<p>Con eso, el mensaje dejó de ser «cómprame» y pasó a ser una invitación: «vamos hacia allá, ¿vienes con nosotros?». El propósito: una tenencia feliz, libre de malos olores.</p>'),
    ('resultado', '<strong>Resultado</strong>',
     '<p class="lead">Después de la estrategia creció la comunidad. Fuchi Chao se vende en tiendas veterinarias, plataformas en línea y redes sociales, es un éxito en las exposiciones de mascotas, y petlovers e influencers se sumaron a contar su historia.</p>'),
    ],
    cta_title='¿Tu producto necesita <strong>una marca propia</strong>?',
    cta_lead='Conversemos sobre tu idea y definamos juntos el nombre, la identidad y el packaging.')
