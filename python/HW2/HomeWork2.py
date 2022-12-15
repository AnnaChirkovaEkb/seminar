# 1.  Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# print ("Input number ")
# num=(input())
# if "-" in num:
#     num = num.replace("-", "", )
# number=str(num)
# # print(type(number))
# # print(number)
# #
# if "." in number:
#     x = number.replace(".","",)
# else:
#     print('! Не найден')
#
# # print(x)
# suma= sum(int(c) for c in x)
# print('Suma =', suma)

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

# s = '0.56'
# summ = 0
# for i in s:
#     if i.isdigit():
#         summ += int(i)
# print(summ)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# print ("Input number ")
# num=int (input())
#
# def fact(n):
#     f = 1
#     for i in range(num):
#         f *= i + 1
#         print(f)
#     return f
#
#
# f = fact(num)
# print(f)
#
# print(f"Factorial number от 1 до {num} is {f}")

# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# print ("Input number ")
# n = int(input())
# lst = [round((1+1/a)**a, 3) for a in range(1, n+1)]
#
#
# print(f'Sequence is: {lst}')
# print(f'Summa is: {round(sum(lst), 3)}')
#
# n = int(input())
# summ = 0
# for i in range(1, n + 1):
#     summ += (1 + 1 / i) ** i
# print(summ)
#
# n = int(input('Введите число: '))

# def sequence(n):
#
#     return[round((1 + 1 / x)**x, 3) for x in range (1, n + 1)]


# 4. (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# print ("Input quantity in list ")
# n = int (input())
# a=[]
# x=-n
# for i in range(x,n+1):
#     a.append(i)
# print(a)
#
#
# f = open('help.txt', 'r')
# print('Position:')
# print(f.read())
# f.close()
#
# f = open('help.txt', 'r')
# b=f.read(1)
# c=f.read(2)
# # print(type(int(b)))
# # print(b)
# # print(f'{a[int(b)]} and * {a[int(c)]}')
# # e=a[int(b)]*a[int(c)]
# # print(f'The product of elementse will be {e}')
# # f.close()
#
# # решение от преподавателя
# from random import randint
# n = int(input('Введите число N - '))
# numbers = []
# for i in range(n):
#     numbers.append(randint(-n, n+1))
# print(numbers)
#
# f = open('file.txt', 'w')
# while True:
#     s = input('Укажите позицию для вычисления - ')
#     if s == "":
#         break
#     f.write(s+"\n")
# f.close()
#
# result = 1
# f = open('file.txt', 'r')
# for line in f:
#     if line == "":
#         break
#     result *= numbers[int(line)]
# f.close()
# print(result)



#5. Реализуйте алгоритм перемешивания списка.
# import random

# arr = [1, 2, 3, 4, 5, 6]
# n = len(arr)
# print (f'Old array is {arr}')
# for i in range(n):
#     j = random.randint(0, n-1)
#     a=arr.pop(j)
#     arr.append(a)
# print(f'New array is {arr}')

# import random
# list = ["Anna", "Alex", 3.14159, 0]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     temp = list[i]
#     list[i] = list[index_a]
#     list[index_a] = temp
# print(list)

import random
y = ['Apple', '2 ', '-5675 ', '0.678 ', 'morning']
random.shuffle(y)
print(y)
