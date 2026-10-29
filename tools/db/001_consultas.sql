-- Mensajes del formulario de contacto. Aplicar una vez en la base MySQL del cPanel (phpMyAdmin).
CREATE TABLE IF NOT EXISTS consultas (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(150) NOT NULL,
  mensaje TEXT NOT NULL,
  ip_hash CHAR(64) NOT NULL,
  consentimiento_version VARCHAR(20) NOT NULL,
  KEY idx_ip_fecha (ip_hash, creado_en)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
