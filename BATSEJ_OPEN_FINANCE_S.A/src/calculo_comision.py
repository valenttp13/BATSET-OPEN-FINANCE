"""
Módulo para calcular comisiones basadas en transacciones exitosas y no exitosas.

Funciones:
    - filtrar_datos: Filtra transacciones y comercios activos.
    - calcular_comision: Calcula la comisión, IVA y total según la empresa.
    - calcular_comisiones: Genera un resumen de comisiones por comercio.
"""

import pandas as pd
from datetime import datetime

def filtrar_datos(datos_apicall, datos_commerce):
    """Filtra comercios activos y transacciones de julio y agosto 2024."""
    datos_commerce = datos_commerce[datos_commerce['commerce_status'] == 'Active']
    datos_apicall['date_api_call'] = pd.to_datetime(datos_apicall['date_api_call'])
    datos_apicall = datos_apicall[
        (datos_apicall['date_api_call'].dt.month.isin([7, 8])) &
        (datos_apicall['date_api_call'].dt.year == 2024)
    ]
    return datos_apicall, datos_commerce

def calcular_comision(empresa, exitosas, no_exitosas):
    """Calcula comisión, IVA y total según tarifas y descuentos."""
    tarifas = {
        "Innovexa Solutions": 300,
        "QuantumLeap Inc.": 600,
        "FusionWave Enterprises": 300
    }
    descuentos = {
        "Zenith Corp.": [(6000, 0.05)],
        "FusionWave Enterprises": [(2500, 0.05), (4500, 0.08)]
    }
    
    if empresa in tarifas:
        valor_comision = exitosas * tarifas[empresa]
    elif empresa == "NexaTech Industries":
        valor_comision = exitosas * (250 if exitosas <= 10000 else 200 if exitosas <= 20000 else 170)
    elif empresa == "Zenith Corp.":
        valor_comision = exitosas * (250 if exitosas <= 22000 else 130)
    else:
        return 0, 0, 0
    
    for limite, descuento in descuentos.get(empresa, []):
        if no_exitosas > limite:
            valor_comision -= valor_comision * descuento
    
    valor_iva = valor_comision * 0.19
    return valor_comision, valor_iva, valor_comision + valor_iva

def calcular_comisiones(datos_apicall, datos_commerce):
    """Genera resumen de comisiones por comercio."""
    datos_apicall, datos_commerce = filtrar_datos(datos_apicall, datos_commerce)
    datos_apicall = datos_apicall.merge(datos_commerce, on='commerce_id', how='left')
    
    resumen_exitosas = datos_apicall[datos_apicall['ask_status'] == 'Successful'].groupby(
        ['commerce_id', 'commerce_name', 'commerce_nit']
    ).size().reset_index(name='Total_exitosas')
    
    resumen_no_exitosas = datos_apicall[datos_apicall['ask_status'] != 'Successful'].groupby(
        ['commerce_id', 'commerce_name', 'commerce_nit']
    ).size().reset_index(name='Total_no_exitosas')
    
    resumen = resumen_exitosas.merge(resumen_no_exitosas, on=['commerce_id', 'commerce_name', 'commerce_nit'], how='left').fillna(0)
    
    resumen[['Valor_comision', 'Valor_iva', 'Valor_Total']] = resumen.apply(
        lambda row: calcular_comision(row['commerce_name'], row['Total_exitosas'], row['Total_no_exitosas']), axis=1, result_type='expand'
    )
    
    resumen['Fecha-Mes'] = datetime.now().strftime("%Y-%m")
    resumen = resumen.merge(datos_commerce[['commerce_id', 'commerce_email']], on='commerce_id', how='left')
    
    return resumen.rename(columns={'commerce_name': 'Nombre', 'commerce_nit': 'Nit', 'commerce_email': 'Correo'})[
        ['Fecha-Mes', 'Nombre', 'Nit', 'Valor_comision', 'Valor_iva', 'Valor_Total', 'Correo']
    ]
