import time
import os
import uuid
import datetime
import random
import json
import datetime
from kafka import KafkaProducer 
from time import sleep
from json import dumps

devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()))

# Create a producer client to produce and publish events to the Kafka.
producer = KafkaProducer(bootstrap_servers=['10.1.0.16:9092','10.1.0.14:9092','10.1.0.15:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
# Kafka Topic Name = VehicleDetails
for y in range(0,20):    # For each device, produce 20 events. 
    for dev in devices:
        # Create a dummy reading.
        reading = {'id': dev, 'timestamp': str(datetime.datetime.utcnow()), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
        producer.send('VehicleDetails',reading)
        producer.flush()
    # producer.send_batch(event_data_batch) # Send the batch of events to the event hub.

# Close the producer.    
