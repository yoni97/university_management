from repo.insert_to_sql import insert_student_profile
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'profiles',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=False,
    group_id='profiles',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for item in consumer:
    profile = item.value
    inserted_email = insert_student_profile(profile)
    print(f"Stored email message: {profile}")
    consumer.commit()