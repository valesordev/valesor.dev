.PHONY: setup
setup:
	- kubectl create namespace identity
	kubectl apply -k .
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=keycloak -n identity --timeout=300s