from kelasHero import HeroIntelligent, HeroStrength
    

hero1 = HeroIntelligent("SPIDERMAN")
hero2 = HeroStrength("HULK")

hero1.show_info()
print(hero1.__dict__)

hero1.exp = 250

hero1.show_info()
print(hero1.__dict__)

hero2.show_info()
print(hero1.__dict__)

hero2.exp = 250

hero2.show_info()
print(hero1.__dict__)
