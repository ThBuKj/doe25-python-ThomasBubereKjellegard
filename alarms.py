

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


def configure_alarm(alarm_type):
    while True:
        try:
            level = int(input(f"\nStäll in nivå för {alarm_type} (1-100): "))
            if 1 <= level <= 100:
                print(f"Larm för {alarm_type} satt till {level}%.")
                break
            else:
                print("Värdet måste vara mellan 1 och 100.")
        except ValueError:
            print("Ogiltig inmatning, skriv ett heltal mellan 1 och 100.")


"""""" """''
Visa larm
Listar alla configurerade larm. Larmen ska vara sorterade på typ när de visas. Exempel:

CPU larm 70%
Disklarm 95%
Minneslarm 80%
Minneslarm 90%
Efter detta promtas användaren om att bekräfta genom att trycka enter.

Tryck valfri tangent för att gå tillbaka till huvudmeny

Notera att man kan ha flera larm av samma typ.



 Triggas ett larm när övervakningen är aktiv skrivs det ut i konsolen. T.ex:

                ***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER 80%***

                
""" """"""


def view_alarms():
    pass


def view_alarms():
    pass
