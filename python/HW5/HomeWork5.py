# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
import random
# вариант от преподавателя
# with open('text.txt', 'r', encoding = 'utf_8') as data:
# stroka = data.read().split()
# print(f'В файле записано: {stroka}')
# print('Удалили все слова с абв и получили: ')
# print(' '.join([word for word in stroka if 'абв' not in word]))
# print()

# вариант2
# text = 'ываабв лповап абвцукв алоабвабв ываываыв'
# print('Исходный текст: ', text)
# text_new= text.split()
# find = 'абв'
# new_text = []
#
# for i in text_new:
#     if find not in i:
#         new_text.append(i)
#
# text_2 = ' '.join(new_text)
# print('Полученный текст: ', text_2)

# 2. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому
# игроку,чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""

# вариант А
# print('Game')
# sum_konf=50
# print(sum_konf)
#
# game_over = False
# while game_over == False:
#     print('Ходит первый игрок А')
#     print('Сколько конфет вы берете?')
#     a=int(input())
#     if a>sum_konf:
#         print('Error!Выберете другой ход')
#     if 0>a>28:
#         print('Error!Выберете другой ход c 1 до 28!')
#     else:
#         sum_konf = sum_konf - a
#
#     print(f'Остаток конфет {sum_konf}')
#
#     # !!!блок повторяется два раза
#     if sum_konf == 0:
#         game_over = True
#         print('Победил игрок A!')
#     else:
#         game_over = False
#
#     while game_over == False:
#         print('Ходит второй игрок B')
#         b=random.randint(1,28)
#         print(b)
#         if a>sum_konf:
#             print('Error!Выберете другой ход:')
#             b = random.randint(1,sum_konf)
#             sum_konf = sum_konf - b
#             print(b)
#         else:
#             sum_konf = sum_konf - b
#         print(f'Остаток конфет {sum_konf}')
#
#         if sum_konf == 0:
#             game_over = True
#             print('Победил игрок B!')
#         else:
#             game_over = False

#вариант Б

#
# print('Game')
# sum_konf=50
# print(sum_konf)
#
# varion=random.randint(1,2)
# print(varion)
#
# if varion==1:
#     game_over = False
#     while game_over == False:
#         print('Ходит первый игрок А')
#         print('Сколько конфет вы берете?')
#         a=int(input())
#         if a>sum_konf:
#             print('Error!Выберете другой ход')
#         if 0>a>28:
#             print('Error!Выберете другой ход c 1 до 28!')
#         else:
#             sum_konf = sum_konf - a
#
#         print(f'Остаток конфет {sum_konf}')
#
#         # !!!блок повторяется два раза
#         if sum_konf == 0:
#             game_over = True
#             print('Победил игрок A!')
#         else:
#             game_over = False
#
#         while game_over == False:
#             print('Ходит второй игрок B')
#             b=(sum_konf%28)+1
#             print(b)
#             if b>sum_konf:
#                 print('Error!Выберете другой ход:')
#                 b = sum_konf
#                 sum_konf = sum_konf - b
#                 print(b)
#             else:
#                 sum_konf = sum_konf - b
#             print(f'Остаток конфет {sum_konf}')
#
#             if sum_konf == 0:
#                 game_over = True
#                 print('Победил игрок B!')
#             else:
#                 game_over = False
#
# if varion==2:
#     game_over = False
#     while game_over == False:
#         print('Ходит второй игрок B')
#         b = sum_konf % (28 + 1)
#         print(b)
#         if b > sum_konf:
#             print('Error!Выберете другой ход:')
#             b = random.randint(sum_konf)
#             sum_konf = sum_konf - b
#             print(b)
#         else:
#             sum_konf = sum_konf - b
#         print(f'Остаток конфет {sum_konf}')
#
#         # !!!блок повторяется два раза
#         if sum_konf == 0:
#             game_over = True
#             print('Победил игрок A!')
#         else:
#             game_over = False
#
#         while game_over == False:
#             print('Ходит первый игрок А')
#             print('Сколько конфет вы берете?')
#             a = int(input())
#             if a > sum_konf:
#                 print('Error!Выберете другой ход')
#             if 0 > a > 28:
#                 print('Error!Выберете другой ход c 1 до 28!')
#             else:
#                 sum_konf = sum_konf - a
#             print(f'Остаток конфет {sum_konf}')
#
#             if sum_konf == 0:
#                 game_over = True
#                 print('Победил игрок B!')
#             else:
#                 game_over = False
#
# 3.Создайте программу для игры в ""Крестики-нолики"".

# a=list["|",1,'|',2,'|',3,'|','\n',"|",4,'|',5,'|',6,'|','\n',"|",7,'|',8,'|',9,'|','\n']
# x=('\n',"|",1,'|',2,'|',3,'|','\n',"|",4,'|',5,'|',6,'|','\n',"|",7,'|',8,'|',9,'|','\n')
# y=str(x)
# print('\n',"|",1,'|',2,'|',3,'|','\n',"|",4,'|',5,'|',6,'|','\n',"|",7,'|',8,'|',9,'|','\n')
#
# maps = [1, 2, 3,
#         4, 5, 6,
#         7, 8, 9]
#
# # Инициализация победных линий
# victories = [[0, 1, 2],
#              [3, 4, 5],
#              [6, 7, 8],
#              [0, 3, 6],
#              [1, 4, 7],
#              [2, 5, 8],
#              [0, 4, 8],
#              [2, 4, 6]]
#
#
# # Вывод карты на экран
# def print_maps():
#     print('|', maps[0], end="|")
#     print(maps[1], end="|")
#     print(maps[2], end="|\n")
#
#     print('|',maps[3], end="|")
#     print(maps[4], end="|")
#     print(maps[5], end="|\n")
#
#     print('|',maps[6], end="|")
#     print(maps[7], end="|")
#     print(maps[8], end="|\n")
# print(print_maps())
#
# def result():
#     win=''
#     for i in victories:
#         if  maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"
#     return win
#
# game_over = False
# while game_over == False:
#     print('Ходит первый игрок Х')
#     x=int(input())-1
#     if x in range (0,9):
#         if maps[x]=='X' and maps[x]=='O':
#             print('Error!Выберете другой ход')
#         else:
#             maps[x] = 'X'
#
#     print(print_maps())
#
#     print('Ходит второй игрок O')
#     y=int(input())
#     if y in range(0,9):
#         if maps[y] == 'X' and maps[y]=='O':
#             print('Error!')
#         else:
#             maps[y] = 'O'
#     print(print_maps())
#
#     win=result()
#     if win !="":
#         game_over = True
#     else:
#         game_over = False
#
# print_maps()
# print(f'Победил, {result()}')


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('555.txt', 'r') as data:
#     st1 = data.readline()
# print(f"Текст {st1}")
#
# st2=''
# c = st1[0]
# count=1
# for i in range(1, len(st1)):
#
#     if st1[i] == c:
#         count += 1
#
#     else:
#         st2 = st2 + str(count) + c+ " "
#         count=1
#         c = st1[i]
#     i+=1
# print(f'New rip:  {st2}')
#
# with open('rip555.txt', 'w') as data:
#     data.writelines(st2)
# with open('rip555.txt', 'r') as data:
#     st4=data.readlines()
# print(st4)
