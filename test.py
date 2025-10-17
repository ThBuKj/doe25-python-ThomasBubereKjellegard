
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def into(self):
        print(name + " (level " + level + ")")

name = input()
level = input()

char = Player(name, level)
# char.into()
