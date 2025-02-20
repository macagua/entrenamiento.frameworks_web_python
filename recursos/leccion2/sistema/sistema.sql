-- ======================================================================
-- ===   Sql Script for Database : sistema
-- ===
-- === Build : 48
-- ======================================================================

CREATE TABLE productos
(
    id int UNIQUE NOT NULL,
    nombre varchar(11) NOT NULL,
    descripcion varchar(25) NOT NULL,
    categoria varchar(25) NOT NULL,
    precio int NOT NULL,
    status char(1) NOT NULL,

    PRIMARY KEY (id),

    CHECK (status IN ('y', 'n'))
);

-- ======================================================================

CREATE TABLE estados
(
    id int UNIQUE NOT NULL,
    nombre varchar(25) NOT NULL,
    codigo varchar(2) NOT NULL,

    PRIMARY KEY (id)
);

-- ======================================================================

CREATE TABLE ciudades
(
    id int UNIQUE NOT NULL,
    id_estado int NOT NULL,
    nombre varchar(25) NOT NULL,
    capital int NOT NULL,

    PRIMARY KEY (id),

    FOREIGN KEY (id_estado) REFERENCES estados (
        id
    ) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ======================================================================

CREATE TABLE clientes
(
    id int UNIQUE NOT NULL,
    nombre varchar(25) NOT NULL,
    apellido varchar(25) NOT NULL,
    codigo_postal int NOT NULL,
    telefono varchar(20) NOT NULL,

    PRIMARY KEY (id),

    FOREIGN KEY (codigo_postal) REFERENCES ciudades (
        id
    ) ON UPDATE CASCADE ON DELETE CASCADE
);

-- ======================================================================

CREATE TABLE pedidos
(
    id int UNIQUE NOT NULL,
    cliente_id int NOT NULL,
    fecha date NOT NULL,
    producto_id int NOT NULL,
    status char(1) NOT NULL,

    PRIMARY KEY (id),

    FOREIGN KEY (cliente_id) REFERENCES clientes (id),
    FOREIGN KEY (producto_id) REFERENCES productos (id),

    CHECK (status IN ('y', 'n'))
);

-- ======================================================================
