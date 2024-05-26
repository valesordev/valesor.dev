create-namespace:
	- kubectl create namespace alloy

setup: create-namespace
	- kubectl create secret generic grafana-cloud-credentials-metrics --namespace alloy --from-literal=username="${GCM_USERNAME}" --from-literal=password="${GCM_PASSWORD}" --from-literal=host="${GCM_HOST}"
	- kubectl create secret generic grafana-cloud-credentials-logs --namespace alloy --from-literal=username="${GCL_USERNAME}" --from-literal=tenantId="${GCL_USERNAME}" --from-literal=password="${GCL_PASSWORD}" --from-literal=host="${GCL_HOST}"
	- kubectl create secret generic grafana-cloud-credentials-traces --namespace alloy --from-literal=username="${GCT_USERNAME}" --from-literal=password="${GCT_PASSWORD}" --from-literal=host="${GCT_HOST}"
	helm upgrade --install --atomic --timeout 600s grafana-k8s-monitoring grafana/k8s-monitoring --namespace "alloy" --values k8s-monitoring-values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=grafana-k8s-monitoring -n alloy --timeout=120s
	kubectl apply -k .
