-- ======================================================================
-- ===   Sql Script for Database : sistema
-- ===
-- === Build : 48
-- ======================================================================

CREATE TABLE productos
  (
    id           int           unique not null,
    nombre       varchar(11)   not null,
    descripcion  varchar(25)   not null,
    categoria    varchar(25)   not null,
    precio       int           not null,
    status       char(1)       not null,

    primary key(id),

    CHECK(status IN ('y', 'n'))
  );

-- ======================================================================

CREATE TABLE estados
  (
    id      int           unique not null,
    nombre  varchar(25)   not null,
    codigo  varchar(2)    not null,

    primary key(id)
  );

-- ======================================================================

CREATE TABLE ciudades
  (
    id         int           unique not null,
    id_estado  int           not null,
    nombre     varchar(25)   not null,
    capital    int           not null,

    primary key(id),

    foreign key(id_estado) references estados(id) on update CASCADE on delete CASCADE
  );

-- ======================================================================

CREATE TABLE clientes
  (
    id             int           unique not null,
    nombre         varchar(25)   not null,
    apellido       varchar(25)   not null,
    codigo_postal  int           not null,
    telefono       varchar(11)   not null,

    primary key(id),

    foreign key(codigo_postal) references ciudades(id) on update CASCADE on delete CASCADE
  );

-- ======================================================================

CREATE TABLE pedidos
  (
    id           int       unique not null,
    cliente_id   int       not null,
    fecha        date      not null,
    producto_id  int       not null,
    status       char(1)   not null,

    primary key(id),

    foreign key(cliente_id) references clientes(id),
    foreign key(producto_id) references productos(id),

    CHECK(status IN ('y', 'n'))
  );

-- ======================================================================
