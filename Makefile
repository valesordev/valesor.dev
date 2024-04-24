.PHONY: clean
clean:
	kind delete cluster

.PHONY: setup
setup:
	cd infra/k8s && make setup

.PHONY: setup-metrics
setup-metrics:
	cd infra/metrics && make setup

.PHONY: setup-eventstore
setup-eventstore:
	cd infra/eventstore && make setup

.PHONY: all
all: clean setup