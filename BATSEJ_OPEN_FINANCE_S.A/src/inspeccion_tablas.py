import sqlite3

def obtener_conexion(ruta_bd):
    return sqlite3.connect(ruta_bd)

def obtener_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [tabla[0] for tabla in cursor.fetchall()]

def obtener_estructura_tablas(conexion, tablas):
    cursor = conexion.cursor()
    estructuras = {}
    for tabla in tablas:
        cursor.execute(f"PRAGMA table_info({tabla});")
        estructuras[tabla] = cursor.fetchall()
    return estructuras

def inspeccionar_tablas(ruta_bd):
    try:
        with obtener_conexion(ruta_bd) as conexion:
            tablas = obtener_tablas(conexion)
            print("Tablas encontradas en la base de datos:")
            for tabla in tablas:
                print(f"- {tabla}")
            
            estructuras = obtener_estructura_tablas(conexion, tablas)
            for tabla, columnas in estructuras.items():
                print(f"\nEstructura de la tabla '{tabla}':")
                for columna in columnas:
                    print(f"Columna: {columna[1]}, Tipo: {columna[2]}, ¿Es clave primaria?: {'Sí' if columna[5] == 1 else 'No'}")
    except sqlite3.Error as e:
        print(f"Error al inspeccionar las tablas: {e}")