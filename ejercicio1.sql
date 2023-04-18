DROP SCHEMA if exists`m1_caso_practico`;
CREATE SCHEMA `m1_caso_practico`;
USE `m1_caso_practico`;

-- Opcion 1: clientes, productos, pedidos, detalles_pedidos
-- Opcion 2: autores, libros, clientes, prestamos
-- Many to One desde book hacia Author
-- One to Many desde Author hacia Book

CREATE TABLE autores (
id_autores INT auto_increment PRIMARY KEY,
nombre VARCHAR (50),
apellidos VARCHAR (100),
fecha_nacimiento DATE
);

CREATE TABLE libros (
id_libro INT auto_increment PRIMARY KEY,
titulo VARCHAR(250),
editorial VARCHAR(100),
category VARCHAR(50),
num_paginas INT,
precio DECIMAL(3, 2),
id_autor INT, -- crear columna
FOREIGN KEY (id_autor) REFERENCES autores(id_autor) -- añadir fk a columna id_autor de libros
);

CREATE TABLE usuarios (
id_usuario INT auto_increment PRIMARY KEY,
nif VARCHAR(9),
email VARCHAR(50) UNIQUE,
fecha_alta DATE,
codigo_postal VARCHAR(5),
UNIQUE KEY ´usuarios_nif_unique´ (´nif´)
);

CREATE TABLE prestamos ( 
id_prestamo INT auto_increment PRIMARY KEY,
id_libro INT,
id_usuario INT,
fecha_inicio DATE,
fecha_fin DATE,
recargo DECIMAL(3, 2) DEFAULT 0.0
FOREIGN KEY (id_libro) REFERENCES libros(id_libro),
FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

select * from autores;
select * from libros;
select * from usuarios;
select * from prestamos;