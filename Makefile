.PHONY: clean
clean:
	kind delete cluster

.PHONY: setup-infra
setup-infra:
	cd infra && make setup

.PHONY: setup-app
setup-app:
	cd app && make setup

.PHONY: dev-app
dev-app:
	cd app && make dev

.PHONY: all
all: clean setup-infra setup-app