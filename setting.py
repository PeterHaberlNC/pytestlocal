import os
bootstrap_servers_s =  os.getenv('bootstrap_servers', '')
bootstrap_servers = bootstrap_servers_s.split(',')
print(f"servers: {bootstrap_servers}")
topic_name = os.getenv('topic_name', '')
print(f"topic_name: {topic_name}")
consumer_group = os.getenv('consumer_group', '')
print(f"consumer_group: {consumer_group}")


kafka_setting = {
    'bootstrap_servers': bootstrap_servers,
    'topic_name': topic_name,
    'consumer_id': consumer_group
}
