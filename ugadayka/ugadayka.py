import random


def generation():
    """ Генерирует число от 1 до 100 невключительно
    """
    return random.randrange(0, 100)
    

def ugadayka(secret_num):
    """ ведет диалог, пока игрок не угадает число. Если загаданное число 
    больше указанного, выводится "Больше", если меньше - "Меньше". Если 
    число угадано, выходит надпись "Вы угадали. Хотите еще?(yes\no)" Если
    yes - то рестарт игры, если no - то брейк.
    """
    print(secret_num)  # for testing
    while True:
        player_num = int(input('Введи число от 1 до 100: ' ))
        if player_num == secret_num:
            print('Да. Загаданное число -', secret_num)
            break
        if player_num > secret_num:
            print('Нет, меньше')
            continue
        if player_num < secret_num:
            print('Нет, больше')
            continue        
        

def game():
    while True:
        secret_num = generation()
        print('Число загадано, начали!')
        ugadayka(secret_num)
        otvet = input('Сыграем еще разок? Да\Нет\n'  )
        if otvet.lower() == 'нет':
            print('Выход из игры')
            break
        continue

game()
