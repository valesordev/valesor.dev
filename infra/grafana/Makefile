.PHONY: setup
setup:
	helm upgrade --install viz --create-namespace --namespace viz grafana/grafana --values ./grafana-values.yaml
	helm upgrade --install search --namespace search grafana/loki --values ./loki-values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=search -n search --timeout=300s
	kubectl apply -k .
