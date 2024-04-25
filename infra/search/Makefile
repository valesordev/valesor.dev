.PHONY: create-namespace
create-namespace:
	- kubectl create namespace search

.PHONY: setup
setup: create-namespace
	helm install search --namespace search grafana/loki --values ./loki-values.yaml
