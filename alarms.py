class Alarm:
    def __init__(self, metric_type, threshold):
        self.metric_type = metric_type
        self.threshold = threshold

    def __str__(self):
        return f"{self.metric_type} larm {self.threshold}%"

alarms_list = []

def create_alarm():
    metric_map = {
        1: "CPU",
        2: "Minne",
        3: "Disk"
    }
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
                threshold = _get_threshold_from_user(metric_type)
                if threshold:
                    new_alarm = Alarm(metric_type, threshold)
                    alarms_list.append(new_alarm)
                    print(f"\n*** Larm skapat: {new_alarm} ***")
                    input("Tryck Enter för att fortsätta...")
                    break
            else:
                print("\n*** Ogiltigt val. Välj ett nummer mellan 0 och 3. ***")
        except ValueError:
            print("\n*** Ogiltig inmatning. Ange endast en siffra. ***")

def _get_threshold_from_user(metric_type):
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

def get_sort_key(alarm):
    return alarm.metric_type

def view_alarms():
    if not alarms_list:
        print("\nInga larm är konfigurerade.")
    else:
        print("\n=== Konfigurerade Larm ===")
        sorted_alarms = sorted(alarms_list, key=get_sort_key)
        for alarm in sorted_alarms:
            print(alarm)
    
    input("\nTryck Enter för att återgå till huvudmenyn.")