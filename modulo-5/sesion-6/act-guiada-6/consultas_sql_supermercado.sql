SELECT
  f.mes,
  p.categoria,
  SUM(m.cantidad) AS total_items,
  SUM(m.total) AS total_monto
FROM movimientos m
JOIN producto p ON m.id_producto = p.id_producto
JOIN fecha f ON m.id_fecha = f.id_fecha
GROUP BY f.mes, p.categoria
ORDER BY f.mes;
