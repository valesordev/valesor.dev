# Variables for common values
NAMESPACE=alloy
TIMEOUT=120s

# Phony targets declaration
.PHONY: create-namespace install-otel-operator create-secrets install-k8s-monitoring apply-kustomization setup

create-namespace:
	-@kubectl get namespace $(NAMESPACE) || kubectl create namespace $(NAMESPACE)

install-otel-operator:
	helm upgrade --install opentelemetry-operator open-telemetry/opentelemetry-operator \
		--set "manager.collectorImage.repository=otel/opentelemetry-collector-k8s"
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/name=opentelemetry-operator \
		-n default --timeout=$(TIMEOUT)

create-secrets: create-namespace
	-@kubectl create secret generic grafana-cloud-credentials --namespace $(NAMESPACE) \
		--from-literal=prometheus="${GCM_USERNAME}" \
		--from-literal=loki="${GCL_USERNAME}" \
		--from-literal=tempo="${GCT_USERNAME}" \
		--from-literal=pyroscope="${GCP_USERNAME}" \
		--from-literal=fleetmanagement="${GFM_USERNAME}" \
		--from-literal=cloudKey="${GC_API_KEY}"
	-@kubectl create secret generic grafana-pdc-agent --namespace $(NAMESPACE) \
		--from-literal=token="${GC_PDC_SIGNING_TOKEN}" \
		--from-literal=hosted-grafana-id="${GC_GRAFANA_ID}" \
		--from-literal=cluster="${GC_PDC_CLUSTER}"

install-k8s-monitoring: create-namespace
	helm upgrade --install grafana-k8s-monitoring grafana/k8s-monitoring \
		--namespace "$(NAMESPACE)" --values k8s-monitoring-values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=grafana-k8s-monitoring \
		-n $(NAMESPACE) --timeout=$(TIMEOUT)

apply-kustomization:
	kubectl apply -k .
	kubectl wait --for=condition=Ready pods -l name=grafana-pdc-agent \
		-n $(NAMESPACE) --timeout=$(TIMEOUT)

# Combined setup target
setup: create-secrets install-otel-operator install-k8s-monitoring apply-kustomization

