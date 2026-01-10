import psutil
import time
import logging
from src import config
from src.alerts import check_thresholds

def setup_logging():
    logging.basicConfig(
        filename=config.LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def get_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return cpu, memory, disk

def monitor():
    setup_logging()
    print("System Health Monitor started...")

    while True:
        cpu, memory, disk = get_metrics()

        logging.info(
            f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
        )

        check_thresholds(cpu, memory, disk)
        time.sleep(config.CHECK_INTERVAL)
