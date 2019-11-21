class Hero:

    __jumlahHero = 0

    def __init__ (self, name):
        self.healthPool     =       [0,100,200,300,400,500]
        self.armorPool      =       [0,10,20,40,60,80]
        self.powerPool      =       [0,15,30,45,60,75]
        self.__name         =       name
        self.__exp          =       0
        self.__level        =       0

    def show_info (self):
        print("{} \n\tlevel: {} \n\tarmor: {} \n\tpower: {} \n\thealt: {}".format(
            self.__name,
            self.__level,
            self.__armor,
            self.__power,
            self.__health,
            )
        )

    @property
    def healthPool(self):
        pass

    @property
    def armorPool(self):
        pass

    @property
    def powerPool(self):
        pass

    @property
    def levelUp(self):
        pass
 
    @property
    def gainExp(self):
        pass
    
    @healthPool.setter
    def healthPool(self, input):
        self.__healthPool = input

    @armorPool.setter
    def armorPool(self, input):
        self.__armorPool = input
    
    @powerPool.setter
    def powerPool(self, input):
        self.__powerPool = input
    
    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if self.__exp >= 100:
            self.__levelUp = self.__exp // 100
            self.__exp     %= 100
    
    @levelUp.setter
    def levelUp (self, input):
        self.__level += input
        self.__health   = self.__healthPool[self.__level]
        self.__armor    = self.__armorPool[self.__level]
        self.__power    = self.__powerPool[self.__level]

class HeroIntelligent(Hero):
    
    def __init__(self, name):
        super().__init__(name)
        self.healthPool = [0, 50, 100, 150, 200, 300]
        self.armorPool = [0, 10, 20, 30, 40, 50]
        self.powerPool = [0, 20, 30, 40, 50, 60]
        self.levelUp =  1


class HeroStrength(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.healthPool = [0, 100, 200, 300, 400, 500]
        self.armorPool = [0, 20, 30, 40, 50, 60]
        self.powerPool = [0, 25, 35, 45, 55, 65]
        self.levelUp = 1




hero1 = HeroIntelligent('SPIDERMAN')

hero1.show_info()
print(hero1.__dict__)

hero1.gainExp = 200

hero1.show_info()
print(hero1.__dict__)
