class Hero:

    jumlahHero = 0

    def __init__ (self, inputName, inputPower, inputArmor):
        self.name       =   inputName
        self.power      =   inputPower
        self.armor      =   inputArmor

    def serang(self, musuh):
        print(self.name, "menyerang", musuh.name)
        print("power", self.name , "=", self.power)
        print("armor", musuh.name, "=", musuh.armor)
        musuh.diserang(self)

    def diserang(self, lawan):
        print(self.name, "diserang" ,lawan.name)
        self.armor = lawan.power - self.armor
        print("armor", self.name, "tersisa", self.armor)


aktor1 = Hero("spiderman", 70, 50)
aktor2 = Hero("superman", 80, 60)

aktor1.serang(aktor2)

