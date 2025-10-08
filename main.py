
from menu import display_menu
from monitoring import start_monitoring, list_active_monitoring, start_monitoring, start_monitoring_mode
from alarms import create_alarm, view_alarms

def main():
    while True:
        choice = display_menu()
        if choice == 1:
            start_monitoring()
        elif choice == 2:
            list_active_monitoring()
        elif choice == 3:
            create_alarm()                  
        elif choice == 4:
            view_alarms()
        elif choice == 5:
            start_monitoring_mode()
        else:
            print("Ogiltigt val, vänligen försök igen.")

if __name__ == "__main__":
    main()