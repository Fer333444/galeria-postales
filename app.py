from flask import Flask, send_from_directory, render_template_string
import os

app = Flask(__name__)
CARPETA_GALERIAS = "galerias"

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
            max-width: 600px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
          }}
        </style>
      </head>
      <body>
        <h2>📸 GALERIA POST CARD</h2>
        <p style="color:gray;">Toca una postal, mantenla presionada y guárdala en tu galería 📥</p>
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
            max-width: 500px;
            border-radius: 12px;
            box-shadow: 0 0 25px rgba(0,0,0,0.9);
            margin-bottom: 30px;
          }}
          .btn {{
            display: block;
            margin: 10px auto;
            padding: 18px 36px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-decoration: none;
            text-align: center;
            width: 250px;
          }}
          .btn-green {{
            background-color: #28a745;
          }}
          .btn-blue {{
            background-color: #007bff;
          }}
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
from flask import redirect

@app.route('/')
def inicio():
    return redirect('/galeria/cliente123')
@app.route('/galeria/<cliente>')
def galeria(cliente):
    # tu código de galería aquí...

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
