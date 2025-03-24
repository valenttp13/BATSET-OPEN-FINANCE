import sqlite3

def obtener_conexion(ruta_bd):
    return sqlite3.connect(ruta_bd)

def obtener_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [tabla[0] for tabla in cursor.fetchall()]

def obtener_muestras_tablas(conexion, tablas, limite=5):
    cursor = conexion.cursor()
    datos = {}
    for tabla in tablas:
        cursor.execute(f"SELECT * FROM {tabla} LIMIT {limite};")
        datos[tabla] = cursor.fetchall()
    return datos

def explorar_base_datos(ruta_bd):
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