import random


def generation():
    """ ���������� ����� �� 1 �� 100 ��������������
    """
    return random.randrange(0, 100)
    

def ugadayka(secret_num):
    """ ����� ������, ���� ����� �� ������� �����. ���� ���������� ����� 
    ������ ����������, ��������� "������", ���� ������ - "������". ���� 
    ����� �������, ������� ������� "�� �������. ������ ���?(yes\no)" ����
    yes - �� ������� ����, ���� no - �� �����.
    """
    print(secret_num)  # for testing
    while True:
        player_num = int(input('����� ����� �� 1 �� 100: ' ))
        if player_num == secret_num:
            print('��. ���������� ����� -', secret_num)
            break
        if player_num > secret_num:
            print('���, ������')
            continue
        if player_num < secret_num:
            print('���, ������')
            continue        
        

def game():
    while True:
        secret_num = generation()
        print('����� ��������, ������!')
        ugadayka(secret_num)
        otvet = input('������� ��� �����? ��\���\n'  )
        if otvet.lower() == '���':
            print('����� �� ����')
            break
        continue

game()
