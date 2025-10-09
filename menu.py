

def display_menu():
    print("\n======================")
    print("   Övervakningssystem ")
    print("======================")
    print("1. Starta övervakning")
    print("2. Lista aktiv övervakning")
    print("3. Skapa larm")
    print("4. Visa larm")
    print("5. Starta övervakningsläge")
    print("0. Avsluta")

    try:
        return int(input("Välj ett alternativ: "))
    except ValueError:
        print("Ogiltig inmatning, ange en siffra.")
        return -1


