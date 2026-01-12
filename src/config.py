import os
from dotenv import load_dotenv

load_dotenv()

# Configuration constants for system health monitoring
CPU_THRESHOLD = 80
MEM_THRESHOLD = 80
DISK_THRESHOLD = 80

CHECK_INTERVAL = 5  # seconds
LOG_FILE = "logs/system_health.log"

#Email settings
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

SMPTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
