import psutil
import time


class SystemMonitor:
    def __init__(self):
        self.monitoring_active = False

    def start(self):
        self.monitoring_active = True
        print("Övervakning har startat.")

    def stop(self):
        self.monitoring_active = False
        print("Övervakning stoppad.")

    def get_status(self):
        cpu = psutil.cpu_percent(interval=1)
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        battery = psutil.sensors_battery()

        return {
            "cpu": cpu,
            "memory": {
                "percent": mem.percent,
                "used": mem.used,
                "total": mem.total
            },
            "disk": {
                "percent": disk.percent,
                "used": disk.used,
                "total": disk.total
            },
            "battery": {
                "percent": battery.percent if battery else None,
                "plugged": battery.power_plugged if battery else None
            } if battery else None
        }

    def print_status(self):
        status = self.get_status()
        print(f"\nCPU Användning: {status['cpu']}%")
        print(f"Minnesanvändning: {status['memory']['percent']}% "
              f"({status['memory']['used'] / 1e9:.2f} GB av {status['memory']['total'] / 1e9:.2f} GB)")
        print(f"Diskanvändning: {status['disk']['percent']}% "
              f"({status['disk']['used'] / 1e9:.2f} GB av {status['disk']['total'] / 1e9:.2f} GB)\n")
        
        if status['battery']:
            plugged = "Ja" if status['battery']['plugged'] else "Nej"
            print(f"Batterinivå: {status['battery']['percent']}% (Strömadapter ansluten: {plugged})")
        else:
            print("Ingen batteriinformation tillgänglig.")
        print()  

    def run_monitoring_mode(self):
        print("Övervakningsläge startat. Tryck Ctrl+C för att återgå till huvudmenyn.\n")
        try:
            while self.monitoring_active:
                self.print_status()
                print("Övervakning är aktiv... (tryck Ctrl+C för att avsluta)\n")
                time.sleep(3)
        except KeyboardInterrupt:
            print("\nÅtergår till huvudmenyn.")
        finally:
            self.stop()


monitor = SystemMonitor()


def start_monitoring():
    if not monitor.monitoring_active:
        monitor.start()
    else:
        print("Övervakning är redan aktiv.")


def list_active_monitoring():
    if not monitor.monitoring_active:
        print("Ingen övervakning är aktiv.")
    else:
        monitor.print_status()
        input("Tryck Enter för att återgå till menyn.")


def start_monitoring_mode():
    if not monitor.monitoring_active:
        print("Du måste starta övervakningen först (alternativ 1).")
    else:
        monitor.run_monitoring_mode()
