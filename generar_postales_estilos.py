from PIL import Image, ImageDraw, ImageFont
import os

# Ruta a la carpeta del cliente
carpeta = "galerias/cliente123"
fondo = os.path.join(carpeta, "postal.jpg")

# Coordenadas exactas del recuadro
x = 45
y = 58
w = 285
h = 345

# Archivos reales de imágenes con estilo
imagenes = [
    "pixel.jpg",
    "dragon.jpg",
    "animado.jpg"
]

for archivo in imagenes:
    ruta_imagen = os.path.join(carpeta, archivo)
    salida = os.path.join(carpeta, f"postcard_final_{archivo}")

    try:
        fondo_postal = Image.open(fondo).convert("RGB")
        imagen = Image.open(ruta_imagen).convert("RGB")
        imagen = imagen.resize((w, h), Image.LANCZOS)

        # Pegamos imagen encima del fondo postal
        fondo_postal.paste(imagen, (x, y))

        # Guardamos imagen final
        fondo_postal.save(salida)
        print(f"✅ Postal generada: {salida}")

    except Exception as e:
        print(f"❌ Error con {archivo}: {e}")
