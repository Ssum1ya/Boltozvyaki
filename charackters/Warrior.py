from charackters.Character import Character
from math import ceil

class Warrior(Character):
    def __init__(self, mana, hp, weapon):
        super().__init__(mana, hp, weapon)
        self.__skill_name = 'Лечение'

    def skill(self):
        self.set_hp(self.get_hp() + ceil(self.get_hp * 0.35))
    
    def get_skill_name(self):
        return self.__skill_name
    