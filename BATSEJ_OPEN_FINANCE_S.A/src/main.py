from cargar_bd import cargar_tabla
from calculo_comision import calcular_comisiones
from generar_reportes import generar_reporte_excel
from enviar_correo import enviar_correo_outlook
import os
from datetime import datetime

def obtener_ruta_base():
    """
    Busca la carpeta 'BATSEJ_OPEN_FINANCE_S.A' a partir del script actual.
    """
    ruta_actual = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ruta absoluta del script
    while not os.path.basename(ruta_actual).upper() == "BATSEJ_OPEN_FINANCE_S.A":
        ruta_actual = os.path.dirname(ruta_actual)
        if ruta_actual == os.path.dirname(ruta_actual):  # Si llega a la raíz sin encontrar la carpeta
            raise FileNotFoundError("No se encontró la carpeta 'BATSEJ_OPEN_FINANCE_S.A'. Verifica la estructura.")
    return ruta_actual

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Cargar datos")
    print("2. Calcular comisiones")
    print("3. Generar Excel")
    print("4. Enviar correo")
    print("5. Salir")
    print("------------------------")

def main():
    datos_apicall = None
    datos_commerce = None
    reporte = None

    # Obtiene la ruta base
    ruta_base = obtener_ruta_base()

    # Corrige la ruta de la base de datos
    ruta_bd = os.path.join(ruta_base, "data", "database.sqlite")

    # Verifica que el archivo de la base de datos exista
    if not os.path.exists(ruta_bd):
        raise FileNotFoundError(f"❌ No se encontró la base de datos en: {ruta_bd}")

    # Ruta del reporte
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M")
    ruta_reporte = os.path.join(ruta_base, "Salidas", f"reporte_comisiones_{fecha_hora}.xlsx")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\nCargando datos de la base de datos...")
            datos_apicall = cargar_tabla(ruta_bd, 'apicall')
            datos_commerce = cargar_tabla(ruta_bd, 'commerce')
            print("✅ Datos cargados exitosamente.")
            print(f"📊 Transacciones (apicall): {len(datos_apicall)} registros")
            print(f"🏬 Comercios (commerce): {len(datos_commerce)} registros")

        elif opcion == "2":
            if datos_apicall is not None and datos_commerce is not None:
                print("\nCalculando comisiones...")
                reporte = calcular_comisiones(datos_apicall, datos_commerce)
                print("✅ Comisiones calculadas exitosamente.")
                print("\nResumen de las primeras filas:")
                print(reporte.head())
            else:
                print("\n⚠️ Por favor, carga los datos primero (opción 1).")

        elif opcion == "3":
            if reporte is not None:
                print("\nGenerando reporte en Excel...")
                generar_reporte_excel(reporte, ruta_reporte)
                print(f"✅ Reporte generado exitosamente en: {ruta_reporte}")
            else:
                print("\n⚠️ Por favor, calcula las comisiones primero (opción 2).")

        elif opcion == "4":
            if reporte is not None:
                print("\nEnviando reporte por correo...")
                ejecutor = input("📧 Ingresa el correo de destino: ")
                asunto = "📊 Reporte de Comisiones"
                cuerpo = "Adjunto encontrarás el reporte de comisiones generado."
                enviar_correo_outlook(ejecutor, asunto, cuerpo, ruta_reporte)
            else:
                print("\n⚠️ Por favor, genera el reporte primero (opción 3).")

        elif opcion == "5":
            print("\n👋 Saliendo del programa.")
            break

        else:
            print("\n❌ Opción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    main()
