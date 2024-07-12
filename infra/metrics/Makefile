.PHONY: setup
setup:
	helm upgrade --install mimir grafana/mimir-distributed --namespace metrics --create-namespace
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=mimir -n metrics --timeout=300s