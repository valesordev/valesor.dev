.PHONY: create-namespace
create-namespace:
	- kubectl create namespace eventstore

.PHONY: install-operator
install-operator:
	helm upgrade my-strimzi-cluster-operator --set watchedNamespaces="eventstore" --namespace eventstore oci://quay.io/strimzi-helm/strimzi-kafka-operator

.PHONY: setup
setup: create-namespace install-operator
	kubectl apply -k .