-- Database: MarketPlaceUIS

-- DROP DATABASE IF EXISTS "MarketPlaceUIS";

--CREATE DATABASE "MarketPlaceUIS"
   -- WITH
   -- OWNER = postgres
   -- ENCODING = 'UTF8'
   -- LC_COLLATE = 'Spanish_Mexico.1252'
   -- LC_CTYPE = 'Spanish_Mexico.1252'
   -- TABLESPACE = pg_default
   -- CONNECTION LIMIT = -1
   -- IS_TEMPLATE = False;
	
	-- tables
-- Table: Categoria_Producto
CREATE TABLE Categoria_Producto (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    descripcion varchar(100)  NOT NULL,
    Categoria_Producto_id int  NULL,
    CONSTRAINT Categoria_Producto_pk PRIMARY KEY (id)
);

-- Table: Categoria_Servicio
CREATE TABLE Categoria_Servicio (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    descripcion varchar(100)  NOT NULL,
    CONSTRAINT Categoria_Servicio_pk PRIMARY KEY (id)
);

-- Table: Chat
CREATE TABLE Chat (
    id int  NOT NULL,
    sesion text  NOT NULL,
    CONSTRAINT Chat_pk PRIMARY KEY (id)
);

-- Table: Ciudad
CREATE TABLE Ciudad (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    CONSTRAINT Ciudad_pk PRIMARY KEY (id)
);

-- Table: Compra_Producto
CREATE TABLE Compra_Producto (
    id int  NOT NULL,
    Usuario_id int  NOT NULL,
    Producto_id int  NOT NULL,
    Chat_id int  NOT NULL,
    Estado_id int  NOT NULL,
    fecha date,
    CONSTRAINT Compra_Producto_pk PRIMARY KEY (id)
);

-- Table: Compra_Servicio
CREATE TABLE Compra_Servicio (
    id int  NOT NULL,
    Proveedor_Servicio_id int  NOT NULL,
    Usuario_id int  NOT NULL,
    Chat_id int  NOT NULL,
    Estado_id int  NOT NULL,
    fecha date,
    CONSTRAINT Compra_Servicio_pk PRIMARY KEY (id)
);

-- Table: Estado
CREATE TABLE Estado (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    descripcion varchar(100)  NOT NULL,
    CONSTRAINT Estado_pk PRIMARY KEY (id)
);

-- Table: Estado_Inmueble
CREATE TABLE Estado_Inmueble (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    descripcion varchar(100)  NOT NULL,
    CONSTRAINT Estado_Inmueble_pk PRIMARY KEY (id)
);

-- Table: Inmueble
CREATE TABLE Inmueble (
    id int  NOT NULL,
    nombre varchar(255)  NOT NULL,
    descripcion text  NOT NULL,
    precio int  NOT NULL,
    Estado_Inmueble_id int  NOT NULL,
    Ubicacion_id int  NOT NULL,
    Tipo_inmueble_id int  NOT NULL,
    Usuario_id int  NOT NULL,
    imagen bytea,
    CONSTRAINT Inmueble_pk PRIMARY KEY (id)
);

-- Table: Inventario
CREATE TABLE Inventario (
    id int  NOT NULL,
    cantidad int  NOT NULL,
    modificado timestamp,
    CONSTRAINT Inventario_pk PRIMARY KEY (id)
);

-- Table: Producto
CREATE TABLE Producto (
    id int  NOT NULL,
    nombre varchar(255)  NOT NULL,
    precio decimal(12,2)  NOT NULL,
    descripcion varchar(1000)  NOT NULL,
    imagen bytea,
    Categoria_Producto_id int  NOT NULL,
    Inventario_id int  NOT NULL,
    Usuario_id int  NOT NULL,
    CONSTRAINT Producto_pk PRIMARY KEY (id)
);

-- Table: Proveedor_Servicio
CREATE TABLE Proveedor_Servicio (
    id int  NOT NULL,
    Usuario_id int  NOT NULL,
    Servicio_id int  NOT NULL,
    precio_hora int  NOT NULL,
    imagen bytea,
    descripcion varchar(500)  NOT NULL,
    CONSTRAINT Proveedor_Servicio_pk PRIMARY KEY (id)
);

-- Table: Renta
CREATE TABLE Renta (
    id int  NOT NULL,
    Inmueble_id int  NOT NULL,
    Usuario_id int  NOT NULL,
    fecha date,
    Chat_id int,
    Estado_id int  NOT NULL,
    CONSTRAINT Renta_pk PRIMARY KEY (id)
);

-- Table: Rol
CREATE TABLE Rol (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    CONSTRAINT Rol_pk PRIMARY KEY (id)
);

-- Table: Servicio
CREATE TABLE Servicio (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    Categoria_Servicio_id int  NOT NULL,
    CONSTRAINT Servicio_pk PRIMARY KEY (id)
);

-- Table: Tipo_inmueble
CREATE TABLE Tipo_inmueble (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    descripcion varchar(100)  NOT NULL,
    CONSTRAINT Tipo_inmueble_pk PRIMARY KEY (id)
);

-- Table: Ubicacion
CREATE TABLE Ubicacion (
    id int  NOT NULL,
    barrio varchar(50)  NOT NULL,
    Ciudad_id int  NOT NULL,
    CONSTRAINT Ubicacion_pk PRIMARY KEY (id)
);

