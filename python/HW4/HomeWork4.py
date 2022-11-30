# 1.  Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#
# def round_pi(d: int) -> float:
#     pi, sign, m = 3, 1, 2
#     while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
#         pi = pi + sign*4/(m**3+3*m**2+2*m)
#         sign = -1*sign
#         m = m+2
#     return round(( pi+ (pi  +sign*4/(m**3+3*m**2+2*m)))/2, d)
#
# d = int(input('Введите точность определения числа ПИ (количество знаков после запятой): '))
# pi = round_pi(d)
# print(f'С точностью {d=}, число {pi=}; ')

# from math import pi
#
# def round_pi(n):
#     return '{:.{}f}'.format(pi, n)
#
# d = int(input('Введите точность определения числа ПИ (количество знаков после запятой): '))
# pi = round_pi(d)
# print(f'С точностью {d=}, число {pi=}; ')


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_number(n: int):
    i = 2
    while n % i != 0 or i == n - 1:
        i += 1
    if i == n:
        return n

# def simple_list(n: int) -> list:
#     simple_list1 = [1]
#     for i in range(2, n+1):
#         if n % i == 0:
#             if simple_number(i) != None:
#                 simple_list1.append(simple_number(i))
#             else:
#                 continue
#     return simple_list1
#
# n = int(input('Введите натуральное число N: '))
# simple_list1 = simple_list(n)
# print(f'Варианты:\n{simple_list1}')
# print(simple_list1)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

# import random
#
# def first_list(n, min, max) -> list:
#     number_list = [random.randint(min, max)]
#     for i in range (1, n):
#         number_list.append(random.randint(min, max))
#     return number_list
#
# def list1(user_list) -> list:
#     new_list = [user_list[0]]
#     for i in range(1, len(user_list)):
#         for j in range(len(new_list)):
#             if user_list[i] == new_list[j]:
#                 break
#             elif j == len(new_list)-1:
#                 new_list.append(user_list[i])
#     return new_list
#
#
# size = int(input('Введите количество: '))
# min=int(input('Введите от: '))
# max=int(input('Введите до: '))
#
# source_list = first_list(size, min, max)
# list = list1(source_list)
# print(f'{source_list} ->')
# print(list)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.