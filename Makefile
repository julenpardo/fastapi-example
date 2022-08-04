.PHONY: build-image

build-image:
	docker build -t fastapi-example:$(TAG) .
	minikube image load fastapi-example:$(TAG)
