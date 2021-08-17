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
    'sasl.password': 'Endpoint=sb://kafkaenabledeventhubns.servicebus.windows.net/;SharedAccessKeyName=sendreceivekafka;SharedAccessKey=zzzzz',
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
topic= 'eventhubsource1'

# devices = ['4ba6e242-7282-4367-b09c-7568e4b12a58', '7e0d39fd-7251-483c-92d6-7d6bb5cc164e', '405a6bb3-ed92-4a85-996c-9d8b01867923', 'a18df3df-0a16-484b-9a3b-9a2a2ed39b58', 'a4cde850-318d-4e91-ba08-1f5cd3ddd561']
devices = ['4ba6e242-7282-4367-b09c-7568e4b12a58', '7e0d39fd-7251-483c-92d6-7d6bb5cc164e', '405a6bb3-ed92-4a85-996c-9d8b01867923', 'a18df3df-0a16-484b-9a3b-9a2a2ed39b58', 'a4cde850-318d-4e91-ba08-1f5cd3ddd561']
# for x in range(0, 5):  
#     devices.append(str(uuid.uuid4()))

print(devices)

for y in range(0,20):    # For each device, produce 5 events. 
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


# Run the blwo code for simulating late arriving data by changingthe timestamp for a specific Id


# reading = {'id': '9e0d39fd-7251-483c-92d6-7d6bb5cc164e', 'timestamp':str(datetime.datetime.utcnow()-datetime.timedelta(minutes=2)), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
# msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
# p.produce(topic, msgformatted, callback=delivery_callback)
# p.flush()

# print(datetime.datetime.utcnow()-datetime.timedelta(minutes=25)) --02:07:14.909217

# reading = {'id': '9e0d39fd-7251-483c-92d6-7d6bb5cc164e', 'timestamp':str(datetime.datetime.utcnow()), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
# msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
# p.produce(topic, msgformatted, callback=delivery_callback)
# p.flush()

# reading = {'id': '10e0d39fd-7251-483c-92d6-7d6bb5cc164e', 'timestamp':str(datetime.datetime.utcnow()-datetime.timedelta(minutes=100)), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000)}
# msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
# p.produce(topic, msgformatted, callback=delivery_callback)
# p.flush()