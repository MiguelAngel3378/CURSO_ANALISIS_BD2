
use m1_caso_practico_sql_miguelangel;

CREATE TABLE `clientes` (
`id_cliente` int NOT NULL AUTO_INCREMENT,
`nombre` varchar(45) NOT NULL,
`apellido` varchar(45) NOT NULL,
`email` varchar(45) NOT NULL,
`telefono` varchar(45) NOT NULL,
`direccion` varchar(45) NOT NULL,
PRIMARY KEY (`id_cliente`),
UNIQUE KEY `id_cliente_UNIQUE` (`id_cliente`),
CONSTRAINT `id_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `productos` (`id_producto`)
);

CREATE TABLE `productos` (
`id_producto` int NOT NULL,
`nombre_producto` varchar(45) NOT NULL,
`descripcion_producto` varchar(45) NOT NULL,
`precio_producto` decimal(10,2) NOT NULL,
`stock_producto` int DEFAULT NULL,
PRIMARY KEY (`id_producto`),
UNIQUE KEY `id_producto_UNIQUE` (`id_producto`)
);

CREATE TABLE `detalles_pedidos` (
`id_detalle_pedido` int NOT NULL,
'id_pedido` varchar(45) NOT NULL,
`id_producto` varchar(45) NOT NULL,
`cantidad` varchar(45) NOT NULL,
`fecha` timestamp(6) NULL DEFAULT NULL,
PRIMARY KEY (`id_detalle_pedido`),
UNIQUE KEY `id_detalle_pedido_UNIQUE`(`id_detalle_pedido`)
);

CREATE TABLE `pedidos` (
`id_pedido` int NOT NULL,
`id_cliente` varchar(45) NOT NULL,
`fecha` date NOT NULL,
PRIMARY KEY (`id_pedido`)
);

select * from clientes;
select * from productos;
select * from pedidos;
select * from detalles_pedidos;

SELECT * FROM clientes ORDER BY apellido ASC; 
SELECT * FROM clientes ORDER BY apellido DESC; 
SELECT * FROM clientes ORDER BY nombre ASC; 
SELECT * FROM clientes ORDER BY nombre DESC; 

SELECT * FROM productos WHERE stock_producto < 10;
SELECT * FROM productos WHERE stock_producto <> 10;
SELECT * FROM productos WHERE precio_producto = 10.00;

SELECT * FROM pedidos WHERE id_cliente = 1;
SELECT * FROM pedidos WHERE id_pedido = 2;

SELECT sum(precio_producto) from productos;
SELECT sum(precio_producto * stock_producto) from productos;

SELECT dp.id_pedido, sum((pd.precio_producto * dp.cantidad)) as total
FROM detalles_pedidos AS dp
INNER JOIN pedidos AS p ON p.id_pedido = dp.id_pedido
INNER JOIN productos AS pd ON pd.id_producto = dp.id_producto
GROUP BY dp.id_pedido;

SELECT COUNT(*) FROM pedidos;
SELECT COUNT(*) FROM productos;

SELECT dp.id_detalle_pedido, SUM(cantidad) AS cantidad_productos_dif
FROM detalles_pedidos AS dp
JOIN pedidos ON id_pedido = id_pedido
JOIN productos ON p.id_producto = q.id_producto
GROUP BY id_pedido, descripcion_producto ORDER BY cantidad DESC LIMIT 1;



