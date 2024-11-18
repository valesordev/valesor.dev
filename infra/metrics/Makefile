setup: namespace create-bucket-role create-bucket install-mimir

install-mimir:
	- kubectl create secret generic mimir-bucket-secret --namespace metrics --from-literal=AWS_ACCESS_KEY_ID="console" --from-literal=AWS_SECRET_ACCESS_KEY="console123"
	helm upgrade --install mimir grafana/mimir-distributed --namespace metrics --create-namespace --values mimir-capped-small.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=mimir -n metrics --timeout=1200s

namespace:
	- kubectl create namespace metrics

create-bucket-role:
	kubectl apply -f create-bucket-role.yaml

create-bucket:
	kubectl apply -f create-mimir-buckets-job.yaml
	kubectl wait --for=condition=complete job -l valesor.dev/job_name=mimir-buckets -n minio-tenant --timeout=60s

clean-bucket-jobs:
	kubectl delete -f create-mimir-buckets-job.yaml
	sleep 10s

clean-bucket-roles:
	kubectl delete -f create-bucket-role.yaml
	sleep 10s

clean: clean-bucket-jobs clean-bucket-roles
	kubectl delete namespace metrics
	sleep 10s

.PHONY: setup clean
