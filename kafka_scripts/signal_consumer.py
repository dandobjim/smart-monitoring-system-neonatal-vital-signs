import json

from kafka.consumer.group import KafkaConsumer

from database.db import get_connection

consumer = KafkaConsumer(
    "vital-signs",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="signal-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

while True:
    with get_connection() as conn:
        for message in consumer:
            data = message.value
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO vital_signs (sensor_id, heart_rate, temperature, timestamp) VALUES (%s, %s, %s, %s)",
                    (data["sensor_id"], data["heart_rate"], data["temperature"], data["timestamp"]),
                )
                conn.commit()
            print(f"Inserted data: {data}")
