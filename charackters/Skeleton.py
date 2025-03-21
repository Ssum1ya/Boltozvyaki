from charackters.Character import Character
from math import ceil

class Skeleton(Character):
    def __init__(self, mana, hp, weapon, attack):
        super().__init__(mana, hp, weapon)
        self.__skill_name = 'Бросок Кости'
        self.__attack = attack

    def attack(self, other):
        other.set_hp(other.get_hp() - ceil(self.get_weapon().damage * 0.7))

    def skill(self, other):
        other.set_hp(other.get_hp() - ceil(self.__attack * 1.5))
    
    def get_skill_name(self):
        return self.__skill_name