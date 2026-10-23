# Caso Fuchi Chao (2021) para Citrex: naming, identidad y packaging para su nueva línea de productos para mascotas.
_fc = next(pr for pr in PROJECTS if pr['slug'] == 'fuchi-chao')
page('proyectos/fuchi-chao.html', 'Fuchi Chao · Caso · Luis Vicencio',
     'Caso de estudio: naming, identidad visual y packaging ecológico de Fuchi Chao, la línea de productos para mascotas de Citrex.',
     current='proyectos', ogtype='article',
     cta_title='¿Tu producto necesita <strong>una marca propia</strong>?',
     cta_lead='Conversemos sobre tu idea y definamos juntos el nombre, la identidad y el packaging.',
     body=case_intro(_fc, _fc['summary'],
        [('Cliente', _fc['client']), ('Año', _fc['year']), ('Rol', _fc['role'])])
     + case_detail('Fuchi Chao: todo el cariño por tu mascota, <strong>sin la parte fuchi</strong>.', [
        ('contexto', 'Contexto y <strong>desafío</strong>',
         '<p class="lead">Citrex es una empresa de emprendedoras locales que desarrolla detergentes y eliminadores de olores para el sector pecuario, donde se trabaja con olores intensos de origen animal.</p>'
         '<p>Con esa experiencia buscaban abrir un nuevo nicho: el de las mascotas. Para entrar en un mercado tan distinto necesitaban una marca propia, con nombre, logotipo y etiquetas para cada producto.</p>'
         '<p>El desafío era llevar al hogar una fórmula pensada para la industria, con una marca cercana y confiable para quienes conviven con sus mascotas.</p>'),
        ('solucion', 'La <strong>solución</strong>',
         '<p class="lead">Un nombre que habla como hablamos en Chile, donde «fuchi» es la forma tierna de decir que algo huele mal.</p>'
         '<p>La identificación de usuarios nos llevó a la tenencia responsable y a los petlovers: personas que ven a su mascota como uno más del hogar. Fuchi Chao les habla con cariño y humor, y les promete lo que buscan: convivir sin malos olores.</p>'
         '<p>Trabajamos mano a mano con Citrex en la definición de un packaging ecológico y en el trabajo con la imprenta, para que cada etiqueta llegara al punto de venta tal como se diseñó.</p>'
         '<p>También definimos una estrategia de comunicación con plantillas por niveles, que da estructura a las publicaciones y mensajes en redes sociales: la marca comunica sin repetirse, pero siempre de forma consistente.</p>'
         '<ul><li>Naming y logotipo: una cabeza de gato que contiene el nombre, con versiones para distintos usos.</li>'
         '<li>Etiquetas para el detergente, el eliminador de olores y el jabón anti olores, con un color por producto.</li>'
         '<li>Estrategia de comunicación y plantillas por niveles para redes sociales, con el mismo tono cercano de la marca.</li></ul>'),
     ]) + case_nav(_fc))
