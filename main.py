import random
import time


class Warrior:
    name = ""
    health = 100

    def get_punched(self):
        self.health = self.health - 20
        return self.health

    def get_health(self):
        self.health = self.health + 10
        return self.health


w1 = Warrior()
w1.name = "John"  # input("Enter name of first warrior: ")
w2 = Warrior()
w2.name = "Peter"  # input("Enter name of second warrior: ")

print(f"{w1.name}'s health: {w1.health}")
print(f"{w2.name}'s health: {w2.health}")

while w1.health > 0 and w2.health > 0:
    time.sleep(1)
    chooser = random.randint(0, 3)
    if chooser == 0:
        print(f"{w1.name} kicks {w2.name}, {w2.name}'s health: {w2.get_punched()}")
    elif chooser == 2:
        print(f"{w1.name} gets +10 HP, {w1.name}'s HP: {w1.get_health()}")
    elif chooser == 3:
        print(f"{w2.name} gets +10 HP, {w2.name}'s HP: {w2.get_health()}")
    else:
        print(f"{w2.name} kicks {w1.name}, {w1.name}'s health: {w1.get_punched()}")

if w1.health > w2.health:
    print(f"{w1.name} won!")
else:
    print(f"{w2.name} won!")
