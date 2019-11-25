class Hero:

    __jumlahHero = 0
    __jumlahSerang = 0

    def __init__(self, name):
        self.healthPool = [0, 100, 200, 300, 400, 500]
        self.armorPool = [0, 10, 20, 40, 60, 80]
        self.powerPool = [0, 15, 30, 45, 60, 75]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def show_info(self):
        print("HERO NAME: {} \n\tlevel: {} \n\tarmor: {} \n\tpower: {} \n\thealth: {}".format(
            self.__name,
            self.__level,
            self.__armor,
            self.__power,
            self.__health,
        )
        )
    
    def serang(self, object):
        print(self.__name, "menyerang", object.__name)
        object.diserang(self)

    def diserang(self, object):
        print(self.__name, "diserang", object.__name)

    @property
    def healthPool(self):
        pass

    @property
    def armorPool(self):
        pass

    @property
    def powerPool(self):
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

    @property
    def exp(self):
        pass
    @exp.setter
    def exp(self, input):
        self.__exp += input
        if (self.__exp >= 100):
            self.__level = self.__exp // 100
            self.levelUp = self.__level
            self.__exp %= 100

    @property
    def levelUp(self):
        pass
    @levelUp.setter
    def levelUp(self, input):
                self.__level = input
                self.__armor = self.__armorPool[self.__level]
                self.__power = self.__powerPool[self.__level]
                self.__health = self.__healthPool[self.__level]


class HeroStrength(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.healthPool = [0, 100, 200, 300, 400, 500]
        self.armorPool = [0, 20, 30, 40, 50, 60]
        self.powerPool = [0, 25, 35, 45, 55, 65]
        self.levelUp = 1
    
    def serang(self, object):
        super().serang(object)


class HeroIntelligent(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.healthPool = [0, 50, 100, 150, 200, 300]
        self.armorPool = [0, 10, 20, 30, 40, 50]
        self.powerPool = [0, 20, 30, 40, 50, 60]
        self.levelUp = 1
    
    def serang(self, object):
        super().serang(object)
