# Variables for common values
NAMESPACE=alloy
TIMEOUT=120s

# Phony targets declaration
.PHONY: create-namespace install-otel-operator create-secrets install-k8s-monitoring apply-kustomization install-data-infra-monitor install-loki-meta-monitoring setup

create-namespace:
	-@kubectl get namespace $(NAMESPACE) || kubectl create namespace $(NAMESPACE)

install-otel-operator:
	helm upgrade --install opentelemetry-operator open-telemetry/opentelemetry-operator \
		--set "manager.collectorImage.repository=otel/opentelemetry-collector-k8s"
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/name=opentelemetry-operator \
		-n default --timeout=$(TIMEOUT)

create-secrets: create-namespace
	-@kubectl create secret generic grafana-cloud-credentials-metrics --namespace $(NAMESPACE) \
		--from-literal=username="${GCM_USERNAME}" \
		--from-literal=password="${GCM_PASSWORD}" \
		--from-literal=host="${GCM_HOST}" \
		--from-literal=endpoint="${GCM_ENDPOINT}"
	-@kubectl create secret generic grafana-cloud-credentials-logs --namespace $(NAMESPACE) \
		--from-literal=username="${GCL_USERNAME}" \
		--from-literal=tenantId="${GCL_USERNAME}" \
		--from-literal=password="${GCL_PASSWORD}" \
		--from-literal=host="${GCL_HOST}" \
		--from-literal=endpoint="${GCL_ENDPOINT}"
	-@kubectl create secret generic grafana-cloud-credentials-traces --namespace $(NAMESPACE) \
		--from-literal=username="${GCT_USERNAME}" \
		--from-literal=password="${GCT_PASSWORD}" \
		--from-literal=host="${GCT_HOST}" \
		--from-literal=endpoint="${GCT_ENDPOINT}"
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

install-data-infra-monitor:
	helm upgrade --install data-infrastructure-monitoring grafana/alloy \
		--namespace $(NAMESPACE) -f data-infrastructure-monitoring-values.yaml
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=data-infrastructure-monitoring \
		-n $(NAMESPACE) --timeout=$(TIMEOUT)

install-loki-meta-monitoring:
	helm upgrade --install meta-monitoring grafana/meta-monitoring \
		--create-namespace --namespace $(NAMESPACE) -f meta-monitoring-values.yaml

# Combined setup target
setup: create-secrets install-otel-operator install-k8s-monitoring apply-kustomization install-data-infra-monitor install-loki-meta-monitoring

