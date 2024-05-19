import sqlite3

conn = sqlite3.connect("personal.db")

conn.execute(
    """
    CREATE TABLE DEPARTAMENTOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL);
    """
)

conn.execute(
    """
    CREATE TABLE CARGOS
    (id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    nivel TEXT NOT NULL,
    fecha_creacion TEXT NOT NULL);
    """
)

conn.execute(
    """
    CREATE TABLE EMPLEADOS
    (id INTEGER PRIMARY KEY,
    nombres TEXT NOT NULL,
    apellido_paterno TEXT NOT NULL,
    apellido_materno TEXT NOT NULL,
    fecha_contratacion TEXT NOT NULL,
    departamentos_id INTEGER NOT NULL,
    cargos_id INTEGER NOT NULL,
    FOREIGN KEY (departamentos_id) REFERENCES DEPARTAMENTOS (id),
    FOREIGN KEY (cargos_id) REFERENCES CARGOS (id));
    """
)

conn.execute(
    """
    CREATE TABLE SALARIOS
    (
        id INTEGER PRIMARY KEY,
        empleado_id INTEGER NOT NULL,
        salario REAL NOT NULL,
        fecha_inicio DATE NOT NULL,
        fecha_fin DATE NOT NULL,
        fecha_creacion DATE NOT NULL,
        FOREIGN KEY (empleado_id) REFERENCES EMPLEADOS (id)
    );
    """
)

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('Ventas','11-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO DEPARTAMENTOS (nombre, fecha_creacion) 
    VALUES ('MArketing','11-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Gerente de Ventas', 'Senior','10-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('Analista de Marketing', 'Junior','11-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO CARGOS (nombre, nivel, fecha_creacion) 
    VALUES ('REpresentante de Ventas', 'Junior','12-04-2020')
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamentos_id, cargos_id) 
    VALUES ('Juan', 'Gonzales', 'Perez', '15-05-2023', 1, 1)
    """
)

conn.execute(
    """
    INSERT INTO EMPLEADOS (nombres, apellido_paterno, apellido_materno, fecha_contratacion, departamentos_id, cargos_id) 
    VALUES ('Maria', 'Lopez', 'Martinez', '20-06-2023', 2, 2)
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (1, 3000.00, '01-07-2024', '30-04-2025', '01-07-2024')
    """
)

conn.execute(
    """
    INSERT INTO SALARIOS (empleado_id, salario, fecha_inicio, fecha_fin, fecha_creacion) 
    VALUES (2, 3500.00, '01-07-2024', '30-04-2025', '01-07-2024')
    """
)

print("DEPARTAMENTOS:")
cursor = conn.execute("SELECT * FROM DEPARTAMENTOS")
for row in cursor:
    print(row)

print("CARGOS:")
cursor = conn.execute("SELECT * FROM CARGOS")
for row in cursor:
    print(row)

print("EMPLEADOS:")
cursor = conn.execute("SELECT * FROM EMPLEADOS")
for row in cursor:
    print(row)

print("SALARIOS:")
cursor = conn.execute("SELECT * FROM SALARIOS")
for row in cursor:
    print(row)

print("\nSALARIOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno, SALARIOS.salario 
    FROM SALARIOS
    JOIN EMPLEADOS ON SALARIOS.empleado_id = empleados.id
    """
)

print("\nDEPARTAMENTOS: INNER JOIN")
cursor = conn.execute(
    """
    SELECT DEPARTAMENTOS.nombre, CARGOS.nombre, EMPLEADOS.nombres, EMPLEADOS.apellido_paterno, EMPLEADOS.apellido_materno 
    FROM EMPLEADOS
    JOIN DEPARTAMENTOS ON EMPLEADOS.departamentos_id = departamentos.id
    JOIN DEPARTAMENTOS ON EMPLEADOS.cargos_id = cargos.id
    """
)

for row in cursor:
    print(row)

conn.commit()

conn.close()

