helm: update cert-manager prometheus-operator-crds

update: kind helm-repos
	helm repo update

helm-repos:
	helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
	helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	helm repo add grafana https://grafana.github.io/helm-charts
	helm repo add jetstack https://charts.jetstack.io
	helm repo add pinot https://raw.githubusercontent.com/apache/pinot/master/helm
	
cert-manager: kind
	helm upgrade --install --atomic --timeout 120s cert-manager jetstack/cert-manager --set crds.enabled=true

prometheus-operator-crds: kind
	helm upgrade --install prometheus-operator-crds prometheus-community/prometheus-operator-crds

kind:
	@kubectl cluster-info >/dev/null 2>&1 || \
		kind create cluster --config kind-cluster.yaml

setup: helm
	kubectl apply -k .
	kubectl wait --namespace ingress-nginx \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=controller \
		--timeout=90s

clean:
	kind delete cluster

dev: setup

.PHONY: helm update cert-manager kind setup clean helm-repos dev
