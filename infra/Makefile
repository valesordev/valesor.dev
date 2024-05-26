.PHONY: setup-k8s
setup-k8s:
	cd k8s && make setup

# .PHONY: setup-metrics
# setup-metrics:
# 	cd metrics && make setup

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

.PHONY: setup
setup: setup-k8s setup-eventstore setup-search setup-cache setup-tabular setup-alloy
