from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import qrcode

# Autenticación rápida
gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # Abre el navegador para autorizar

drive = GoogleDrive(gauth)

# Imagen que deseas subir (ajústalo al nombre real que tengas)
archivo_local = "C:/FotosEstilizadas/sepia_20141129_123316 - copia.jpg"  # ← cambia este nombre si hace falta

# Subir a Google Drive
f = drive.CreateFile({'title': 'sepia_foto.jpg'})
f.SetContentFile(archivo_local)
f.Upload()

# Compartir públicamente
f['shared'] = True
f.Upload()

# Obtener link
link_publico = f['alternateLink']
print(f"✅ Link público: {link_publico}")

# Crear QR
qr = qrcode.make(link_publico)
qr.save("C:/QRs/qr_drive.png")
print("✅ Código QR generado en: C:/QRs/qr_drive.png")
