from PIL import Image, ImageDraw, ImageFont
import os
import uuid

# Carpeta y fondo
carpeta = "galerias/cliente123"
fondo = os.path.join(carpeta, "postal.jpg")

# Coordenadas para imagen
x, y = 110, 200
w, h = 520, 680

# Fuente para el código (usa una genérica del sistema si no tienes ttf personalizada)
try:
    fuente = ImageFont.truetype("arial.ttf", 24)
except:
    fuente = ImageFont.load_default()

def generar_postal(nombre_img):
    if nombre_img.startswith("postcard_final_") or not nombre_img.lower().endswith(".jpg"):
        return  # ignora postales ya procesadas o archivos inválidos

    ruta_img = os.path.join(carpeta, nombre_img)
    salida = os.path.join(carpeta, f"postcard_final_{nombre_img}")
    fondo_postal = Image.open(fondo).convert("RGB")
    imagen = Image.open(ruta_img).convert("RGB")
    imagen = imagen.resize((w, h), Image.LANCZOS)

    fondo_postal.paste(imagen, (x, y))

    # Código único
    codigo = str(uuid.uuid4())[:8]
    draw = ImageDraw.Draw(fondo_postal)
    draw.text((x, y + h + 10), f"#{codigo}", fill="black", font=fuente)

    fondo_postal.save(salida)
    print(f"✅ Postal generada con código #{codigo}: {salida}")

    # Guardar código para futuras búsquedas
    with open("codigos_postales.txt", "a") as f:
        f.write(f"{codigo},{os.path.basename(salida)}\n")
