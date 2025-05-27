from PIL import Image, ImageDraw, ImageFont
import os
import hashlib

carpeta = "galerias/cliente123"
fondo = os.path.join(carpeta, "postal.jpg")

# Coordenadas del recuadro
x = 110
y = 200
w = 520
h = 680

# Ruta al archivo que guardará los códigos únicos
archivo_codigos = "codigos_postales.txt"

def generar_postal(archivo):
    if archivo.startswith("postcard_final_") or not archivo.lower().endswith(".jpg"):
        return  # Ignora archivos ya procesados o con extensión incorrecta

    ruta_imagen = os.path.join(carpeta, archivo)
    salida = os.path.join(carpeta, f"postcard_final_{archivo}")

    try:
        fondo_postal = Image.open(fondo).convert("RGB")
        imagen = Image.open(ruta_imagen).convert("RGB")
        imagen = imagen.resize((w, h), Image.LANCZOS)

        # Pegar imagen en el fondo
        fondo_postal.paste(imagen, (x, y))

        # Generar código único
        hash_codigo = hashlib.sha1(archivo.encode()).hexdigest()[:8]

        # Agregar texto con código en la esquina inferior izquierda
        draw = ImageDraw.Draw(fondo_postal)
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except:
            font = ImageFont.load_default()

        draw.text((20, fondo_postal.height - 40), f"#{hash_codigo}", fill="black", font=font)

        # Guardar postal final
        fondo_postal.save(salida)
        print(f"✅ Postal generada: {salida}")

        # Guardar código en archivo
        with open(archivo_codigos, "a") as f:
            f.write(f"{hash_codigo}|{os.path.basename(salida)}\n")

    except Exception as e:
        print(f"❌ Error generando postal de {archivo}: {e}")
