import enum
from dataclasses import dataclass


class SignalStatus(enum.Enum):
    NORMAL = "normal"
    FIVER = "fiver"
    TACHYCARDIA = "tachycardia"

    def __str__(self):
        return self.value


@dataclass
class Signal:
    def __init__(self,
                 sensor_id: str,
                 timestamp: str,
                 temperature: float,
                 heart_rate: float,
                 status: SignalStatus):
        self.sensor_id = sensor_id
        self.timestamp = timestamp
        self.temperature = temperature
        self.heart_rate = heart_rate
        self.status = status

    def __repr__(self):
        return (f"Signal(sensor_id={self.sensor_id}, timestamp={self.timestamp}, "
                f"temperature={self.temperature}, heart_rate={self.heart_rate}, status={self.status})")