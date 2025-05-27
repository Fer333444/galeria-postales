from PIL import Image
import os

# Rutas
carpeta = "galerias/cliente123"
plantilla = os.path.join(carpeta, "postal.jpg")

# Posición y tamaño de la foto dentro del postcard
x, y = 110, 200
w, h = 520, 680

# Abrimos la plantilla base una vez
for archivo in os.listdir(carpeta):
    if archivo.lower().endswith(".jpg") and not archivo.startswith("postcard_final") and archivo != "postal.jpg":
        nombre_final = f"postcard_final_{archivo}"
        ruta_final = os.path.join(carpeta, nombre_final)

        if os.path.exists(ruta_final):
            continue  # Ya fue generado

        print(f"🖼️ Generando postal de: {archivo}")

        try:
            fondo = Image.open(plantilla).convert("RGB")
            imagen = Image.open(os.path.join(carpeta, archivo)).convert("RGB")
            imagen = imagen.resize((w, h))

            fondo.paste(imagen, (x, y))
            fondo.save(ruta_final)
            print(f"✅ Postal guardada como: {nombre_final}")
        except Exception as e:
            print(f"❌ Error con {archivo}: {e}")
