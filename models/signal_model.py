class Signal:
    def __init__(self, sensor_id, timestamp, temperature, heart_rate, status):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.temperature = temperature
        self.heart_rate = heart_rate
        self.status = status

    def __repr__(self):
        return (f"Signal(sensor_id={self.sensor_id}, timestamp={self.timestamp}, "
                f"temperature={self.temperature}, heart_rate={self.heart_rate}, status={self.status})")