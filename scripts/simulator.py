import datetime
import random

from models.signal_model import Signal, SignalStatus


def generate_sensor_data() -> Signal:
    """
    Generates a random signal for a neonatal patient.
    :return: Signal object containing sensor data.
    """
    temperature = round(random.uniform(36.5, 38.5), 1)  # °C
    cardiac_rate = random.randint(120, 160)  # BPM

    timestamp = datetime.datetime.now(datetime.UTC).isoformat() + "Z"
    id_number = random.randint(1, 5)
    sensor_id = f"neonate_{id_number:03d}"
    status = check_status(temperature, cardiac_rate)
    return Signal(sensor_id, timestamp, temperature, cardiac_rate, status)


def check_status(temperature, cardiac_rate) -> SignalStatus:
    """
    Checks the status of the signal based on temperature and cardiac rate.
    :param temperature:
    :param cardiac_rate:
    :return: SignalStatus
    """
    if temperature < 36.5 or temperature > 38.5:
        return SignalStatus.FIVER
    elif cardiac_rate < 120 or cardiac_rate > 160:
        return SignalStatus.TACHYCARDIA
    else:
        return SignalStatus.NORMAL
