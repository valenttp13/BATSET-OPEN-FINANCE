import sqlite3

def obtener_conexion(ruta_bd):
    """Establece y devuelve una conexión a la base de datos SQLite."""
    return sqlite3.connect(ruta_bd)

def obtener_tablas(conexion):
    """Devuelve una lista con los nombres de todas las tablas en la base de datos."""
    cursor = conexion.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [tabla[0] for tabla in cursor.fetchall()]

def obtener_muestras_tablas(conexion, tablas, limite=5):
    """Obtiene una muestra de datos de cada tabla especificada, con un límite de filas por tabla."""
    cursor = conexion.cursor()
    datos = {}
    for tabla in tablas:
        cursor.execute(f"SELECT * FROM {tabla} LIMIT {limite};")
        datos[tabla] = cursor.fetchall()
    return datos

def explorar_base_datos(ruta_bd):
    """Explora la base de datos, mostrando las tablas existentes y una muestra de sus datos."""
    try:
        with obtener_conexion(ruta_bd) as conexion:
            tablas = obtener_tablas(conexion)
            print("Tablas en la base de datos:")
            for tabla in tablas:
                print(f"- {tabla}")
            
            muestras = obtener_muestras_tablas(conexion, tablas)
            for tabla, filas in muestras.items():
                print(f"\nDatos de la tabla '{tabla}':")
                for fila in filas:
                    print(fila)
    except sqlite3.Error as e:
        print(f"Error al explorar la base de datos: {e}")
