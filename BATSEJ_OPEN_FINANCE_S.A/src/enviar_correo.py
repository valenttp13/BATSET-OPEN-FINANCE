import win32com.client as win32
import os

def crear_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto=None):
    """Crea un correo en Outlook con el destinatario, asunto y cuerpo especificados.  
    Opcionalmente, adjunta un archivo si se proporciona una ruta válida."""
    outlook = win32.Dispatch('outlook.application')
    correo = outlook.CreateItem(0)
    correo.To = receptor
    correo.Subject = asunto
    correo.Body = cuerpo
    
    if ruta_adjunto and os.path.exists(ruta_adjunto):
        correo.Attachments.Add(ruta_adjunto)
    
    return correo

def enviar_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto=None):
    """Crea y envía un correo electrónico a través de Outlook.  
    Muestra un mensaje de confirmación o un error en caso de fallo."""
    try:
        correo = crear_correo_outlook(receptor, asunto, cuerpo, ruta_adjunto)
        correo.Send()
        print(f"Correo enviado exitosamente a {receptor}.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
