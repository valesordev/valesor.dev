.PHONY: helm
helm: update cert-manager

.PHONY: update
update: kind
	helm repo update
	
.PHONY: cert-manager
cert-manager: kind
	helm upgrade --install --atomic --timeout 120s cert-manager jetstack/cert-manager --set installCRDs=true

.PHONY: kind
kind:
	kind create cluster --config kind-cluster.yaml

.PHONY: setup
setup: helm
	kubectl apply -k .
	kubectl wait --namespace ingress-nginx \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=controller \
		--timeout=90s