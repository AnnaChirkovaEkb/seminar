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

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


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


# 4. (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

print ("Input quantity in list ")
n = int (input())
a=[]
x=-n
for i in range(x,n+1):
    a.append(i)
print(a)


f = open('help.txt', 'r')
print('Position:')
print(f.read())
f.close()

f = open('help.txt', 'r')
b=f.read(1)
c=f.read(2)
# print(type(int(b)))
# print(b)
# print(f'{a[int(b)]} and * {a[int(c)]}')
e=a[int(b)]*a[int(c)]
print(f'The product of elementse will be {e}')
f.close()


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