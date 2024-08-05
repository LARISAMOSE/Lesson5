class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лег спать")
        self.endurance += 2
    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1
    def hit(self):
        print(f"{self.name} бьёт кого-то")
        self.endurance -= 6
    def walk(self):
        print(f"{self.name} гуляет")
    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")

war1 = Warrior("Алёша", 74, 56, "светлый" )
war2 = Warrior("Егор", 43, 64, "блонд")

print(war1.endurance)
print(war1.power)
war1.sleep()
war1.eat()
war1.hit()
war1.walk()
war1.info()
print(war1.endurance)
print(war1.power)

war2.sleep()
war2.eat()
war2.hit()
war2.walk()
war2.info()