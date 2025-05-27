from PIL import Image, ImageDraw, ImageFont
import os
import uuid

def generar_postal(nombre_imagen):
    carpeta = "galerias/cliente123"
    fondo_path = os.path.join(carpeta, "postal.jpg")
    imagen_path = os.path.join(carpeta, nombre_imagen)

    if not os.path.exists(fondo_path) or not os.path.exists(imagen_path):
        print("❌ No se encontró postal.jpg o la imagen original.")
        return

    # Abrir imágenes
    fondo = Image.open(fondo_path).convert("RGB")
    imagen = Image.open(imagen_path).convert("RGB")

    # Redimensionar imagen al espacio en la postal
    x, y, w, h = 110, 200, 520, 680
    imagen = imagen.resize((w, h), Image.LANCZOS)

    # Pegar imagen sobre la postal
    fondo.paste(imagen, (x, y))

    # Generar código único
    codigo = str(uuid.uuid4())[:8]

    # Dibujar el código en la parte inferior izquierda
    draw = ImageDraw.Draw(fondo)
    font_path = "arial.ttf"
    if os.path.exists(font_path):
        font = ImageFont.truetype(font_path, 28)
    else:
        font = ImageFont.load_default()
    draw.text((50, 520), f"#{codigo}", fill="black", font=font)

    # Guardar postal con nuevo nombre
    salida = os.path.join(carpeta, f"postcard_final_{nombre_imagen}")
    fondo.save(salida)
    print(f"✅ Postal guardada: {salida} con código #{codigo}")
