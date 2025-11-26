from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "clave-super-secreta"

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMSG DevOps Mejorado</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
        body {
            background: radial-gradient(circle, #0b0f0c, #000000);
            color: #e3ffe3;
            font-family: 'Arial', sans-serif;
        }

        .card {
            background: rgba(10, 15, 10, 0.9);
            border: 1px solid #00ff88;
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.3);
        }

        h2 {
            color: #00ff88;
            font-weight: 700;
            letter-spacing: 2px;
            text-shadow: 0 0 10px #00ff88;
        }

        .form-control {
            background: #0d1510;
            border: 1px solid #008a55;
            color: #baffd5;
        }

        .form-control:focus {
            border-color: #00ff88;
            box-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
            background: #0f1f17;
            color: #e2ffe9;
        }

        .btn-primary {
            background-color: #00ff88;
            border: none;
            color: black;
            font-weight: bold;
            box-shadow: 0 0 10px #00ff88;
        }

        .btn-primary:hover {
            background-color: #00cc6b;
            box-shadow: 0 0 15px #00ff88;
        }

        .btn-secondary {
            background-color: #1d1d1d;
            border: 1px solid #00ff88;
            color: #00ff88;
        }

        .btn-secondary:hover {
            background-color: #111;
            color: #00ffaa;
        }

        .btn-dark {
            background-color: #00331f;
            border: 1px solid #00ff88;
            color: #00ff88;
        }

        .btn-dark:hover {
            background-color: #004d2c;
            box-shadow: 0 0 10px #00ff88;
        }

        .alert-info {
            background-color: rgba(0, 255, 136, 0.1);
            border-left: 4px solid #00ff88;
            color: #baffd5;
        }
    </style>
</head>
<body class="bg-light">

<div class="container py-5">
    <div class="card shadow p-4" style="max-width: 600px; margin:auto;">
        <h2 class="text-center mb-4">Jary Cuji</h2>

        <form method="POST" action="/">
            <label class="form-label">Ingrese su nombre:</label>
            <input name="nombre" class="form-control mb-3" required />

            <div class="d-flex gap-2">
                <button class="btn btn-primary w-50" name="accion" value="saludar">Enviar</button>
                <button class="btn btn-secondary w-50" name="accion" value="limpiar">Limpiar</button>
            </div>

            <button class="btn btn-dark w-100 mt-3" name="accion" value="contar">Contar Click</button>
        </form>

        {% if mensaje %}
        <div class="alert alert-info mt-4">
            {{ mensaje }}
        </div>
        {% endif %}
    </div>
</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    mensaje = None

    if "contador" not in session:
        session["contador"] = 0

    if request.method == "POST":
        accion = request.form.get("accion")
        nombre = request.form.get("nombre")

        if accion == "saludar":
            mensaje = f"Hola {nombre}. Bienvenido al proyecto."

        elif accion == "limpiar":
            session["contador"] = 0
            mensaje = "El formulario ha sido limpiado correctamente."

        elif accion == "contar":
            session["contador"] += 1
            mensaje = f"{nombre}, llevas {session['contador']} clic(s)."

    return render_template_string(HTML, mensaje=mensaje)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8816)
