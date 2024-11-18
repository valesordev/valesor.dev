setup: create-buckets
	helm upgrade --install search --create-namespace --namespace search grafana/loki --values ./loki-values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=search -n search --timeout=300s

create-buckets:
	kubectl apply -f create-loki-buckets-job.yaml

clean-bucket-jobs:
	- kubectl delete -f create-loki-buckets-job.yaml

clean: clean-bucket-jobs
	- kubectl delete namespace search

.PHONY: setup clean clean-bucket-jobs create-buckets
