.PHONY: create-namespace
create-namespace:
	- kubectl create namespace search

.PHONY: setup
setup: create-namespace
	helm upgrade --install search --namespace search grafana/loki --values ./loki-values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=search -n search --timeout=300s
	kubectl apply -k .
