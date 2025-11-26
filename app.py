from flask import Flask, render_template_string, request, session

app = Flask(__name__)
app.secret_key = "clave-super-secreta"  # necesaria para usar session

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AMSG DevOps Mejorado</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">

<div class="container py-5">
    <div class="card shadow p-4" style="max-width: 600px; margin:auto;">
        <h2 class="text-center mb-4">Proyecto AMSG DevOps Mejorado</h2>

        <form method="POST" action="/">
            <label class="form-label">Ingrese su nombre:</label>
            <input name="nombre" class="form-control mb-3" required />

            <div class="d-flex gap-2">
                <button class="btn btn-primary w-50" name="accion" value="saludar">Enviar</button>
                <button class="btn btn-secondary w-50" name="accion" value="limpiar">Limpiar</button>
            </div>

            <!-- 🔥 BOTÓN NUEVO PARA CONTAR CLICKS -->
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

    # Inicializar contador
    if "contador" not in session:
        session["contador"] = 0

    if request.method == "POST":
        accion = request.form.get("accion")
        nombre = request.form.get("nombre")

        if accion == "saludar":
            mensaje = f"Hola {nombre}. Bienvenido."

        elif accion == "limpiar":
            session["contador"] = 0
            mensaje = "El formulario ha sido limpiado correctamente."

        elif accion == "contar":
            session["contador"] += 1
            mensaje = f"{nombre}, llevas {session['contador']} clic(s)."

    return render_template_string(HTML, mensaje=mensaje)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8816)
