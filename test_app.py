from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_saludar():
    client = app.test_client()
    res = client.post("/", data={"accion": "saludar", "nombre": "Jary"})
    assert b"Hola Jary. Bienvenido al proyecto." in res.data

def test_contar():
    client = app.test_client()
    res = client.post("/", data={"accion": "contar", "nombre": "Jary"})
    assert b"1 clic" in res.data

def test_limpiar():
    client = app.test_client()
    client.post("/", data={"accion": "contar", "nombre": "Jary"})
    res = client.post("/", data={"accion": "limpiar", "nombre": "Jary"})
    assert b"El formulario ha sido limpiado correctamente." in res.data
