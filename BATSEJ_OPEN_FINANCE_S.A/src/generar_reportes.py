import pandas as pd
import xlsxwriter

def crear_writer_excel(nombre_archivo):
    return pd.ExcelWriter(nombre_archivo, engine='xlsxwriter')

def escribir_reporte_excel(writer, reporte, sheet_name='Reporte'):
    reporte.to_excel(writer, index=False, sheet_name=sheet_name)

def generar_reporte_excel(reporte, nombre_archivo):
    with crear_writer_excel(nombre_archivo) as writer:
        escribir_reporte_excel(writer, reporte)