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

spiderman   =   Hero("Spiderman", 75, 50, 80)
superman    =   Hero("Superman", 80, 75, 85)
hulk        =   Hero("  Hulk", 75, 85, 80)

print(spiderman.name)

superman.whoIs()

hulk.healthUp(10)

print(spiderman.name , 'health =' ,hulk.healthScore())