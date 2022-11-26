-- ======================================================================
-- ===   Sql Script for Database : sistema
-- ===
-- === Build : 41
-- ======================================================================

CREATE TABLE pais
  (
    id      int           unique not null,
    nombre  varchar(25)   not null,
    codigo  varchar(2)    not null,

    primary key(id,nombre)
  );

-- ======================================================================

CREATE TABLE estados
  (
    id         int           unique not null,
    codigo     varchar(2)    not null,
    nombre     varchar(25)   not null,
    pais       int           not null,
    poblacion  int           not null,

    primary key(id),

    foreign key(pais) references pais(id) on update CASCADE on delete CASCADE
  );

-- ======================================================================

CREATE TABLE ciudades
  (
    id         int           unique not null,
    nombre     varchar(25)   not null,
    estado     int           not null,
    poblacion  int           not null,

    primary key(id),

    foreign key(estado) references estados(id) on update CASCADE on delete CASCADE
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
