-- Totales de la prueba A/B de inicio. Aplicar una vez en la base MySQL del cPanel (phpMyAdmin).
-- Solo guarda conteos por día, versión y evento: ningún dato de personas.
CREATE TABLE IF NOT EXISTS ab_resultados (
  fecha DATE NOT NULL,
  variante CHAR(1) NOT NULL,
  evento VARCHAR(20) NOT NULL,
  total INT UNSIGNED NOT NULL DEFAULT 0,
  PRIMARY KEY (fecha, variante, evento)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Para ver el resultado, ejecutar esta consulta:
-- SELECT variante,
--        SUM(CASE WHEN evento = 'visita' THEN total ELSE 0 END) AS personas,
--        SUM(CASE WHEN evento = 'conversemos' THEN total ELSE 0 END) AS abrieron_conversemos,
--        ROUND(100 * SUM(CASE WHEN evento = 'conversemos' THEN total ELSE 0 END)
--              / NULLIF(SUM(CASE WHEN evento = 'visita' THEN total ELSE 0 END), 0), 2) AS conversion_pct
-- FROM ab_resultados
-- GROUP BY variante;
