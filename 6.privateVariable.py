class Hero:
    jumlahHero = 0

    def __init__ (self, inputName, inputPower, inputHeatlh, recovery):
        self.name       =   inputName
        self.power      =   inputPower
        self.health     =   inputHeatlh
        self.__recovery =   recovery #variable private


hero1   = Hero("spiderman",75,100,2)

print(hero1.__dict__)
print(hero1.health)