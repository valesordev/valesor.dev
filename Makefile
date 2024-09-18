all: clean setup-infra setup-app

clean-%:
	cd $* && make clean

# Generalized setup target for components
setup-%:
	cd $* && make setup

dev-%:
	cd $* && make dev

.PHONY: all clean setup-infra setup-app dev-app

