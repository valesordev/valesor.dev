create-namespace:
	- kubectl create namespace tabular

setup: create-namespace
	kubectl apply -k .
	kubectl wait --for=condition=Ready pods -l app.kubernetes.io/instance=postgres -n tabular --timeout=300s