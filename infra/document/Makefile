.PHONY: all setup clean

all: clean setup

setup:
	- kubectl create namespace document
	kubectl apply -k .

clean:
	kubectl delete namespace document
