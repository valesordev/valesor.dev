PACKAGE_NAMESPACE=ghcr.com/valesordev/valesor.dev
BINARY_NAME=kafka-loader

clean:
	kubectl delete -f job.yaml
	kubectl delete pod -l 'batch.kubernetes.io/job-name=kafka-producer-job'

docker-build:
	docker build -t $(PACKAGE_NAMESPACE)/$(BINARY_NAME) .

kind-load: docker-build
	kind load docker-image $(PACKAGE_NAMESPACE)/$(BINARY_NAME)

k8s-run: clean kind-load
	kubectl apply -f job.yaml