class Tipe:
    def tipe(self, tipe):
        self.tipe = tipe
    def infoTipe(self):
        print("tipenya adalah",self.tipe)

class Team:
    def team(self, team):
        self.team = team
    def infoTeam(self):
        print("teamnya adalah",self.team)

class Hero(Tipe,Team): #class Hero mendapatkan turunan method dari 2 class, yaitu Class Tipe dan Class Team
    def __init__ (self, name, power):
        self.name = name
        self.power = power
        print(self.name , "mempunyai power", self.power)

hero1 = Hero("superman", 100)
hero1.tipe("Strenght")
hero1.team("Merah")

hero1.infoTipe()
hero1.infoTeam()