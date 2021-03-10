#!/usr/bin/env python

# #Required for Event Hubs for kafka
# sasl.mechanism=PLAIN
# security.protocol=SASL_SSL
# sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="{YOUR.EVENTHUBS.CONNECTION.STRING}";


from confluent_kafka import Producer,Consumer
import sys
import json
import datetime
import uuid
import random

conf = {
    'bootstrap.servers': 'kafkaenabledeventhubns.servicebus.windows.net:9093',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '$ConnectionString',
    'ssl.ca.location': 'cacert.pem',  
    'sasl.password': 'Endpoint=sb://kafkaenabledeventhubns.servicebus.windows.net/;SharedAccessKeyName=sendreceivekafka;SharedAccessKey=4vxbVwOGJD7b4aVcUWBvYp440+SFHpRyQVIpMeXvoVE=',
    'client.id': 'python-example-producer'
}

# Create Producer instance
p = Producer(**conf)


def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        print('Message delivered to {} {} @{} {} \n'.format(msg.topic(), msg.partition(), msg.offset(),msg.value()))


#  topic name which is the event hub name
topic= 'kafkaenabledhub'

devices = []
for x in range(0, 10):  
    devices.append(str(uuid.uuid4()))

for y in range(0,20):    # For each device, produce 20 events. 
    # event_data_batch = producer.create_batch() # Create a batch. You will add events to the batch later. 
    for dev in devices:
        try:
        # Create a dummy vehicle reading.
            reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
            msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
            p.produce(topic, msgformatted, callback=delivery_callback)
            p.flush()

        except BufferError as e:
            sys.stderr.write('some error')

sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
p.flush()
