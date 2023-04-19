DROP SCHEMA if exists`m1_caso_practico`;
CREATE SCHEMA `m1_caso_practico`;
USE `m1_caso_practico`;

-- Opcion 1: clientes, productos, pedidos, detalles_pedidos
-- Opcion 2: autores, libros, clientes, prestamos
-- Many to One desde book hacia Author
-- One to Many desde Author hacia Book

CREATE TABLE autores (
id_autor INT auto_increment PRIMARY KEY,
nombre VARCHAR(50),
apellidos VARCHAR(100),
fecha_nacimiento DATE
);


CREATE TABLE libros (
	id_libro INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(250),
    editorial VARCHAR (100),
    category VARCHAR (50),
    num_paginas INT,
    precio DECIMAL(6, 2),
    id_autor INT, -- crear columna
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor) -- añadir fk a columna id_autor de libros
);

CREATE TABLE usuarios (
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nif VARCHAR(9),
    email VARCHAR(50) UNIQUE,
    fecha_alta DATE,
    codigo_postal VARCHAR(5),
    UNIQUE KEY `usuarios_nif_unique` (`nif`)
);

CREATE TABLE prestamos (
	id_prestamo INT PRIMARY KEY AUTO_INCREMENT, 
    id_libro INT,
    id_usuario INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    recargo DECIMAL(6, 2) DEFAULT 0.0,
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

select * from autores;
select * from libros;
select * from usuarios;
select * from prestamos;

-- INSERTAR 
INSERT INTO autores (nombre, apellidos, fecha_nacimiento) VALUES 
('author1', 'apellido1', '1980-01-01'),
('author2', 'apellido2', '1981-01-01'),
('author3', 'apellido3', '1982-01-01'),
('author4', 'apellido4', '1983-01-01'),
('author5', 'apellido5', '1984-01-01'),
('author6', 'apellido6', '1985-01-01')
;

INSERT INTO libros (titulo, editorial, category, num_paginas, precio, id_autor) VALUES
('Ejemplo libro antiguo', 'Planeta', 'Novela', 250, 19.99, 1),
('Ejemplo libro moderno', 'Anaya', 'Tecnico', 500, 39.99, 1),
('Ensayos varios', 'Planeta', 'Ensayo', 432, 9.99, 2),
('Poemas', 'Planeta', 'Novela', 250, 19.99, 3),
('Periodico semanal', 'Planeta', 'Novela', 250, 19.99, 3),
('Ejemplo libro antiguo', 'Planeta', 'Novela', 250, 19.99, 3)
;

INSERT INTO usuarios (nif, email, fecha_alta, codigo_postal) VALUES
('1111111A', 'user1@gmail.com', '2015-01-01', '28003'),
('2222222B', 'user2@gmail.com', '2016-01-01', '28002'),
('3333333C', 'user3@gmail.com', '2015-02-01', '44500'),
('4444444D', 'user4@gmail.com', '2015-03-01', '24001'),
('5555555E', 'user5@gmail.com', '2015-04-01', '33020')
;
-- sin recargo
INSERT INTO prestamos (id_libro, id_usuario, fecha_inicio, fecha_fin) VALUES 
(1, 2, '2023-04-10', '2023-04-18')
;
-- con recargo
INSERT INTO prestamos (id_libro, id_usuario, fecha_inicio, fecha_fin, recargo) VALUES 
(1, 2, '2023-04-10', '2023-04-18', 0.0),
(2, 3, '2023-04-10', '2023-04-18', 2.34),
(3, 4, '2023-04-11', '2023-04-19', 0.0),
(2, 5, '2023-04-14', '2023-04-23', 3.0)
;

-- 1. Tabla autores
-- select por nombre like
-- select count por año de nacimiento
SELECT EXTRACT(YEAR FROM fecha_nacimiento) as birth_year, 
count(*) as total_authors
from autores
GROUP BY EXTRACT(YEAR FROM fecha_naciemiento);

	
-- 2. tabla libros
-- select por titulo like
-- count por editorial o por category
SELECT count(*) from libros;
SELECT editorial, count(*) as count_books FROM libros GROUP by editorial;
-- sum de precio por editorial
SELECT editorial, sum(precio) as precio_total from libros GROUP by editorial;
SELECT editorial, round(avg(precio), 2) as precio_medio from libros GROUP by editorial;
-- avg de precio por nombre de autor
SELECT * 
FROM libros 
JOIN autores ON libros.id_autor = autores.id_autor

SELECT autores.nombre, round(avg(precio), 2), sum(precio), round(avg(num_paginas),0), sum(num_paginas)
FROM libros 
JOIN autores ON libros.id_autor = autores.id_autor GROUP by autores.nombre;

-- max o avg por num_paginas

-- qué autor tiene más libros: max count por autor
SELECT autores.nombre as nombre_autor, count(*) as count_libros
from libros
JOIN autores on libros.id_autor = autores.id_autor GROUP by autores.nombre;

SELECT nombre_autor, max(count_libros) from
(
SELECT autores.nombre as nombre_autor, count(*) as count_libros
from libros
JOIN autores on libros.id_autor = autores.id_autor GROUP by autores.nombre
)
as result;

-- qué autor tiene más libros: min count por autor

-- 3. tabla usuarios
-- count de altas por mes
-- count por código postal

-- 4. tabla prestamos
-- count por mes
-- sum recargo
SELECT sum(recargo) from prestamos;
SELECT id_usuario, sum(recargo) as Recargo_Euros from prestamos GROUP by id_usuario;
SELECT id_usuario, sum(recargo) as Recargo_Euros from prestamos GROUP by id_usuario HAVING Recargo_Euros > 0;

-- max sum recargos group by user
-- avg (count por usuario) group by year
-- count por autor
-- max count libro