# 🖥️ System Health Monitor

A lightweight Python application that monitors system resource usage and logs metrics
with timestamped alerts when thresholds are exceeded.

## Features
- CPU, Memory, and Disk monitoring
- Configurable thresholds
- Timestamped logging
- Console alerts
- Modular, testable design
- **Email alerts when thresholds are exceeded**  <!-- New feature -->

## Tech Stack
- Python 3
- psutil
- pytest
- **python-dotenv** (for loading email credentials)  <!-- New dependency -->

## Configuration for Email Alerts

1. Create a `.env` file in the project root and add your email credentials:

```env
EMAIL_SENDER="yourGmail"
EMAIL_PASSWORD="yourGmailAppPassword"
EMAIL_RECEIVER="receiverGmail"


2. Make sure Gmail **2-Step Verification is enabled** and an **App Password** is generated.
3. Adjust thresholds in `src/config.py` if needed.

## Installation

```bash
git clone https://github.com/shehanD2004/system-health-monitor.git
cd system-health-monitor
pip install -r requirements.txt
