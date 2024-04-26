.PHONY: setup
setup:
	helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack --namespace prometheus --create-namespace --values ./kube-p8s-stack-values.yaml
	kubectl wait --for=condition=Ready pods -l  app.kubernetes.io/name=kube-prometheus-stack-prometheus-operator -n prometheus
	kubectl apply -k .