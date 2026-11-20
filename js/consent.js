// Consentimiento de cookies. Por defecto no se guarda ni se envía nada de analítica. Solo si la persona acepta se carga
// Google Tag Manager (con Consent Mode v2) y Microsoft Clarity. La elección queda en la cookie técnica lv_consent (6 meses).
// Si un ID aún no está configurado, ese servicio no se carga.
//
// Versiones del consentimiento: cada vez que se suma un servicio o una finalidad nueva, sube VERSION y anota qué cubre.
//   v1 (cookie «aceptado»):    Google Tag Manager y Google Analytics.
//   v2 (cookie «aceptado-v2»): v1 + Microsoft Clarity (noviembre de 2026).
// Quien aceptó una versión anterior conserva solo lo que aceptó y vuelve a ver el aviso. Quien rechazó no vuelve a verlo.
(function initConsent() {
  const VERSION = 2;
  const banner = document.getElementById('cookie-banner');
  if (!banner) return;
  const gtmId = banner.dataset.gtm || '';
  const gtmListo = /^GTM-[A-Z0-9]{6,}$/.test(gtmId) && !gtmId.includes('XXXX');
  const gaId = banner.dataset.ga || '';
  const gaListo = /^G-[A-Z0-9]{6,}$/.test(gaId);
  const clarityId = banner.dataset.clarity || '';
  const clarityListo = /^[a-z0-9]{6,12}$/.test(clarityId);
  const cargados = {};

  // Consent Mode: todo denegado antes de cualquier etiqueta de Google
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function gtag() { window.dataLayer.push(arguments); };
  window.gtag('consent', 'default', { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' });

  // Devuelve { aceptado: false } si rechazó, { aceptado: true, version: n } si aceptó, o null si aún no elige
  function leerElección() {
    const coincidencia = document.cookie.match(/(?:^|; )lv_consent=(rechazado|aceptado(?:-v(\d+))?)/);
    if (!coincidencia) return null;
    if (coincidencia[1] === 'rechazado') return { aceptado: false };
    return { aceptado: true, version: coincidencia[2] ? Number(coincidencia[2]) : 1 };
  }

  function guardarElección(aceptado) {
    const valor = aceptado ? `aceptado-v${VERSION}` : 'rechazado';
    document.cookie = `lv_consent=${valor}; Max-Age=15552000; Path=/; SameSite=Lax; Secure`;
  }

  // Microsoft Clarity (mapas de calor y grabaciones de sesión): desde la versión 2
  function cargarClarity() {
    if (!clarityListo || cargados.clarity) return;
    cargados.clarity = true;
    window.clarity = window.clarity || function clarity() { (window.clarity.q = window.clarity.q || []).push(arguments); };
    window.clarity('consentv2', { ad_Storage: 'denied', analytics_Storage: 'granted' });
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.clarity.ms/tag/${encodeURIComponent(clarityId)}`;
    document.head.appendChild(script);
  }

  // Google Tag Manager y Analytics: desde la versión 1
  function cargarGoogle() {
    if ((!gtmListo && !gaListo) || cargados.google) return;
    cargados.google = true;
    window.gtag('consent', 'update', { analytics_storage: 'granted' });
    if (gaListo) {
      const gaScript = document.createElement('script');
      gaScript.async = true;
      gaScript.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(gaId)}`;
      document.head.appendChild(gaScript);
      window.gtag('js', new Date());
      window.gtag('config', gaId);
    }
    if (!gtmListo) return;
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtm.js?id=${encodeURIComponent(gtmId)}`;
    document.head.appendChild(script);
  }

  // Carga solo los servicios que cubre la versión aceptada
  function cargarHasta(version) {
    if (version >= 1) cargarGoogle();
    if (version >= 2) cargarClarity();
  }

  const elección = leerElección();
  if (elección === null) banner.hidden = false;
  else if (elección.aceptado) {
    cargarHasta(elección.version);
    if (elección.version < VERSION) banner.hidden = false;
  }

  banner.querySelectorAll('[data-consent]').forEach((boton) => {
    boton.addEventListener('click', () => {
      const aceptado = boton.dataset.consent === 'aceptado';
      guardarElección(aceptado);
      banner.hidden = true;
      if (aceptado) cargarHasta(VERSION);
      // Si rechaza después de haber aceptado una versión anterior, Google deja de guardar datos de analítica
      else if (cargados.google) window.gtag('consent', 'update', { analytics_storage: 'denied' });
    });
  });
})();
