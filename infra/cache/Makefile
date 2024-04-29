install-operator:
	# Install the CRD and Operator
	kubectl apply -f https://raw.githubusercontent.com/dragonflydb/dragonfly-operator/main/manifests/dragonfly-operator.yaml

setup: install-operator
	kubectl create namespace cache
	kubectl apply -k .