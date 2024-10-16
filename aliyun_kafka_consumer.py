#!/usr/bin/env python
# encoding: utf-8
# source copied over to /app

import socket
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import setting

sVer = "v1.0.0.1 "

conf = setting.kafka_setting

consumer = KafkaConsumer(bootstrap_servers=conf['bootstrap_servers'],
                        group_id=conf['consumer_id'],
                        api_version = (0,10,2), 
                        session_timeout_ms=25000,
                        max_poll_records=100,
                        fetch_max_bytes=1 * 1024 * 1024)

print (sVer + 'consumer start to consuming...')
consumer.subscribe((conf['topic_name'], ))
for message in consumer:
    print (message.topic, message.offset, message.key, message.value, message.partition)
