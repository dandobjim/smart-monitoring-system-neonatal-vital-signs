from models.signal_model import SignalStatus
from scripts.simulator import check_status, generate_sensor_data


class TestSimulator:
    def test_check_status_fiver(self):
        assert check_status(36.4, 130) == SignalStatus.FIVER
        assert check_status(38.6, 130) == SignalStatus.FIVER

    def test_check_status_tachycardia(self):
        assert check_status(37.0, 119) == SignalStatus.TACHYCARDIA
        assert check_status(37.0, 161) == SignalStatus.TACHYCARDIA

    def test_check_status_normal(self):
        assert check_status(37.0, 130) == SignalStatus.NORMAL
        assert check_status(37.5, 150) == SignalStatus.NORMAL

    def test_check_status_edge_cases(self):
        assert check_status(36.5, 120) == SignalStatus.NORMAL
        assert check_status(38.5, 160) == SignalStatus.NORMAL
        assert check_status(36.4, 119) == SignalStatus.FIVER
        assert check_status(38.6, 161) == SignalStatus.FIVER

    def test_generate_sensor_data(self):
        signal = generate_sensor_data()
        assert signal.sensor_id.startswith("neonate_")
        assert isinstance(signal.timestamp, str)
        assert 36.5 <= signal.temperature <= 38.5
        assert 120 <= signal.heart_rate <= 160
        assert isinstance(signal.status, SignalStatus)
