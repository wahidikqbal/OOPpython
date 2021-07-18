class Hero:

    jumlahHero = 0

    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        self.__name      = inputName
        self.__power     = inputPower
        self.__armor     = inputArmor
        self.__health    = inputHealth
        #self.info        = print("nama Hero:", self.__name,
        #                         "\npower:", self.__power,
        #                         "\narmor:", self.__armor,
        #                         "\nhealth:", self.__health,
        #                         "\n-------------------------")

    @property
    def info (self):
        return print("nama Hero:", self.__name,
                     "\npower:", self.__power,
                     "\narmor:", self.__armor,
                     "\nhealth:", self.__health,
                     "\n-------------------------")
    
    #getter di pass terlebih dahulu menggunakan property
    @property                                                              
    def armor(self):                       
        pass                       
    @armor.getter                      
    def armor (self):                      
        return self.__armor                    
    #setter
    @armor.setter
    def armor (self, input):
        self.__armor = input

hero1 = Hero("Spiderman", 77, 50, 80)
hero2 = Hero("Superman", 80, 75, 85)
hero3 = Hero("Hulk", 75, 85, 80)

hero1.info
#print("armor sekarang",hero1.armor)
#hero1.armor = 75
#print("armor naik!!!",hero1.armor)
