import qrcode

# URL pública que quieres que abra el QR (ajústala a tu ruta real en Render)
url = "https://galeria-postales.onrender.com/galeria/cliente123"

# Crear QR
qr = qrcode.make(url)

# Guardar imagen
qr.save("qr_cliente123.png")

print("✅ Código QR generado exitosamente.")
