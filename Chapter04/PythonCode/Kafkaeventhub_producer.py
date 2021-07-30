
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
    'sasl.password': 'Endpoint=sb://kafkaenabledeventhubns.servicebus.windows.net/;SharedAccessKeyName=sendreceivekafka;SharedAccessKey=FLdyRBpyGt6Pluis5b79vRTwuHOy/OjwijF7jsCmFnA=',
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
topic= 'kafkaenabledhub2'

devices = []
for x in range(0, 10):  
    devices.append(str(uuid.uuid4()))

for y in range(0,20):    # For each device, produce 20 events. 
    # . 
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

# datetime.datetime.utcnow()

# {"start": "2021-07-30T01:55:00.000+0000", "end": "2021-07-30T01:56:00.000+0000"}
# c7bb7aa9-cc1c-453f-a86e-ca171c710e85


# reading = {'id': 'c7bb7aa9-cc1c-453f-a86e-ca171c710e85', 'timestamp':str(datetime.datetime.utcnow()-datetime.timedelta(minutes=55)), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
# msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
# p.produce(topic, msgformatted, callback=delivery_callback)
# p.flush()


# {"start": "2021-03-14T10:47:00.000+0000", "end": "2021-03-14T10:49:00.000+0000"} 
# and {"start": "2021-03-14T10:46:00.000+0000", "end": "2021-03-14T10:48:00.000+0000"}. 
# Here .data with timestamp 2021-03-14T10:47:00.000+0000 

# datetime.datetime.utcnow()-datetime.timedelta(minutes=31)

# reading = {'id': 'c2c7cb35-2f97-4fab-ab23-62fe24eca7af', 'timestamp':str(datetime.datetime.utcnow()-datetime.timedelta(minutes=32)), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
# msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
# p.produce(topic, msgformatted, callback=delivery_callback)
# p.flush()
