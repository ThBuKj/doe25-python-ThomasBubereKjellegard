

import psutil
import time
import threading
import os

class SystemMonitor:
    def __init__(self):
        self.monitoring_active = False
        self.monitor_thread = None
        self.alarms = []

