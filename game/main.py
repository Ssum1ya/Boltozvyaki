from charackters.Magician import Magician
from charackters.Warrior import Warrior
from charackters.Zombie import Zombie
from charackters.Skeleton import Skeleton

from weapons.Weapon import Weapon
from weapons.SpecAttack import Specatk
from Game import Game

fireball = Specatk(50, 50, 'fireball')
staff = Weapon(30, fireball, 'Staff')
cut = Specatk(10, 30, 'cut')
sword = Weapon(20, cut, 'sword')
print('Выберите класс:')
print('1-Маг')
print('2-Воин')
answer=int(input())
if answer==1:
    player = Magician(100, 170, staff)
elif answer==2:
    player = Warrior(170, 100, sword)
enemy1 = Zombie(100, 100, 0, 10)
enemy2 = Skeleton(100, 70, 0, 20)
enemys = [enemy1, enemy2]
weapons = [staff, sword]

game = Game(player, enemys, weapons)
game.gameplay()
