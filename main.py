# Importen för configparser är borttagen
from menu import get_menu_choice
from monitoring import SystemMonitor




def main():
    monitor = SystemMonitor()  

    try:
        while True:
            choice = get_menu_choice()
            if choice == 1:
                monitor.start()
            elif choice == 2:
                if not monitor.monitoring_active:
                    print("\nIngen övervakning är aktiv. Starta den med alternativ 1.")
                else:
                    monitor.print_status()
                input("\nTryck Enter för att återgå till menyn.")
            elif choice == 3:
                monitor.create_alarm()
            elif choice == 4:
                monitor.view_alarms()
            elif choice == 5:
                if not monitor.monitoring_active:
                    print("\nDu måste starta övervakningen först (alternativ 1).")
                    input("Tryck Enter för att fortsätta...")
                else:
                    monitor.start_monitoring_mode()
            elif choice == 0:
                print("Programmet avslutas.")
                break
            else:
                print("Ogiltigt val, försök igen.")
    except KeyboardInterrupt:
        print("\nProgrammet avbröts av användaren.")

if __name__ == "__main__":
    main()