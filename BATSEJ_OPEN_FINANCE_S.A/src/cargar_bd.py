import sqlite3
import pandas as pd

def obtener_conexion(ruta_bd):
    """Establece y devuelve una conexión a la base de datos SQLite."""
    return sqlite3.connect(ruta_bd)

def ejecutar_consulta(conexion, query):
    """Ejecuta una consulta SQL en la base de datos y devuelve los resultados como un DataFrame de Pandas."""
    return pd.read_sql_query(query, conexion)

def cargar_tabla(ruta_bd, nombre_tabla):
    """Abre una conexión a la base de datos, recupera todos los datos de la tabla especificada y los devuelve como un DataFrame."""
    with obtener_conexion(ruta_bd) as conexion:
        return ejecutar_consulta(conexion, f"SELECT * FROM {nombre_tabla}")