-- Table: Usuario
CREATE TABLE Usuario (
    id int  NOT NULL,
    nombre varchar(50)  NOT NULL,
    apellido varchar(50)  NOT NULL,
    email varchar(255)  NOT NULL,
    telefono int  NOT NULL,
    Rol_id int  NOT NULL,
    CONSTRAINT Usuario_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: Categoria_Producto_Categoria_Producto (table: Categoria_Producto)
ALTER TABLE Categoria_Producto ADD CONSTRAINT Categoria_Producto_Categoria_Producto
    FOREIGN KEY (Categoria_Producto_id)
    REFERENCES Categoria_Producto (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Producto_Chat (table: Compra_Producto)
ALTER TABLE Compra_Producto ADD CONSTRAINT Compra_Producto_Chat
    FOREIGN KEY (Chat_id)
    REFERENCES Chat (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Producto_Estado (table: Compra_Producto)
ALTER TABLE Compra_Producto ADD CONSTRAINT Compra_Producto_Estado
    FOREIGN KEY (Estado_id)
    REFERENCES Estado (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Producto_Producto (table: Compra_Producto)
ALTER TABLE Compra_Producto ADD CONSTRAINT Compra_Producto_Producto
    FOREIGN KEY (Producto_id)
    REFERENCES Producto (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Producto_Usuario (table: Compra_Producto)
ALTER TABLE Compra_Producto ADD CONSTRAINT Compra_Producto_Usuario
    FOREIGN KEY (Usuario_id)
    REFERENCES Usuario (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Servicio_Chat (table: Compra_Servicio)
ALTER TABLE Compra_Servicio ADD CONSTRAINT Compra_Servicio_Chat
    FOREIGN KEY (Chat_id)
    REFERENCES Chat (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Servicio_Estado (table: Compra_Servicio)
ALTER TABLE Compra_Servicio ADD CONSTRAINT Compra_Servicio_Estado
    FOREIGN KEY (Estado_id)
    REFERENCES Estado (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Servicio_Proveedor_Servicio (table: Compra_Servicio)
ALTER TABLE Compra_Servicio ADD CONSTRAINT Compra_Servicio_Proveedor_Servicio
    FOREIGN KEY (Proveedor_Servicio_id)
    REFERENCES Proveedor_Servicio (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Compra_Servicio_Usuario (table: Compra_Servicio)
ALTER TABLE Compra_Servicio ADD CONSTRAINT Compra_Servicio_Usuario
    FOREIGN KEY (Usuario_id)
    REFERENCES Usuario (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Inmueble_Estado_Inmueble (table: Inmueble)
ALTER TABLE Inmueble ADD CONSTRAINT Inmueble_Estado_Inmueble
    FOREIGN KEY (Estado_Inmueble_id)
    REFERENCES Estado_Inmueble (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Inmueble_Tipo_inmueble (table: Inmueble)
ALTER TABLE Inmueble ADD CONSTRAINT Inmueble_Tipo_inmueble
    FOREIGN KEY (Tipo_inmueble_id)
    REFERENCES Tipo_inmueble (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Inmueble_Ubicacion (table: Inmueble)
ALTER TABLE Inmueble ADD CONSTRAINT Inmueble_Ubicacion
    FOREIGN KEY (Ubicacion_id)
    REFERENCES Ubicacion (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Inmueble_Usuario (table: Inmueble)
ALTER TABLE Inmueble ADD CONSTRAINT Inmueble_Usuario
    FOREIGN KEY (Usuario_id)
    REFERENCES Usuario (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Producto_Categoria_Producto (table: Producto)
ALTER TABLE Producto ADD CONSTRAINT Producto_Categoria_Producto
    FOREIGN KEY (Categoria_Producto_id)
    REFERENCES Categoria_Producto (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Producto_Inventario (table: Producto)
ALTER TABLE Producto ADD CONSTRAINT Producto_Inventario
    FOREIGN KEY (Inventario_id)
    REFERENCES Inventario (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Producto_Usuario (table: Producto)
ALTER TABLE Producto ADD CONSTRAINT Producto_Usuario
    FOREIGN KEY (Usuario_id)
    REFERENCES Usuario (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Proveedor_Servicio_Servicio (table: Proveedor_Servicio)
ALTER TABLE Proveedor_Servicio ADD CONSTRAINT Proveedor_Servicio_Servicio
    FOREIGN KEY (Servicio_id)
    REFERENCES Servicio (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Proveedor_Servicio_Usuario (table: Proveedor_Servicio)
ALTER TABLE Proveedor_Servicio ADD CONSTRAINT Proveedor_Servicio_Usuario
    FOREIGN KEY (Usuario_id)
    REFERENCES Usuario (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Renta_Chat (table: Renta)
ALTER TABLE Renta ADD CONSTRAINT Renta_Chat
    FOREIGN KEY (Chat_id)
    REFERENCES Chat (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Renta_Estado (table: Renta)
ALTER TABLE Renta ADD CONSTRAINT Renta_Estado
    FOREIGN KEY (Estado_id)
    REFERENCES Estado (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Renta_Inmueble (table: Renta)
ALTER TABLE Renta ADD CONSTRAINT Renta_Inmueble
    FOREIGN KEY (Inmueble_id)
    REFERENCES Inmueble (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Renta_Usuario (table: Renta)
ALTER TABLE Renta ADD CONSTRAINT Renta_Usuario
    FOREIGN KEY (Usuario_id)
    REFERENCES Usuario (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Servicio_Categoria_Servicio (table: Servicio)
ALTER TABLE Servicio ADD CONSTRAINT Servicio_Categoria_Servicio
    FOREIGN KEY (Categoria_Servicio_id)
    REFERENCES Categoria_Servicio (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Ubicacion_Ciudad (table: Ubicacion)
ALTER TABLE Ubicacion ADD CONSTRAINT Ubicacion_Ciudad
    FOREIGN KEY (Ciudad_id)
    REFERENCES Ciudad (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Usuario_Rol (table: Usuario)
ALTER TABLE Usuario ADD CONSTRAINT Usuario_Rol
    FOREIGN KEY (Rol_id)
    REFERENCES Rol (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;
