from charackters.Character import Character
from math import ceil

class Magician(Character):
    def __init__(self, mana, hp, weapon):
        super().__init__(mana, hp, weapon)
        self.__skill_name = 'Лечение засчёт маны'

    def skill(self):
        self.set_hp(ceil(self.get_mana() * 0.2))
        self.set_mana(self.get_mana() - self.get_mana() * 0.35)
    
    def get_skill_name(self):
        return self.__skill_name