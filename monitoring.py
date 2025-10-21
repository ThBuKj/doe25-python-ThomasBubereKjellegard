import psutil
import time
import threading
import os
from alarms import Alarm


class SystemMonitor:
    def __init__(self):
        self.monitoring_active = False
        self.monitor_thread = None
        self.alarms = []
        self.interval = 5

    def start(self):
        if not self.monitoring_active:
            self.monitoring_active = True
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
                    current_value = status["cpu"]
                elif metric_key == "memory":
                    current_value = status["memory"]["percent"]
                elif metric_key == "disk":
                    current_value = status["disk"]["percent"]

                if current_value > alarm.threshold:
                    print(
                        f"\n*** VARNING, LARM AKTIVERAT, {alarm.metric_type.upper()} ANVÄNDNING ÖVERSTIGER {alarm.threshold}% ***"
                    )

            time.sleep(self.interval)

    def get_status(self):
        cpu = psutil.cpu_percent(interval=None)
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
        print(
            f"Minnesanvändning: {status['memory']['percent']:.1f}% ({status['memory']['used'] / 1e9:.2f} GB av {status['memory']['total'] / 1e9:.2f} GB)"
        )
        print(
            f"Diskanvändning: {status['disk']['percent']:.1f}% ({status['disk']['used'] / 1e9:.2f} GB av {status['disk']['total'] / 1e9:.2f} GB)"
        )

    def create_alarm(self):
        metric_map = {1: "CPU", 2: "Minne", 3: "Disk"}
        while True:
            print("\n=== Konfigurera larm ===")
            print("1. CPU användning")
            print("2. Minnesanvändning")
            print("3. Diskanvändning")
            print("0. Tillbaka till huvudmeny")

            try:
                choice_str = input("Välj typ av larm att skapa (0-3): ").strip()
                choice = int(choice_str)

                if choice == 0:
                    break

                if choice in metric_map:
                    metric_type = metric_map[choice]
                    threshold = self._get_threshold_from_user(metric_type)
                    if threshold:
                        new_alarm = Alarm(metric_type, threshold)
                        self.alarms.append(new_alarm)
                        print(f"\n*** Larm skapat: {new_alarm} ***")
                        input("Tryck Enter för att fortsätta...")
                    break
                else:
                    print("\n*** Ogiltigt val. Välj ett nummer mellan 0 och 3. ***")
            except ValueError:
                print("\n*** Ogiltig inmatning. Ange endast en siffra. ***")

    def _get_threshold_from_user(self, metric_type):
        while True:
            try:
                level_str = input(f"Ställ in nivå för {metric_type}-larm (1-100): ").strip()
                level = int(level_str)
                if 1 <= level <= 100:
                    return level
                else:
                    print("\n*** Värdet måste vara mellan 1 och 100. ***")
            except ValueError:
                print("\n*** Ogiltig inmatning, skriv ett heltal. ***")

    def view_alarms(self):
        if not self.alarms:
            print("\nInga larm är konfigurerade.")
        else:
            print("\n=== Konfigurerade Larm ===")
            sorted_alarms = sorted(self.alarms, key=self.get_sort_key)
            for alarm in sorted_alarms:
                print(alarm)

        input("\nTryck Enter för att återgå till huvudmenyn.")

    def get_sort_key(self, alarm):
        return alarm.metric_type



    def start_monitoring_mode(self):
        print("\nStartar live-övervakning...")
        time.sleep(1)

        try:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("--- LIVE-ÖVERVAKNING ---")
                print("(Tryck Ctrl+C för att återgå till menyn)\n")
                self.print_status()
                time.sleep(2)
        except KeyboardInterrupt:
            print("\n\nLive-övervakning avslutad. Återgår till huvudmenyn.")



