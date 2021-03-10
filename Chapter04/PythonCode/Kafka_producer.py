import time
import os
import uuid
import datetime
import random
import json
import json
import datetime
from kafka import KafkaProducer
from time import sleep
from json import dumps

# from azure.eventhub import EventHubProducerClient, EventData

# This script simulates the production of events for 10 devices.
devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()))

# Create a producer client to produce and publish events to the Kafka.
producer = KafkaProducer(bootstrap_servers=['10.1.0.13:9092','10.1.0.11:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for y in range(0,20):    # For each device, produce 20 events. 
    # event_data_batch = producer.create_batch() # Create a batch. You will add events to the batch later. 
    for dev in devices:
        # Create a dummy reading.
        reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
        # s = json.dumps(reading) # Convert the reading into a JSON string.
        # event_data_batch.add(EventData(s)) # Add event data to the batch.
        producer.send('VehicleDetails',reading)
        producer.flush()
    # producer.send_batch(event_data_batch) # Send the batch of events to the event hub.

# Close the producer.    
# producer.close()