.PHONY: setup
setup:
	- kubectl create namespace minio-tenant
	kubectl kustomize github.com/minio/operator\?ref=v6.0.3 | kubectl apply -f -
	kubectl apply -k github.com/minio/operator/examples/kustomization/bases


