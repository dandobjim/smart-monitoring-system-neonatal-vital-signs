import json

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "vital-signs",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="signal-consumer-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

for message in consumer:
    data = message.value
    print(
        f"Received message: sensor_id={data['sensor_id']}, "
        f"timestamp={data['timestamp']}, "
        f"temperature={data['temperature']}, "
        f"heart_rate={data['heart_rate']}, "
        f"status={data['status']}"
    )
