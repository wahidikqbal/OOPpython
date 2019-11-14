class Hero:
    jumlahHero = 0

    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        self.name       =   inputName
        self.power      =   inputPower
        self.armor      =   inputArmor
        self.health     =   inputHealth
        Hero.jumlahHero +=  1

    def whoIs(self):
        print("saya adalah " + self.name)

    def healthUp(self, up):
        self.health += up

    def healthScore(self):
        return self.health

hero1       =   Hero("Spiderman", 75, 50, 80)
hero2       =   Hero("Superman", 80, 75, 85)
hero3       =   Hero("  Hulk", 75, 85, 80)

print(hero1.name)

hero2.whoIs()

hero3.healthUp(10)

print(hero2.name , 'health =' ,hero2.healthScore())