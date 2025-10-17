

import psutil
import time
import threading
import os       

class SystemMonitor:
    def __init__(self):
        self.monitoring_active = False
        self.monitor_thread = None
        self.alarms = []

    def start(self, alarms_list):
        if not self.monitoring_active:
            self.monitoring_active = True
            self.alarms = alarms_list  
            print("Övervakning har startat. Larm kontrolleras i bakgrunden.")
            self.monitor_thread = threading.Thread(
                target=self._background_alarm_checker, daemon=True
            )
            self.monitor_thread.start()
        else:
            print("Övervakning är redan aktiv.")

    def stop(self):
        self.monitoring_active = False
        print("Övervakning stoppad.")

    def _background_alarm_checker(self):
        while self.monitoring_active:
            status = self.get_status()
            for alarm in self.alarms:
                metric = alarm['metric']
                threshold = alarm['threshold']
                
                if metric == 'cpu' and status['cpu'] > threshold:
                    print(f"\n[LARM!] CPU-användning ({status['cpu']:.1f}%) är över gränsen på {threshold}%!")
                elif metric == 'memory' and status['memory']['percent'] > threshold:
                    print(f"\n[LARM!] Minnesanvändning ({status['memory']['percent']:.1f}%) är över gränsen på {threshold}%!")
                elif metric == 'disk' and status['disk']['percent'] > threshold:
                    print(f"\n[LARM!] Diskanvändning ({status['disk']['percent']:.1f}%) är över gränsen på {threshold}%!")

            time.sleep(5)

    def get_status(self):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("/")
        battery = psutil.sensors_battery()
        return {
            "cpu": cpu,
            "memory": {"percent": mem.percent, "used": mem.used, "total": mem.total},
            "disk": {"percent": disk.percent, "used": disk.used, "total": disk.total},
            "battery": ({"percent": battery.percent, "plugged": battery.power_plugged} if battery else None),
        }

    def print_status(self):
        status = self.get_status()
        print(f"\nCPU Användning: {status['cpu']}%")
        print(f"Minnesanvändning: {status['memory']['percent']}% ({status['memory']['used'] / 1e9:.2f} GB av {status['memory']['total'] / 1e9:.2f} GB)")
        print(f"Diskanvändning: {status['disk']['percent']}% ({status['disk']['used'] / 1e9:.2f} GB av {status['disk']['total'] / 1e9:.2f} GB)")
        if status["battery"]:
            plugged = "Ja" if status["battery"]["plugged"] else "Nej"
            print(f"Batterinivå: {status['battery']['percent']}% (Strömadapter ansluten: {plugged})")
        else:
            print("Ingen batteriinformation tillgänglig.")


def start_monitoring(monitor, alarms_list):
    monitor.start(alarms_list)

def show_current_status(monitor):
    if not monitor.monitoring_active:
        print("Ingen övervakning är aktiv. Starta den med alternativ 1.")
    else:
        monitor.print_status()
    input("\nTryck Enter för att återgå till menyn.")

def start_monitoring_mode(monitor):
    if not monitor.monitoring_active:
        print("Du måste starta övervakningen först (alternativ 1).")
        return
    
    print("\nLive-övervakning aktiv. Tryck Ctrl+C för att återgå till menyn.")
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            monitor.print_status()
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nLive-övervakning avslutad. Återgår till huvudmenyn.")