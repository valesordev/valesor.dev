create-namespace:
	kubectl create namespace alloy

setup: create-namespace
	helm upgrade --install --namespace alloy alloy grafana/alloy -f values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=alloy -n alloy --timeout=120s
