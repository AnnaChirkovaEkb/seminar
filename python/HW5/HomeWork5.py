# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open('text.txt', 'r', encoding = 'utf_8') as data:
# stroka = data.read().split()
# print(f'В файле записано: {stroka}')
# print('Удалили все слова с абв и получили: ')
# print(' '.join([word for word in stroka if 'абв' not in word]))
# print()

# 2. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""




#
# 3.Создайте программу для игры в ""Крестики-нолики"".

# a=list["|",1,'|',2,'|',3,'|','\n',"|",4,'|',5,'|',6,'|','\n',"|",7,'|',8,'|',9,'|','\n']
# x=('\n',"|",1,'|',2,'|',3,'|','\n',"|",4,'|',5,'|',6,'|','\n',"|",7,'|',8,'|',9,'|','\n')
# y=str(x)
# print('\n',"|",1,'|',2,'|',3,'|','\n',"|",4,'|',5,'|',6,'|','\n',"|",7,'|',8,'|',9,'|','\n')
#
maps = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]


# Вывод карты на экран
def print_maps():
    print('|', maps[0], end="|")
    print(maps[1], end="|")
    print(maps[2], end="|\n")

    print('|',maps[3], end="|")
    print(maps[4], end="|")
    print(maps[5], end="|\n")

    print('|',maps[6], end="|")
    print(maps[7], end="|")
    print(maps[8], end="|\n")
print(print_maps())

def result():
    win=''
    for i in victories:
        if  maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"
    return win

game_over = False
while game_over == False:
    print('Ходит первый игрок Х')
    x=int(input())-1
    if x in range (0,9):
        if maps[x]=='X' and maps[x]=='O':
            print('Error!Выберете другой ход')
        else:
            maps[x] = 'X'

    print(print_maps())

    print('Ходит второй игрок O')
    y=int(input())
    if y in range(0,9):
        if maps[y] == 'X' and maps[y]=='O':
            print('Error!')
        else:
            maps[y] = 'O'
    print(print_maps())

    win=result()
    if win !="":
        game_over = True
    else:
        game_over = False

print_maps()
print(f'Победил, {result()}')


    # 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.