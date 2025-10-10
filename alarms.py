

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
    

