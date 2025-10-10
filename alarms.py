

def create_submenu():
    print("\n=== Skapa larm ===")
    print("1. CPU-användning")
    print("2. Minnesanvändning")
    print("3. Diskanvändning")
    print("4. Tillbaka till huvudmeny")
    try:
        return int(input("Välj ett alternativ: "))
    except ValueError:
        print("Ogiltig inmatning, ange en siffra.")
        return -1
    

def create_alarm():
    while True:                                     
        choice = create_submenu()                   
        if choice == 1:
            configure_alarm("CPU-användning")
            break                                   
        elif choice == 2:
            configure_alarm("Minnesanvändning")
            break
        elif choice == 3:
            configure_alarm("Diskanvändning")
            break
        elif choice == 4:
            print("Återgår till huvudmenyn...")
            break
        else:
            print("Ogiltigt val, försök igen.")
