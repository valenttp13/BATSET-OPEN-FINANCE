import pandas as pd
import xlsxwriter

def crear_writer_excel(nombre_archivo):
    """Crea y devuelve un objeto ExcelWriter para escribir en un archivo Excel."""
    return pd.ExcelWriter(nombre_archivo, engine='xlsxwriter')

def escribir_reporte_excel(writer, reporte, sheet_name='Reporte'):
    """Escribe un DataFrame en un archivo Excel en la hoja especificada."""
    reporte.to_excel(writer, index=False, sheet_name=sheet_name)

def generar_reporte_excel(reporte, nombre_archivo):
    """Genera un archivo Excel con los datos del DataFrame especificado."""
    with crear_writer_excel(nombre_archivo) as writer:
        escribir_reporte_excel(writer, reporte)
