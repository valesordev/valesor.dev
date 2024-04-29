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

.PHONY: setup-search
setup-search:
	cd infra/search && make setup

.PHONY: setup-alloy
setup-alloy:
	cd infra/alloy && make setup

.PHONY: setup-cache
setup-cache:
	cd infra/cache && make setup

.PHONY: all
all: clean setup setup-metrics setup-eventstore setup-search setup-alloy setup-cache