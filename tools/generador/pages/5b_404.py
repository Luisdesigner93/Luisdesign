# Página sin datos compartidos: su contenido se edita directamente en fragmentos/404.html
page('404.html', 'Página no encontrada · Luis Vicencio',
     'La página que buscas no existe o cambió de dirección.',
     body=fragment('404.html'), contact=False, noindex=True, absolute=True)
