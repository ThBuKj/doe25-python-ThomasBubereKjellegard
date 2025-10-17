from menu import get_menu_choice 
from monitoring import start_monitoring, show_current_status, start_monitoring_mode, SystemMonitor
from alarms import create_alarm, view_alarms


def main():
    monitor = SystemMonitor()  
    alarms_list = []

    try:
        while True:
            choice = get_menu_choice()          
            if choice == 1:
                start_monitoring(monitor, alarms_list)
            elif choice == 2:
                show_current_status(monitor)
            elif choice == 3:
                create_alarm()
            elif choice == 4:
                view_alarms()
            elif choice == 5:
                start_monitoring_mode(monitor)
            elif choice == 0:
                print("Programmet avslutas.")
                break
            else:
                print("Ogiltigt val, försök igen.")
    except KeyboardInterrupt:
        print("\nProgrammet avbröts av användaren med Ctrl+C.")
        print("Avslutar snyggt...")


if __name__ == "__main__":
    main()
