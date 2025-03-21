from Battle import Battle
from random import randint

class Game():
    def __init__(self, player, enemys, weapons):
        self.player = player
        self.enemys = enemys
        self.weapons = weapons
    def gameplay(self):
        while len(self.enemys) != 0:
            enemy_index = randint(0, len(self.enemys) - 1)
            enemy = self.enemys[enemy_index]
            temp = randint(0, len(self.weapons) - 1)
            weapon = self.weapons[temp]
            print('Вы нашли: '+weapon.name+'. Взять? Да/Нет')
            answer = input()
            if answer.lower() == 'да':
                print('Теперь вы используете ' + weapon.name)
            print('На вас напал '+ enemy.name)
            battle = Battle(self.player, enemy)
            result = battle.battle()
            if result == 0:
                print('Игра окончена')
                break
            elif result == 1:
                self.enemys.pop(enemy_index)
        if len(self.enemys) == 0:
            print('Вы выиграли')
