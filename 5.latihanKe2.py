class Hero:
	jumlahHero = 0

	def __init__ (self, selfName, selfPower, selfArmor):
		self.name	= selfName
		self.power	= selfPower
		self.armor	= selfArmor


	def serang(self, lawan):
		print(self.name, 'attack ke', lawan.name)
		lawan.diserang(self)

	def diserang(self, attacker):
		print(self.name, 'defense dari', attacker.name)
		
		print('Kekuatan serang dari', attacker.name, '=', attacker.power)
		print('Kekuatan bertahan dari', self.name, '=', self.armor)

		self.armor -= attacker.power
		if self.armor > 0:
			print (self.name, 'still alive')
		elif self.armor < 0:
			print(self.name, 'game over')
			print(attacker.name, 'win')

hero1 = Hero('superman', 80, 70)
hero2 = Hero('batman', 60 , 70)	

#hero1.serang(hero2)
hero2.serang(hero1)