from kafka import KafkaConsumer

consumer = KafkaConsumer(bootstrap_servers=['10.1.0.13:9092','10.1.0.11:9092'],auto_offset_reset='earliest',api_version=(0, 10, 1))
consumer.subscribe(['vesseltopic'])
for msg in consumer:
    print (msg)



consumer = KafkaConsumer(bootstrap_servers=['10.1.0.13:9092','10.1.0.11:9092'],auto_offset_reset='earliest',api_version=(0, 10, 1))
consumer.subscribe(['temptopic'])
for msg in consumer:
    print (msg)
