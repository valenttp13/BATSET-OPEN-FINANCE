import win32com.client as win32
import os

def crear_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto=None):
    outlook = win32.Dispatch('outlook.application')
    correo = outlook.CreateItem(0)
    correo.To = receptor
    correo.Subject = asunto
    correo.Body = cuerpo
    
    if ruta_adjunto and os.path.exists(ruta_adjunto):
        correo.Attachments.Add(ruta_adjunto)
    
    return correo

def enviar_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto=None):
    try:
        correo = crear_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto)
        correo.Send()
        print(f"Correo enviado exitosamente a {receptor}.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")