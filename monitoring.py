import psutil
import time
import threading
import os


class SystemMonitor:
    def __init__(self): 
        self.monitoring_active = False
        self.monitor_thread = None
        self.alarms = []
        self.interval = 10  

    def start(self, alarms_list):
        if not self.monitoring_active:
            self.monitoring_active = True
            self.alarms = alarms_list
            print("Övervakning har startat.")
            print(f"Kontrollintervall är satt till {self.interval} sekunder.")
            self.monitor_thread = threading.Thread(
                target=self._background_alarm_checker, daemon=True
            )
            self.monitor_thread.start()
        else:
            print("Övervakning är redan aktiv.")

    def stop(self):
        self.monitoring_active = False

    def _background_alarm_checker(self):
        metric_map = {"CPU": "cpu", "Minne": "memory", "Disk": "disk"}
        while self.monitoring_active:
            status = self.get_status()
            for alarm in self.alarms:
                metric_key = metric_map.get(alarm.metric_type)
                if not metric_key:
                    continue

                current_value = 0
                if metric_key == "cpu":
                    current_value = status['cpu']
                elif metric_key == "memory":
                    current_value = status['memory']['percent']
                elif metric_key == "disk":
                    current_value = status['disk']['percent']
                
                if current_value > alarm.threshold:
                    print(f"\n*** VARNING, LARM AKTIVERAT, {alarm.metric_type.upper()} ANVÄNDNING ÖVERSTIGER {alarm.threshold}% ***")
            
            time.sleep(self.interval)

    def get_status(self):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        return {
            "cpu": cpu,
            "memory": {"percent": mem.percent, "used": mem.used, "total": mem.total},
            "disk": {"percent": disk.percent, "used": disk.used, "total": disk.total},
        }

    def print_status(self):
        status = self.get_status()
        print(f"CPU Användning: {status['cpu']:.1f}%")
        print(f"Minnesanvändning: {status['memory']['percent']:.1f}% ({status['memory']['used'] / 1e9:.2f} GB av {status['memory']['total'] / 1e9:.2f} GB)")
        print(f"Diskanvändning: {status['disk']['percent']:.1f}% ({status['disk']['used'] / 1e9:.2f} GB av {status['disk']['total'] / 1e9:.2f} GB)")

def start_monitoring_mode(monitor):
    print("\nStartar live-övervakning...")
    time.sleep(1)

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("--- LIVE-ÖVERVAKNING ---")
            print("(Tryck Ctrl+C för att återgå till menyn)\n")
            monitor.print_status()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n\nLive-övervakning avslutad. Återgår till huvudmenyn.")