setup:
	- kubectl create namespace minio-tenant
	kubectl kustomize github.com/minio/operator\?ref=v6.0.3 | kubectl apply -f -
	kubectl apply -k .

clean:
	- kubectl delete namespace minio-tenant
	- kubectl delete namespace minio-operator

.PHONY: setup clean
