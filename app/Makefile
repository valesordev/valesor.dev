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

.PHONY: setup-event_processor
setup-event_processor:
	cd event_processor && make setup

.PHONY: dev-event_processor
dev-event_processor: setup-event_processor
	docker run -d --name flask-kafka-app -p 5000:5000 -e KAFKA_BROKER="your-kafka-broker:9092" -e OTEL_EXPORTER_OTLP_ENDPOINT="http://otel-collector:4317" valesor.dev/event_processor/flask-kafka:latest

.PHONY: setup
setup: setup-autobs

.PHONY: dev
dev: dev-autobs dev-viewor
