from flask import Blueprint, request, jsonify
import csv
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

from configs.data_files import csv_profile_path

student_profile_bp = Blueprint('student_profile', __name__)

try:
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
except KafkaError as e:
    print(f"Failed to connect to Kafka: {e}")
    producer = None

if producer:
    try:
        with open(csv_profile_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                topic = 'profiles'
                producer.send(topic, value=row)
                print(f"Sent to Kafka: {row}")
    except Exception as e:
        print(f"Error reading CSV or sending to Kafka: {e}")
    finally:
        producer.flush()
        producer.close()
else:
    print("Kafka producer is not initialized.")




# from flask import Blueprint, request, jsonify
# import csv
# import json
# import os
# from kafka import KafkaProducer
# from kafka.errors import KafkaError
#
# # נתיבי קבצי ה-CSV
# csv_files = {
#     'profiles': './data_files/students_profiles.csv',
#     'lifestyle': './data_files/student_lifestyle.csv',
#     'performance': './data_files/student_course_performance.csv',
#     'reviews': './data_files/reviews_with_students.csv',
# }
#
# # יצירת Kafka Producer
# try:
#     producer = KafkaProducer(
#         bootstrap_servers='localhost:9092',
#         value_serializer=lambda v: json.dumps(v).encode('utf-8')
#     )
#     print("Connected to Kafka.")
# except KafkaError as e:
#     print(f"Failed to connect to Kafka: {e}")
#     producer = None
#
# if producer:
#     try:
#         # מעבר על כל הקבצים ושליחת הודעות
#         for topic, csv_path in csv_files.items():
#             if os.path.exists(csv_path):
#                 print(f"Processing file: {csv_path}")
#                 with open(csv_path, mode='r') as file:
#                     csv_reader = csv.DictReader(file)
#                     for row in csv_reader:
#                         producer.send(topic, value=row)
#                         print(f"Sent to Kafka topic '{topic}': {row}")
#             else:
#                 print(f"File not found: {csv_path}")
#     except Exception as e:
#         print(f"Error reading CSV or sending to Kafka: {e}")
#     finally:
#         producer.flush()
#         producer.close()
#         print("Kafka producer closed.")
# else:
#     print("Kafka producer is not initialized.")
