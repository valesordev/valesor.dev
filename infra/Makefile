.PHONY: setup-k8s
setup-k8s:
	cd k8s && make setup

.PHONY: setup-metrics
setup-metrics:
	cd metrics && make setup

.PHONY: setup-identity
setup-identity:
	cd identity && make setup

.PHONY: setup-eventstore
setup-eventstore:
	cd eventstore && make setup

.PHONY: setup-search
setup-search:
	cd search && make setup

.PHONY: setup-alloy
setup-alloy:
	cd alloy && make setup

.PHONY: setup-cache
setup-cache:
	cd cache && make setup

.PHONY: setup-tabular
setup-tabular:
	cd tabular && make setup

.PHONY: setup-columnar
setup-columnar:
	cd columnar && make setup

.PHONY: setup
setup: setup-k8s setup-tabular setup-identity setup-eventstore setup-metrics setup-search setup-columnar setup-cache setup-alloy 
