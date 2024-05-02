.PHONY: clean
clean:
	kind delete cluster

.PHONY: setup-infra
setup-infra:
	cd infra && make setup

.PHONY: setup-app
setup-app:
	cd app && make setup

.PHONY: all
all: clean setup-infra setup-app