# Variables
BACKEND_IMAGE_NAME := videogallery-backend
FRONTEND_IMAGE_NAME := videogallery-frontend
DOCKER_COMPOSE_FILE := compose.yaml

# Targets
build-backend-image:
	docker build -t $(BACKEND_IMAGE_NAME) backend

build-frontend-image:
	docker build -t $(FRONTEND_IMAGE_NAME) frontend

build-images: build-backend-image build-frontend-image

run:
	docker-compose -f $(DOCKER_COMPOSE_FILE) up

clean:
	docker-compose -f $(DOCKER_COMPOSE_FILE) down --rmi all --remove-orphans
	docker rmi $(BACKEND_IMAGE_NAME) $(FRONTEND_IMAGE_NAME)

.PHONY: build-backend-image build-frontend-image build-images run clean
