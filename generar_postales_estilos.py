import json
import os
import hashlib
from PIL import Image, ImageDraw, ImageFont

# Ruta
carpeta = "galerias/cliente123"
fondo = os.path.join(carpeta, "postal.jpg")

# Coordenadas imagen sobre postal
x, y = 110, 200
w, h = 520, 680

# Cargar códigos previos
json_codigos = "codigos.json"
if os.path.exists(json_codigos):
    with open(json_codigos, "r") as f:
        codigos = json.load(f)
else:
    codigos = {}

# Función principal
def generar_postal(imagen):
    if imagen.startswith("postcard_final_") or not imagen.lower().endswith(".jpg"):
        return

    ruta_imagen = os.path.join(carpeta, imagen)
    salida = os.path.join(carpeta, f"postcard_final_{imagen}")

    try:
        fondo_postal = Image.open(fondo).convert("RGB")
        img = Image.open(ruta_imagen).convert("RGB")
        img = img.resize((w, h), Image.LANCZOS)

        fondo_postal.paste(img, (x, y))

        # ✅ Código hash único por imagen
        codigo = "#" + hashlib.md5(imagen.encode()).hexdigest()[:8]
        font = ImageFont.truetype("arial.ttf", 22)
        draw = ImageDraw.Draw(fondo_postal)
        draw.text((40, 420), codigo, fill="black", font=font)

        fondo_postal.save(salida)
        print(f"✅ Postal guardada como: {salida}")

        # ✅ Guardar en archivo JSON
        codigos[codigo] = f"postcard_final_{imagen}"
        with open(json_codigos, "w") as f:
            json.dump(codigos, f)

    except Exception as e:
        print(f"❌ Error con {imagen}: {e}")
import hashlib

# Al final de tu bucle for:
    # Código hash único por imagen
    hash_codigo = hashlib.sha1(archivo.encode()).hexdigest()[:8]
    
    # Dibujar código en la postal
    draw = ImageDraw.Draw(fondo_postal)
    font = ImageFont.truetype("arial.ttf", 24)
    draw.text((20, fondo_postal.height - 40), f"#{hash_codigo}", fill="black", font=font)

    # Guardar relación código <-> nombre
    with open("codigos_postales.txt", "a") as f:
        f.write(f"{hash_codigo}|{os.path.basename(salida)}\n")
