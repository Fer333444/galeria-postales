from flask import Flask, send_from_directory, render_template_string, request, redirect
import os

app = Flask(__name__)
CARPETA_GALERIAS = "galerias"

@app.route('/')
def inicio():
    return redirect('/galeria/cliente123')

@app.route('/galeria/<cliente>')
def galeria(cliente):
    ruta = os.path.join(CARPETA_GALERIAS, cliente)
    if not os.path.exists(ruta):
        return f"<h1>Galería '{cliente}' no encontrada</h1>", 404

    imagenes = [f for f in os.listdir(ruta) if f.startswith("postcard_final") and f.endswith(".jpg")]

    html = f"""
    <html>
      <head>
        <title>GALERIA POST CARD</title>
        <style>
          body {{ font-family: sans-serif; background: #f8f8f8; text-align: center; }}
          .galeria {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; margin-top: 30px; }}
          .postal img {{ width: 100%; max-width: 300px; border-radius: 10px; box-shadow: 0 0 15px rgba(0,0,0,0.3); }}
        </style>
      </head>
      <body>
        <h2>📸 GALERIA POST CARD</h2>
        <p style='color:gray;'>Toca una postal, mantenla presionada y guárdala en tu galería 📥</p>
        <form action="/buscar" method="get" style="margin-bottom: 20px;">
          <input type="text" name="codigo" placeholder="🔍 Código postal..." required style="padding: 10px; font-size: 16px; width: 250px;">
          <button type="submit" style="padding: 10px 20px; font-size: 16px;">Buscar</button>
        </form>
        <div class="galeria">
          {"".join(f"<a href='/postal/{cliente}/{img}'><div class='postal'><img src='/galeria/{cliente}/{img}'></div></a>" for img in imagenes)}
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
          body {{ background: #000; margin: 0; display: flex; flex-direction: column; align-items: center; padding: 20px; }}
          .postal img {{ width: 95%; max-width: 500px; border-radius: 12px; box-shadow: 0 0 25px rgba(0,0,0,0.9); margin-bottom: 20px; }}
          .botones {{ display: flex; gap: 10px; justify-content: center; }}
          .btn {{ padding: 14px 26px; font-size: 16px; font-weight: bold; border-radius: 6px; text-decoration: none; color: white; }}
          .btn-green {{ background-color: #28a745; }}
          .btn-blue {{ background-color: #007bff; }}
        </style>
      </head>
      <body>
        <div class="postal">
          <img src="{ruta}" />
        </div>
        <div class="botones">
          <a href="{ruta}" download class="btn btn-green">⬇️ DOWNLOAD</a>
          <a href="/galeria/{cliente}" class="btn btn-blue">⬅️ BACK</a>
        </div>
      </body>
    </html>
    """
    return html

@app.route('/buscar')
def buscar_postal():
    codigo = request.args.get("codigo")
    if not codigo:
        return "<h2>❌ Código no proporcionado</h2>", 400

    try:
        with open("codigos_postales.txt", "r") as f:
            for linea in f:
                if linea.startswith(codigo):
                    _, archivo = linea.strip().split(",")
                    return redirect(f"/postal/cliente123/{archivo}")
    except:
        return "<h2>❌ No se pudo acceder a la base de códigos</h2>", 500

    return f"<h2>❌ No se encontró ninguna postal con el código: {codigo}</h2>", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
