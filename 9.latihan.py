class Hero:

    __jumlahHero = 0
    __jumlahSerang = 0

    def __init__(self, inputName, inputPower, inputArmor, inputHealth):
        self.__name = inputName
        self.__power = inputPower
        self.__armor = inputArmor
        self.__health = inputHealth
        self.__level = 1
        self.__exp = 0

        self.life = self.__health * self.__level
        self.attack = self.__power * self.__level
        self.defense = self.__armor * self.__level

        self.__health = self.life
        self.__power = self.attack
        self.__armor = self.defense

        Hero.__jumlahHero += 1

    @property
    def info(self):
        return print("nama Hero:", self.__name,
                     "\npower:", self.__power,
                     "\narmor:", self.__armor,
                     "\nhealth:", self.__health,
                     "\nexp:", self.__exp,
                     "\nlevel:", self.__level,
                     "\nlife:", self.life,
                     "\nattack:", self.attack,
                     "\ndefense:", self.defense,

                     "\n-------------------------")

    def serang(self, objekSerang):
        print(self.__name, "menyerang", objekSerang.__name)
        objekSerang.diserang(self)
        Hero.__jumlahSerang += 1
        print("jumlah serang", self.__name, "adalah =", Hero.__jumlahSerang)

        self.life = self.__health * self.__level
        self.attack = self.__power * self.__level
        self.defense = self.__armor * self.__level

        self.__health = self.life
        self.__power = self.attack
        self.__armor = self.defense

        self.up()

        

    def diserang(self, objekPenyerang):
        print(self.__name, "diserang", objekPenyerang.__name)
        self.life = objekPenyerang.attack - self.defense

    def up(self):
        if Hero.__jumlahSerang >= 3:
            print("EXPERIENCE UP !!!")
            self.__exp += 1
            if self.__exp > 2:
                print("LEVEL UUP !!!")
                self.__level += 1
                self.__exp -= 3


hero1 = Hero("Spiderman", 77, 50, 80)
hero2 = Hero("Superman", 80, 75, 85)
hero3 = Hero("Hulk", 75, 85, 80)

hero1.serang(hero2)

hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
print(hero1.__dict__)
hero1.info
print(hero1.__dict__)
hero2.info
print(hero2.__dict__)

# hero2.diserang(hero1)
