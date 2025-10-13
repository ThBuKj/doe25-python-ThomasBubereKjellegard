
def display_menu():
    print("\n============================")
    print("    SYSTEMÖVERVAKNING     ")
    print("============================")
    print("1. Starta övervakning i bakgrunden")
    print("2. Visa aktuell systemstatus")
    print("3. Skapa/ändra larm")
    print("4. Visa aktiva larm")
    print("5. Starta live-övervakning")
    print("0. Avsluta")
    print("============================\n")

def get_menu_choice():
    while True:
        display_menu()
        choice_str = input("Välj ett alternativ (0-5): ").strip()
        
        try:
            choice = int(choice_str)
            if 0 <= choice <= 5:
                return choice
            else:
                print("\n*** Ogiltigt val. Välj ett nummer mellan 0 och 5. ***")
        except ValueError:
            print("\n*** Ogiltig inmatning. Ange endast en siffra. ***")
        
        input("Tryck Enter för att försöka igen...")