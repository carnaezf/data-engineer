CREATE DATABASE supermercado_olap;
USE supermercado_olap;


-- Crear dimensiones
CREATE TABLE producto (
  id_producto INT PRIMARY KEY,
  nombre TEXT,
  categoria TEXT,
  proveedor TEXT
);


CREATE TABLE sucursal (
  id_sucursal INT PRIMARY KEY,
  ciudad TEXT,
  zona TEXT
);


CREATE TABLE fecha (
  id_fecha INT PRIMARY KEY,
  fecha DATE,
  mes TEXT,
  año INT
);


-- Definir la tabla de hechos
CREATE TABLE movimientos (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  id_producto INT,
  id_sucursal INT,
  id_fecha INT,
  tipo_movimiento TEXT, -- entrada o salida
  cantidad INT,
  total DECIMAL(10,2),
  CONSTRAINT fk_prod FOREIGN KEY (id_producto) REFERENCES producto(id_producto),
  CONSTRAINT fk_suc FOREIGN KEY (id_sucursal) REFERENCES sucursal(id_sucursal),
  CONSTRAINT fk_fecha FOREIGN KEY (id_fecha) REFERENCES fecha(id_fecha)
);