from src.alerts import check_thresholds

def test_no_alerts():
    alerts = check_thresholds(10, 20, 30)
    assert alerts == []

def test_cpu_alert():
    alerts = check_thresholds(90, 20, 30)
    assert len(alerts) == 1
