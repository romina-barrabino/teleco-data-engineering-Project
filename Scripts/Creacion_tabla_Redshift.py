#No se pudo ejecutar por falta de permisos del usuario
create table telecom_transformed (
    id_cliente INT,
    nombre_cliente VARCHAR(255),
    plan VARCHAR(255),
    fecha_inicio DATE,
    fecha_fin DATE,
    monto DECIMAL (10,2),
    monto_total DECIMAL(10,2)
);
go