__author__='Burik Sergey'

import random


print('Здравствуй, в игре "Угадай, где враг"')

#variables
enemy_life = 100
player_life = 100

while player_life > 0:
    while enemy_life > 0:
        enemy_place = random.randint(1,4)

        player_decis = int(input('Враг находится?\n 1. Сзади 2.Спереди 3.Слево 4.Справо'))

        if player_decis == enemy_place:
            if enemy_life > 0:
               if player_life > 0:
                    print("Вы попали по врагу")
                    enemy_life = enemy_life - 20
                    print('Ваш hp',player_life)
                    print('Противника hp', enemy_life)
                    print('_____________________________')
                    if player_life == 0:
                        print('Вы проиграли!!!')
                        print('_____________________________')
                    elif enemy_life == 0:
                        print('Вы выиграли!!!')
                        print('_____________________________')
        else:
            if enemy_life > 0:
               if player_life > 0:
                    print('Вы не попали, вас ранили')
                    player_life = player_life - 20
                    print('Ваш hp',player_life)
                    print('Противника hp', enemy_life)
                    print('_____________________________')
                    if player_life == 0:
                        print('Вы проиграли!!!')
                        print('_____________________________')
                    elif enemy_life == 0:
                        print('Вы выиграли!!!')
                        print('_____________________________')