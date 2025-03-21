class Character():
    def __init__(self, mana, hp, weapon):
        self.__mana = mana
        self.__hp = hp
        self.__weapon = weapon

    def attack(self, other):
        other.set_hp(other.get_hp() - self.get_weapon().damage)
    
    def get_mana(self):
        return self.__mana
    
    def get_hp(self):
        return self.__hp
    
    def get_weapon(self):
        return self.__weapon
    
    def set_weapon(self, weapon):
        self.__weapon = weapon

    def set_mana(self, mana):
        self.__mana = mana
    
    def set_hp(self, hp):
        self.__hp = hp
