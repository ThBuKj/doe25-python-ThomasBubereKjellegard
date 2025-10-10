
def display_menu():
    while True:
        print("\n============================")
        print("     SYSTEMÖVERVAKNING      ")
        print("============================")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("0. Avsluta")
        print("============================\n")
        

        choice = input("Välj ett alternativ (0–5): ").strip()
        print()
        
        if not choice:
            print("Du måste ange ett val (0–5). Försök igen.")
            continue

        if not choice.isdigit():
            print("Ogiltig inmatning. Ange endast siffror (0–5).")
            continue

        choice = int(choice)

        if choice not in range(0, 6):
            print("Ogiltigt val. Välj mellan 0 och 5.")
            continue

        return choice


