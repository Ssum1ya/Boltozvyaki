from random import randint

class Battle():
    def __init__(self, player, enemy):
        self.player=player
        self.enemy=enemy
    def battle(self):
        action=1
        relult=None
        while self.player.get_hp() > 0 and self.enemy.get_hp() >0:
            if action==1:
                print('Выберите действие:')
                print('1-атаковать')
                if self.player.get_mana()>=self.player.get_weapon().spec_atk.mana_cost:
                    print('2- использовать '+self.player.get_weapon().spec_atk.name)
                print('3-использовать '+self.player.get_skill_name())
                answer=None
                answer=int(input())
                if answer==1:
                    self.player.attack(self.enemy)
                elif answer==2:
                    self.player.get_weapon().spec_atk.spec_attack(self.enemy, self.player)
                elif answer==3:
                    self.player.skill()
                print('У врага осталось '+str(self.enemy.get_hp())+' hp')
                if self.enemy.get_hp()<=0:
                    print('Враг повержен')
                    result=1
                    return result
                action=2
            elif action==2:
                temp=randint(1,3)
                if temp==1:
                    self.enemy.attack(self.player)
                    print(self.enemy.name+' наносит удар')
                    print(self.enemy.name+' нанёс вам '+str(self.enemy.get_attack())+' урона')
                else:
                    self.enemy.skill(self.player)
                    print(self.enemy.name + ' использует '+self.enemy.get_skill_name())
                    print(self.enemy.name + ' нанёс вам ' + str(self.enemy.get_attack()) + ' урона')
                print('У вас '+str(self.player.get_hp())+' hp')
                if self.player.get_hp()<=0:
                    print('Вы проиграли')
                    result=0
                    return result
                action=1