class Hero:
    
    jumlahHero = 0

    def __init__ (self, inputName, inputPower, inputArmor, inputHealth):
        self.__name   =   inputName
        self.__power  =   inputPower
        self.__armor  =   inputArmor
        self.__health =   inputHealth
    
    def getName (self):     #-----> getter, mengambil nilai dengan return
        return self.__name

    def serang (self, objectSerang):
        print(self.__name, "menyerang", objectSerang.__name)
        objectSerang.diserang(self, self.__power)

    def diserang (self, objectPenyerang, powerPenyerang):
        print(self.__name, "diserang", objectPenyerang.__name)               
        # health
        self.__health -= powerPenyerang-self.__armor  #setter, merubah nilai dengan "__"
        print("sisa health", self.__name, "adalah", self.__health)

hero1 = Hero("Spiderman", 77, 50, 80)
hero2 = Hero("Superman", 80, 75, 85)
hero3 = Hero("Hulk", 75, 85, 80)

#print(hero1.getName())
#hero1.diserang(70)

hero1.serang(hero2)
