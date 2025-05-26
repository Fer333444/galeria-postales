from PIL import Image
import qrcode
import socket
import os

carpeta = "galerias/cliente123"
fondo = os.path.join(carpeta, "postal.jpg")
x, y = 110, 200     # la empuja más a la izquierda y arriba
w, h = 520, 680     # la hace más ancha y más alta    # más ancho y más alto    # más ancha y más alta
imagenes = [
    ("pixel.jpg", "PIXEL ART"),
    ("dragon.jpg", "DRAGON BALL"),
    ("animado.jpg", "ESTILO ANIMADO"),
    ("puente.jpg", "PUENTE DOURO"),
    ("tv.jpg", "FÚTBOL EN CASA")  # 👈 nueva imagen
]

def obtener_ip_local():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

for nombre, estilo in imagenes:
    try:
        ruta_img = os.path.join(carpeta, nombre)
        salida = os.path.join(carpeta, f"postcard_final_{nombre}")
        base = Image.open(fondo).convert("RGB")
        foto = Image.open(ruta_img).convert("RGB").resize((w, h), Image.LANCZOS)
        base.paste(foto, (x, y))
        base.save(salida)
        print(f"✅ Postal generada: {salida}")

        ip = obtener_ip_local()
        url = f"http://{ip}:5000/postal/cliente123/postcard_final_{nombre}"
        qr = qrcode.make(url)
        qr.save(f"qr_{nombre.replace('.jpg','.png')}")
        print(f"🔗 QR generado: {url}")

    except Exception as e:
        print(f"❌ Error con {nombre}: {e}")
