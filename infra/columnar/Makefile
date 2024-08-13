.PHONY: setup
setup:
	helm upgrade --install pinot pinot/pinot \
		--create-namespace \
		-n columnar \
		--set cluster.name=pinot \
		--set server.replicaCount=2
