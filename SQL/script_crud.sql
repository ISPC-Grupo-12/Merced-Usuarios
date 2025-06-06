-- CONSULTAS SQL

--CREAR LA TABLA

DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    contraseña TEXT NOT NULL,
    rol TEXT CHECK(rol IN ('admin', 'usuario')) NOT NULL
);

--REGISTRAR USUARIOS

INSERT INTO usuarios (nombre, apellido, email, contraseña, rol)
VALUES ('Pedro', 'González', 'pedro@gmail.com', 'pass1234', 'admin');

--BUSCAR USUARIOS

--Listar todos los usuarios

SELECT * FROM usuarios;

--Por id

SELECT * FROM usuarios WHERE id = 1;

--Validar login

SELECT * FROM usuarios WHERE email = 'pedro@gmail.com' AND contraseña = 'pass1234';


--MODIFICAR USUARIOS

--Modificar datos

UPDATE usuarios
SET nombre = 'Pedro actualizado', apellido = 'González actualizado'
WHERE id = 1;

--Modificar rol

UPDATE usuarios
SET rol = 'usuario'
WHERE id = 1;

--ELIMINAR USUARIO

DELETE FROM usuarios
WHERE id = 1;







