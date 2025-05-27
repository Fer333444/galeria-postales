from flask import Flask, send_from_directory, render_template_string, request, redirect
from urllib.parse import quote
from flask import request
import os
import re

app = Flask(__name__)
CARPETA_GALERIAS = "galerias"
@app.route('/buscar')
def buscar_codigo():
    codigo = request.args.get("codigo", "").replace("#", "").strip()
    try:
        with open("codigos_postales.txt", "r") as f:
            for linea in f:
                if linea.startswith(codigo):
                    _, imagen = linea.strip().split(" ", 1)
                    return redirect(f"/postal/cliente123/postcard_final_{imagen}")
        return "<h1 style='color:red;'>❌ Código no encontrado</h1>"
    except Exception as e:
        return f"<h1 style='color:red;'>❌ Error al buscar el código</h1><p>{e}</p>"

@app.route('/')
def inicio():
    return redirect('/galeria/cliente123')

@app.route('/galeria/<cliente>')
def galeria(cliente):
    carpeta = os.path.join("galerias", cliente)
    if not os.path.exists(carpeta):
        return f"<h1>Galería '{cliente}' no encontrada</h1>", 404

    imagenes = [f for f in os.listdir(carpeta) if f.startswith("postcard_final") and f.endswith(".jpg")]

    html = f"""
    <html>
      <head>
        <title>GALERIA POST CARD</title>
        <style>
          body {{
            font-family: sans-serif;
            background: #f8f8f8;
            text-align: center;
          }}
          .galeria {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
            margin-top: 30px;
          }}
          .postal img {{
            width: 100%;
            max-width: 280px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
          }}
          .busqueda {{
            margin-top: 15px;
            margin-bottom: 10px;
          }}
          input[type=text] {{
            padding: 10px;
            font-size: 16px;
            border: 2px solid #ccc;
            border-radius: 6px;
          }}
          button {{
            padding: 10px 20px;
            background: #333;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 6px;
            cursor: pointer;
          }}
        </style>
      </head>
      <body>
        <h2>📸 GALERIA POST CARD</h2>
        <div class="busqueda">
          <form action="/buscar">
            <input type="text" name="codigo" placeholder="Ingresa código de postal" oninput="this.value=this.value.replace('#', '')" />
            <button type="submit">Buscar</button>
          </form>
        </div>
        <p style="color:gray;">Toca una postal, mantenla presionada y guárdala en tu galería 📅</p>
        <div class="galeria">
          {"".join(f"<a href='/postal/{cliente}/{quote(img)}'><div class='postal'><img src='/galeria/{cliente}/{quote(img)}'></div></a>" for img in imagenes)}
        </div>
      </body>
    </html>
    """
    return render_template_string(html)

@app.route('/galeria/<cliente>/<filename>')
def imagen(cliente, filename):
    return send_from_directory(os.path.join(CARPETA_GALERIAS, cliente), filename)

@app.route('/postal/<cliente>/<imagen>')
def ver_postal(cliente, imagen):
    ruta = f"/galeria/{cliente}/{imagen}"

    html = f"""
    <html>
      <head>
        <title>Postal completa</title>
        <style>
          body {{
            margin: 0;
            background: #000;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            min-height: 100vh;
            padding-top: 30px;
          }}
          .postal img {{
            width: 90%;
            max-width: 400px;
            border-radius: 12px;
            box-shadow: 0 0 25px rgba(0,0,0,0.9);
            margin-bottom: 20px;
          }}
          .btn {{
            display: inline-block;
            margin: 10px;
            padding: 12px 30px;
            border-radius: 6px;
            font-size: 16px;
            font-weight: bold;
            color: white;
            text-decoration: none;
          }}
          .btn-green {{ background-color: #28a745; }}
          .btn-blue {{ background-color: #007bff; }}
        </style>
      </head>
      <body>
        <div class="postal">
          <img src="{ruta}" />
        </div>
        <a href="{ruta}" download class="btn btn-green">⬇️ DOWNLOAD</a>
        <a href="/galeria/{cliente}" class="btn btn-blue">⬅️ BACK</a>
      </body>
    </html>
    """
    return html

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
