class Hero:

    jumlahHero = 0

    def __init__ (self, inputName, inputPower, inputArmor, inputHealth):
        self.name   =   inputName
        self.power  =   inputPower
        self.armor  =   inputArmor
        self.health =   inputHealth
    
    def serang (self, objekSerang):
        print(self.name , "menyerang" , objekSerang.name )
        objekSerang.diserang(self, self.power)
        """             |
            -------------
            |               """        
    def diserang (self, objectPenyerang, powerPenyerang):
        print(self.name, "diserang", objectPenyerang.name)
        self.health -= powerPenyerang-self.armor
        print("sisa health",self.name, "setelah diserang oleh", objectPenyerang.name, "adalah", self.health)

hero1       =   Hero("Spiderman", 77, 50, 80)
hero2       =   Hero("Superman", 80, 75, 85)
hero3       =   Hero("Hulk", 75, 85, 80)   

hero1.serang(hero2)
#hero3.serang(hero1)