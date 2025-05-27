from flask import Flask, send_from_directory, render_template_string, redirect
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
            padding-top: 20px;
          }}
          .postal img {{
            width: 95%;
            max-width: 700px;
            border-radius: 12px;
            box-shadow: 0 0 25px rgba(0,0,0,0.9);
            margin-bottom: 30px;
          }}
          .botones {{
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
          }}
          .btn {{
            padding: 16px 32px;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            color: white;
            text-decoration: none;
            text-align: center;
            min-width: 140px;
          }}
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
