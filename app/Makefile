.PHONY: setup-autobs
setup-autobs:
	cd autobs && make all

.PHONY: dev-autobs
dev-autobs: setup-autobs
	./autobs/autobs target dev &> /dev/null &
	./autobs/autobs gatherer dev &> /dev/null &

.PHONY: setup-viewor
setup-viewor:
	cd viewor && make setup

.PHONY: dev-viewor
dev-viewor: setup-viewor
	cd viewor && npm run dev &> /dev/null &

.PHONY: setup
setup: setup-autobs

.PHONY: dev
dev: dev-autobs dev-viewor
