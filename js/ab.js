// Prueba A/B de la landing de inicio: A es la portada actual y B es /inicio-b. Reparto 50/50 y gana la que logra más personas
// que abren Conversemos. Se carga antes de pintar para evitar parpadeos. La cookie lv_ab guarda solo la versión y qué ya se contó.
// Para revisar sin afectar los datos: /?ab=a y /?ab=b. Resultados: tools/db/003_ab_resultados.sql.
(function initAB() {
  const ACTIVO = false; // Cambiar a true para iniciar la prueba, y a false para terminarla
  const script = document.currentScript;
  const pagina = script.dataset.variante;
  const base = script.getAttribute('src').replace(/js\/ab\.js.*$/, '');
  const destino = (v) => base + (v === 'b' ? 'inicio-b' : './') + location.search + location.hash;
  const forzada = new URLSearchParams(location.search).get('ab');

  if (forzada === 'a' || forzada === 'b') {
    if (forzada !== pagina) location.replace(destino(forzada));
    return;
  }
  if (!ACTIVO || /bot|crawl|spider|slurp|lighthouse|headless|preview/i.test(navigator.userAgent)) return;

  const leer = () => (document.cookie.match(/(?:^|; )lv_ab=([ab][12]?)/) || [])[1] || '';
  const guardar = (valor) => {
    const segura = location.protocol === 'https:' ? '; Secure' : '';
    document.cookie = `lv_ab=${valor}; Max-Age=7776000; Path=/; SameSite=Lax${segura}`;
  };
  let estado = leer();
  if (!estado) {
    estado = Math.random() < 0.5 ? 'a' : 'b';
    guardar(estado);
  }
  const variante = estado[0];
  if (variante !== pagina) {
    location.replace(destino(variante));
    return;
  }
  const contar = (evento) => {
    if (!navigator.sendBeacon) return;
    const datos = new FormData();
    datos.set('variante', variante);
    datos.set('evento', evento);
    navigator.sendBeacon(`${base}contacto/ab.php`, datos);
  };
  // Cada persona cuenta una sola vez como visita y una sola vez como apertura
  if (estado.length === 1) {
    contar('visita');
    estado = `${variante}1`;
    guardar(estado);
  }
  document.addEventListener('DOMContentLoaded', () => {
    const dialogo = document.getElementById('pl-conversemos');
    if (!dialogo) return;
    dialogo.addEventListener('pl:abierto', () => {
      if (leer().endsWith('2')) return;
      contar('conversemos');
      guardar(`${variante}2`);
    });
  });
})();
