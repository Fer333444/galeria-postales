from PIL import Image, ImageDraw, ImageFont
import os

# Coordenadas exactas del recuadro
x = 110
y = 200
w = 520
h = 680

def generar_postal(nombre_imagen):
    """
    Genera una postal a partir de la imagen recibida.
    nombre_imagen: str, el nombre de la imagen dentro de la carpeta del cliente (sin ruta completa)
    """
    carpeta = "galerias/cliente123"
    fondo = os.path.join(carpeta, "postal.jpg")
    ruta_imagen = os.path.join(carpeta, nombre_imagen)
    salida = os.path.join(carpeta, f"postcard_final_{nombre_imagen}")

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
        print(f"❌ Error con {nombre_imagen}: {e}")
