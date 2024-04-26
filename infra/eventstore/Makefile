.PHONY: create-namespace
create-namespace:
	- kubectl create namespace eventstore

.PHONY: install-operator
install-operator:
	helm upgrade --install my-strimzi-cluster-operator --set watchedNamespaces="eventstore" --namespace eventstore oci://quay.io/strimzi-helm/strimzi-kafka-operator
	kubectl wait --for=condition=Ready pods -l strimzi.io/kind=cluster-operator --timeout=120s -n eventstore

.PHONY: setup
setup: create-namespace install-operator
	kubectl apply -k .
	sleep 10s
	kubectl wait --for=condition=Ready pods -l strimzi.io/kind=Kafka -n eventstore --timeout=300s
	kubectl wait --for=condition=Ready pods -l strimzi.io/kind=KafkaConnect -n eventstore --timeout=300s