import sqlite3
import pandas as pd

def obtener_conexion(ruta_bd):
    return sqlite3.connect(ruta_bd)

def ejecutar_consulta(conexion, query):
    return pd.read_sql_query(query, conexion)

def cargar_tabla(ruta_bd, nombre_tabla):
    with obtener_conexion(ruta_bd) as conexion:
        return ejecutar_consulta(conexion, f"SELECT * FROM {nombre_tabla}")