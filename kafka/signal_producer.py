import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

from scripts.simulator import generate_sensor_data

producer = KafkaProducer(bootstrap_servers=["localhost:9092"])

data = generate_sensor_data()

data_dict = {
    "sensor_id": data.sensor_id,
    "timestamp": data.timestamp,
    "temperature": data.temperature,
    "heart_rate": data.heart_rate,
    "status": str(data.status),
}

future = producer.send("vital-signs", json.dumps(data_dict).encode("utf-8"))

try:
    record_metadata = future.get(timeout=10)
    print(
        f"Message sent to topic {record_metadata.topic} partition {record_metadata.partition} offset {record_metadata.offset}"
    )
except KafkaError as e:
    print(f"Failed to send message: {e}")
