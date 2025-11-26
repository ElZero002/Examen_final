# Nombre del proyecto / imagen
APP_NAME=finaljary
USER=elzero002
IMAGE=ghcr.io/$(USER)/$(APP_NAME):latest

# Puerto interno donde escucha Flask
PORT=8816

# Ejecutar localmente sin Docker
run:
	python app.py

# Construir imagen Docker local
build:
	docker build -t $(APP_NAME) .

# Ejecutar contenedor local para pruebas
run-docker:
	docker run -p $(PORT):$(PORT) $(APP_NAME)

# Subir imagen al GHCR (para que Swarm la use)
push:
	docker tag $(APP_NAME) $(IMAGE)
	docker push $(IMAGE)

# Limpiar basura
clean:
	docker system prune -f
