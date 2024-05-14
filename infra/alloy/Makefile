create-namespace:
	- kubectl create namespace alloy

setup: create-namespace
	- kubectl create secret generic grafana-cloud-credentials-metrics --namespace alloy --from-literal=username="${GCM_USERNAME}" --from-literal=password="${GCM_PASSWORD}"
	- kubectl create secret generic grafana-cloud-credentials-logs --namespace alloy --from-literal=username="${GCL_USERNAME}" --from-literal=password="${GCL_PASSWORD}"
	helm upgrade --install --namespace alloy-stateful alloy-stateful grafana/alloy -f values-metrics.yaml
	helm upgrade --install --namespace alloy-daemon alloy-daemon grafana/alloy -f values-logs.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=alloy -n alloy --timeout=120s
