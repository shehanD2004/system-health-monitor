import smtplib
import logging
from datetime import datetime
from email.message import EmailMessage
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

def send_email_alert(subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = config.EMAIL_SENDER
    msg["To"] = config.EMAIL_RECEIVER
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
        server.starttls()
        server.login(config.EMAIL_SENDER, config.EMAIL_PASSWORD)
        server.send_message(msg)