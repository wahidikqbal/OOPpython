class Hero:

    __jumlahHero = 0

    def __init__ (self, name):
        self.health_pool     =       [0,100,200,300,400,500]
        self.armor_pool      =       [0,10,20,40,60,80]
        self.power_pool      =       [0,15,30,45,60,75]
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
    def health_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def power_pool(self):
        pass

    @property
    def levelUp(self):
        pass
 
    @property
    def gainExp(self):
        pass
    
    @health_pool.setter
    def health_pool(self, input):
        self.__health_pool = input

    @armor_pool.setter
    def armor_pool(self, input):
        self.__armor_pool = input
    
    @power_pool.setter
    def power_pool(self, input):
        self.__power_pool = input
    
    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if self.__exp >= 100:
            self.__levelUp = self.__exp // 100
            self.__exp %= 100
    
    @levelUp.setter
    def levelUp (self, input):
        self.__level += input
        self.__health   = self.__health_pool[self.__level]
        self.__armor    = self.__armor_pool[self.__level]
        self.__power    = self.__power_pool[self.__level]

class HeroIntelligent(Hero):
    
    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 50, 100, 150, 200, 300]
        self.armor_pool = [0, 10, 20, 30, 40, 50]
        self.power_pool = [0, 20, 30, 40, 50, 60]
        self.levelUp =  1


class HeroStrength(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.armor_pool = [0, 20, 30, 40, 50, 60]
        self.power_pool = [0, 25, 35, 45, 55, 65]
        self.levelUp = 1




hero1 = HeroIntelligent('SPIDERMAN')
hero1.show_info()
hero1.gainExp = 200

hero1.show_info()
print(hero1.__dict__)

