SELECT
  EXTRACT(YEAR FROM fecha) AS anio,
  EXTRACT(MONTH FROM fecha) AS mes,
  SUM(total_venta) AS total_mensual
FROM ventas
GROUP BY anio, mes
ORDER BY anio, mes;

