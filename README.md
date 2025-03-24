# 📊 Automatización de Comisiones - BATSEJ OPEN FINANCE S.A  

Este proyecto implementa un sistema de automatización con **Python** y **SQLite** para calcular y gestionar las comisiones de empresas que utilizan la API de verificación de cuentas bancarias de BATSEJ OPEN FINANCE S.A.  

## 🚀 Funcionalidades  
✔️ Extrae los datos desde una base de datos **SQLite**.  
✔️ Calcula las comisiones según los contratos establecidos.  
✔️ Aplica descuentos cuando corresponda.  
✔️ Genera un archivo **Excel (.xlsx)** con el resumen de las comisiones.  
✔️ Envía un correo con el informe adjunto.  
✔️ Almacena los resultados en la carpeta **Resultados/**.  

## 🛠️ Tecnologías Utilizadas  
- **Python 3.8+**  
- **SQLite** para manejo de base de datos  
- **Pandas** para análisis de datos  
- **Openpyxl** para generar archivos Excel  
- **smtplib & email** para el envío de correos  

## 📂 Estructura del Proyecto  

PRUEBA_ECOSISTEMAS
│── BATSEJ_OPEN_FINANCE_S.A
│   ├── data
│   │   ├── database.sqlite
│   │   ├── Salidas
│   ├── src
│   │   ├── __pycache__
│   │   ├── calculo_comision.py
│   │   ├── cargar_bd.py
│   │   ├── enviar_correo.py
│   │   ├── exploracion_bd.py
│   │   ├── generar_reportes.py
│   │   ├── inspeccion_tablas.py
│   │   ├── main.py
│   ├── venv
│   │   ├── Include
│   │   ├── Lib
│   │   ├── Scripts
│   │   ├── pyvenv.cfg
│   ├── .gitignore
│   ├── comisionador.bat
│   ├── requirements.txt
│   ├── README.md


## ⚙️ Instalación  
Sigue estos pasos para ejecutar el proyecto en tu máquina local.  

### 1️⃣ Clonar el Repositorio  
```sh
git clone https://github.com/valenttp13/BATSET-OPEN-FINANCE.git
cd BATSEJ_OPEN_FINANCE_S.A
