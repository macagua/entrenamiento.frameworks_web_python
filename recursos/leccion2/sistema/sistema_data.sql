-- Insertar registros de tabla clientes
INSERT INTO clientes (id, nombre, apellido, codigo_postal, telefono)
VALUES (1, 'Leonardo', 'Caballero', '5001', '+58-412-4734567');
INSERT INTO clientes (id, nombre, apellido, codigo_postal, telefono)
VALUES (2, 'Ana', 'Poleo', '6302', '+58-426-5831297');
INSERT INTO clientes (id, nombre, apellido, codigo_postal, telefono)
VALUES (3, 'Manuel', 'Matos', '4001', '+58-414-2360943');

-- Seleccionar registros
SELECT * FROM clientes;
SELECT * FROM clientes
WHERE id = 1;

-- Actualizar registros
UPDATE clientes SET codigo_postal = 5051
WHERE id = 1;
UPDATE clientes SET codigo_postal = 6303
WHERE id = 2;

-- Eliminar registros
DELETE FROM clientes
WHERE id = 2;
