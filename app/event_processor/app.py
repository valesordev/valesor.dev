from flask import Flask, jsonify
import requests
from kafka import KafkaProducer, KafkaConsumer
from threading import Thread
import xml.etree.ElementTree as ET
import json
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.confluent_kafka import ConfluentKafkaInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter


app = Flask(__name__)

# Instrument Flask app
FlaskInstrumentor().instrument_app(app)

# Instrument requests library
RequestsInstrumentor().instrument()

# Instrument Kafka
ConfluentKafkaInstrumentor().instrument()

# Configure OpenTelemetry
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Create OTLP exporters
otlp_trace_exporter = OTLPSpanExporter(endpoint=os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'http://localhost:4317'), insecure=True)
otlp_metric_exporter = OTLPMetricExporter(endpoint=os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT', 'http://localhost:4317'), insecure=True)

# Create a BatchSpanProcessor and add the exporter to it
span_processor = BatchSpanProcessor(otlp_exporter)

# Add the SpanProcessor to the tracer provider
trace.get_tracer_provider().add_span_processor(span_processor)

# Set up Metrics
metrics.set_meter_provider(MeterProvider(metric_readers=[PeriodicExportingMetricReader(otlp_metric_exporter)]))
meter = metrics.get_meter(__name__)

# Create a custom counter metric
request_counter = meter.create_counter(
    name="requests_count",
    description="Counts the number of requests received",
    unit="1"
)


# Kafka configuration
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'localhost:9092')
TOPIC_INCOMING = os.getenv('KAFKA_TOPIC_INCOMING', 'incoming_xml')
TOPIC_DEADLETTER = os.getenv('KAFKA_TOPIC_DEADLETTER', 'deadletter_xml')
TOPIC_OUTGOING = os.getenv('KAFKA_TOPIC_OUTGOING', 'outgoing_xml')

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))

@app.route('/fetch_xml', methods=['GET'])
def fetch_xml():
    with tracer.start_as_current_span("fetch_xml_endpoint"):
        url = os.getenv('XML_URL', 'https://bwt.cbp.gov/xml/bwt.xml')
        response = requests.get(url)
        if response.status_code == 200:
            headers = [('trace_id', str(span.get_span_context().trace_id))]
            producer.produce(TOPIC_INCOMING, value=response.text, headers=headers)
            producer.flush()
            request_counter.add(1, {"http.method": "GET", "status_code": "200", "endpoint": "/fetch_xml", "trace_id": span.get_span_context().trace_id})
            return jsonify({"message": "XML data fetched and published to Kafka topic."}), 200
        else:
            headers = [('trace_id', str(span.get_span_context().trace_id))]
            producer.produce(TOPIC_DEADLETTER, value=response.text, headers=headers)
            producer.flush()
            request_counter.add(1, {"http.method": "GET", "status_code": str(response.status_code) "endpoint": "/fetch_xml", "trace_id": span.get_span_context().trace_id})
            return jsonify({"message": "Failed to fetch XML data."}), 500

def consume_and_process():
    consumer = KafkaConsumer(
        TOPIC_INCOMING,
        bootstrap_servers=KAFKA_BROKER,
        auto_offset_reset='earliest',
        group_id='xml_group',
        value_deserializer=lambda x: x.decode('utf-8')
    )
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    for message in consumer:
        with tracer.start_as_current_span("consume_and_process"):
            xml_data = message.value
            root = ET.fromstring(xml_data)
            # Extract data item from XML
            data_item = root.find('your_data_item_tag').text
            producer.send(TOPIC_OUTGOING, {'data_item': data_item})

if __name__ == '__main__':
    Thread(target=consume_and_process).start()
    app.run(host='0.0.0.0', port=5000)
