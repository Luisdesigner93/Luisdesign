// Consentimiento de cookies. Por defecto no se guarda ni se envía nada de analítica. Solo si la persona acepta se carga
// Google Tag Manager, y con Consent Mode v2 se habilita el almacenamiento de analítica. La elección queda en la cookie
// técnica lv_consent (6 meses). Si el ID de GTM aún no está configurado (GTM-XXXXXXX), no se carga Google.
(function initConsent() {
  const banner = document.getElementById('cookie-banner');
  if (!banner) return;
  const gtmId = banner.dataset.gtm || '';
  const gtmListo = /^GTM-[A-Z0-9]{6,}$/.test(gtmId) && !gtmId.includes('XXXX');

  // Consent Mode: todo denegado antes de cualquier etiqueta de Google
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag() { window.dataLayer.push(arguments); };
  window.gtag('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });

  function leerElección() {
    const coincidencia = document.cookie.match(/(?:^|; )lv_consent=(aceptado|rechazado)/);
    return coincidencia ? coincidencia[1] : null;
  }

  function guardarElección(valor) {
    document.cookie = `lv_consent=${valor}; Max-Age=15552000; Path=/; SameSite=Lax; Secure`;
  }

  function cargarGoogle() {
    if (!gtmListo) return;
    window.gtag('consent', 'update', { analytics_storage: 'granted' });
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtm.js?id=${encodeURIComponent(gtmId)}`;
    document.head.appendChild(script);
  }

  const elección = leerElección();
  if (elección === 'aceptado') cargarGoogle();
  if (elección === null) banner.hidden = false;

  banner.querySelectorAll('[data-consent]').forEach((boton) => {
    boton.addEventListener('click', () => {
      const valor = boton.dataset.consent;
      guardarElección(valor);
      banner.hidden = true;
      if (valor === 'aceptado') cargarGoogle();
    });
  });
})();
