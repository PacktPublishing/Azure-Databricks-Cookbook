
from confluent_kafka import Producer,Consumer
import sys
import json
import datetime
import uuid
import random
import time
from datetime import timedelta

conf = {
    'bootstrap.servers': 'kafkademoenabledeventhubns.servicebus.windows.net:9093',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanism': 'PLAIN',
    'sasl.username': '$ConnectionString',
    'ssl.ca.location': 'cacert.pem',  
    'sasl.password': 'Endpoint=sb://kafkaenabledeventhubns.servicebus.windows.net/;SharedAccessKeyName=sendreceivekafka;SharedAccessKey=dfdsfdfdsfdsfMesfsdffdsdfVE=',
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
topic= 'VehicleSensorEventHub'

# Sensor data is genrated for on below 10 Vehicles
devices = ['4b1e829f-5f32-4ae9-b415-9e7f0eb15401', '115e6d02-4a43-4131-b6af-9d2a8d642073', '90ccea91-416e-453f-b582-e6f04f02ee40', 'aa7e09d0-92cb-4cc0-99e2-04602ab0f85a', 'b51480fc-af07-491d-b914-fec46d7d7d47', '5cb4ae8e-19de-40e1-96b5-874ffc43210b', 'c79935cc-0b88-44ae-9765-a68d3c0fd37d', '04ac43cf-ed3c-4fb7-a15e-2dabd3c8342e', '2832b3ec-222c-4049-9af5-45a8d66d6b58', '288e3ee8-ea29-489b-9c3d-07e7c6d6ee99']

# latlong =[[40.730610,-73.984016,"NYC"],[40.650002, -73.949997,"BROOKLYN"],
# [40.579021, -74.151535,"STATEN ISLAND"],[40.837048, -73.865433,"BRONX"],[40.742054, -73.769417,"QUEENS"]]

latlong =[[40.730610,-73.984016],[40.650002, -73.949997],
[40.579021, -74.151535],[40.837048, -73.865433],[40.742054, -73.769417]]

for dev in devices:    
    for y in range(0,random.randrange(20)): # For each device, produce upto 20 events max.  
        lfi=0
        if(y%2==0):
            lfi=random.randint(0,1)
        try:
        # Create a dummy vehicle reading.
            print(y)
            latlonglocal = random.choice(latlong)
            reading = {'id': dev, 'eventtime': str(datetime.datetime.utcnow()+timedelta(hours=y)), 'rpm': random.randrange(100), 'speed': random.randint(70, 120), 'kms': random.randint(100, 10000),'lfi': lfi,'lat':latlonglocal[0],'long':latlonglocal[1]}

            msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
            p.produce(topic, msgformatted, callback=delivery_callback)
            p.flush()
            # time.sleep(1)

        except BufferError as e:
            sys.stderr.write('some error')

sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
p.flush()


# reading = {'id': '2832b3ec-222c-4049-9af5-45a8d66d6b58', 'eventtime':str(datetime.datetime.utcnow()+timedelta(hours=16)), 'rpm': random.randrange(100), 'speed': random.randint(70, 100), 'kms': random.randint(100, 1000),'lfi':0,'lat':40.579021,'long':-74.151535}
# msgformatted = json.dumps(reading) # Convert the reading into a JSON object.
# p.produce(topic, msgformatted, callback=delivery_callback)
# p.flush()
