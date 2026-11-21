import sqlite3

NOMBRE_BD = "rentacar.db"

def obtener_conexion():
    """Abre una conexion con la base de datos"""
    conexion = sqlite3.connect(NOMBRE_BD)
    conexion.row_factory = sqlite3.Row  #permite acceder a las columnas por nombre
    return conexion

def crear_tablas():
    """Crea todas las tablas si todavia no existen"""
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL UNIQUE,
            clave TEXT NOT NULL,
            rol TEXT NOT NULL DEFAULT 'cliente'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            nombre TEXT NOT NULL,
            identidad TEXT NOT NULL,
            telefono TEXT,
            direccion TEXT,
            FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT NOT NULL,
            modelo TEXT NOT NULL,
            anio INTEGER NOT NULL,
            categoria TEXT,
            precio_dia REAL NOT NULL,
            cantidad INTEGER NOT NULL DEFAULT 1,
            disponible INTEGER NOT NULL DEFAULT 1
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS compras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehiculo_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            costo_unitario REAL NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alquileres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            vehiculo_id INTEGER NOT NULL,
            fecha_inicio TEXT NOT NULL,
            fecha_fin TEXT NOT NULL,
            total REAL NOT NULL,
            estado TEXT NOT NULL DEFAULT 'activo',
            FOREIGN KEY (cliente_id) REFERENCES clientes(id),
            FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alquiler_id INTEGER NOT NULL,
            monto REAL NOT NULL,
            metodo TEXT NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (alquiler_id) REFERENCES alquileres(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS facturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero TEXT NOT NULL UNIQUE,
            fecha TEXT NOT NULL,
            alquiler_id INTEGER NOT NULL,
            cliente_id INTEGER NOT NULL,
            detalle TEXT,
            subtotal REAL NOT NULL,
            impuesto REAL NOT NULL,
            total REAL NOT NULL,
            FOREIGN KEY (alquiler_id) REFERENCES alquileres(id),
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)

    conexion.commit()
    conexion.close()

def crear_admin_por_defecto():
    """Crea un administrador inicial si todavia no hay ninguno"""
    conexion = obtener_conexion()
    existe = conexion.execute(
        "SELECT 1 FROM usuarios WHERE rol = 'admin'"
    ).fetchone()
    if existe is None:
        conexion.execute(
            "INSERT INTO usuarios (nombre, correo, clave, rol) VALUES (?, ?, ?, ?)",
            ("Administrador", "admin@rentacar.com", "admin123", "admin"),
        )
        conexion.commit()
    conexion.close()

