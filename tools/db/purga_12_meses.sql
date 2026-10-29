-- Plazo de conservación: 12 meses. Ejecutar mensualmente (cron o phpMyAdmin).
DELETE FROM consultas WHERE creado_en < NOW() - INTERVAL 12 MONTH;
