.PHONY: setup
setup:
	helm upgrade --install --atomic --timeout 120s ksm prometheus-community/kube-state-metrics \
		--values kube-state-metrics.yaml
	kubectl wait --for=condition=Ready pods \
		-n default --timeout=300s \
		-l app.kubernetes.io/instance=ksm 
	- kubectl create secret generic grafana-cloud-credentials \
		--from-literal=CLOUD_API_KEY="${GRAFANA_CLOUD_API_KEY}" \
		--from-literal=OTEL_TENANT="${GCO_USERNAME}" \
		--from-literal=OTEL_HOST="${GCO_HOST}"
	helm upgrade --install --atomic --timeout 120s node-exporter prometheus-community/prometheus-node-exporter \
		--values prometheus-node-exporter.yaml
	helm upgrade --install --atomic --timeout 120s opentelemetry-operator open-telemetry/opentelemetry-operator \
		--set "manager.collectorImage.repository=otel/opentelemetry-collector-k8s" \
		--set admissionWebhooks.certManager.enabled=true
	kubectl apply -f otelcol-cluster-role.yaml
	kubectl apply -f otelcol-cluster-role-binding.yaml
	kubectl apply -f otel-collector.yaml

