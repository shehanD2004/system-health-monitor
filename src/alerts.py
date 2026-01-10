import logging
from datetime import datetime
from src import config

def check_thresholds(cpu, memory, disk):
    alerts = []

    if cpu > config.CPU_THRESHOLD:
        alerts.append(f"High CPU usage detected: {cpu}%")
    if memory > config.MEM_THRESHOLD:
        alerts.append(f"High Memory usage detected: {memory}%")
    if disk > config.DISK_THRESHOLD:
        alerts.append(f"High Disk usage detected: {disk}%")

    for alert in alerts:
        print(f"{datetime.now()} - ALERT: {alert}")
        logging.warning(alert)

    return alerts
