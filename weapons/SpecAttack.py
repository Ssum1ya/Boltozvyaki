class Specatk():
    def __init__(self, mana_cost, damage,name):
        self.mana_cost=mana_cost
        self.damage=damage
        self.name=name
    def spec_attack(self,other,player):
        other.set_hp(other.get_hp()-self.damage)
        player.set_mana(player.get_mana()-self.mana_cost)