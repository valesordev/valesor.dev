setup:
	- kubectl create namespace minio-tenant
	kubectl kustomize github.com/minio/operator\?ref=v6.0.3 | kubectl apply -f -
	kubectl wait --for=condition=ready pod -l app.kubernetes.io/instance=minio-operator -n minio-operator --timeout=60s
	kubectl apply -k .
	@while true; do \
		CURRENT_STATE=$$(kubectl get tenant s3-infra -n minio-tenant -o jsonpath='{.status.currentState}'); \
		if [ "$$CURRENT_STATE" = "Initialized" ]; then \
			break; \
		fi; \
		sleep 5; \
	done
	#kubectl wait --for=condition=ready pod -l v1.min.io/tenant=s3-infra -n minio-tenant --timeout=60s

clean:
	- kubectl delete namespace minio-tenant
	- kubectl delete namespace minio-operator

.PHONY: setup clean
