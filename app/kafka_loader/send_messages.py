import json
import time
from confluent_kafka import Producer

# Kafka configuration
conf = {
    'bootstrap.servers': 'eventstore-kafka-bootstrap.eventstore:9092',  # Replace with your Kafka broker(s)
}

# Create a Producer instance
producer = Producer(conf)

# Kafka topic
topic = 'events'  # Replace with your Kafka topic

# Function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Generate and send 1000 JSON messages
for i in range(10000):
    message = {
        'id': i,
        'testrun': 4,
        'timestamp': time.time(),
        'value': f'This is message number {i}'
    }

    # Produce the message to the Kafka topic
    producer.produce(topic, json.dumps(message).encode('utf-8'), callback=delivery_report)

    # Wait for any outstanding messages to be delivered
    producer.poll(0)

# Wait for all messages to be delivered
producer.flush()
