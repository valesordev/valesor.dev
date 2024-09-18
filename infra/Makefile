# List all components here
COMPONENTS := k8s object metrics search tabular eventstore columnar cache alloy identity 

# General setup target
setup: $(addprefix setup-, $(COMPONENTS))

dev: $(addprefix dev-, $(COMPONENTS))

clean: $(addprefix clean-, $(COMPONENTS))

# Pattern rule for setup
setup-%:
	cd $* && make setup

clean-%:
	cd $* && make clean

.PHONY: all clean setup-infra setup-app dev-infra dev-app
