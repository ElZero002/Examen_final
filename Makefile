APP=usina
IMAGE_OWNER=elzero002
IMAGE_TAG=1.0.5
REGISTRY=ghcr.io
IMAGE=$(REGISTRY)/$(IMAGE_OWNER)/$(APP):$(IMAGE_TAG)

install:
	python -m pip install --upgrade pip
	if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

run:
	python app.py

test:
	pytest -v --tb=short

build:
	docker build -t $(IMAGE) .

run-docker:
	docker run -p 5000:5000 $(IMAGE)

login-ghcr:
	echo "${GHCR_PAT}" | docker login ghcr.io -u $(IMAGE_OWNER) --password-stdin

push:
	docker push $(IMAGE)

build-push: build push

deploy:
	ssh -p $(VPS_SSH_PORT) $(VPS_USER)@$(VPS_HOST) "\
		echo \"Logeando en GHCR\" && \
		echo \"$$GHCR_PAT\" | docker login ghcr.io -u $(IMAGE_OWNER) --password-stdin && \
		cd ~/despliegue && \
		docker pull $(IMAGE) && \
		docker stack rm $(APP) || true && \
		sleep 15 && \
		docker stack deploy --with-registry-auth -c stack.yml $(APP)"

upload-stack:
	scp -P $(VPS_SSH_PORT) finaljary/stack.yml $(VPS_USER)@$(VPS_HOST):~/despliegue/

full:
	make test
	make build-push
	make upload-stack
	make deploy

clean:
	docker system prune -f
