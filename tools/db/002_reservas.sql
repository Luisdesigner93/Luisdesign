-- Reuniones agendadas desde el popup de contacto. Aplicar una vez en la base MySQL del cPanel (phpMyAdmin).
-- Las fechas se guardan en UTC.
CREATE TABLE IF NOT EXISTS reservas (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  creado_en DATETIME NOT NULL,
  inicio DATETIME NOT NULL,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(150) NOT NULL,
  mensaje TEXT NOT NULL,
  idioma CHAR(2) NOT NULL DEFAULT 'es',
  google_evento_id VARCHAR(255) NULL,
  ip_hash CHAR(64) NOT NULL,
  consentimiento_version VARCHAR(20) NOT NULL,
  KEY idx_ip_fecha (ip_hash, creado_en),
  KEY idx_correo_inicio (correo, inicio)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
