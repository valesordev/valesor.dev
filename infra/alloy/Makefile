create-namespace:
	- kubectl create namespace alloy

setup: create-namespace
	- kubectl create secret generic grafana-cloud-credentials-metrics --namespace alloy --from-literal=username="${GCM_USERNAME}" --from-literal=password="${GCM_PASSWORD}"
	- kubectl create secret generic grafana-cloud-credentials-logs --namespace alloy --from-literal=username="${GCL_USERNAME}" --from-literal=password="${GCL_PASSWORD}"
	- kubectl create secret generic grafana-cloud-credentials-traces --namespace alloy --from-literal=username="${GCM_USERNAME}" --from-literal=password="${GCM_PASSWORD}"
	helm upgrade --install --atomic --timeout 300s grafana-k8s-monitoring grafana/k8s-monitoring --namespace "alloy" --values k8s-monitoring-values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=grafana-k8s-monitoring -n alloy --timeout=120s
