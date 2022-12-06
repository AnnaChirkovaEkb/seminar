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

# вариант2
# import math
# d = input('Введите число d указывающее степень округления числа pi ')
# d = d[2:len(d)]
# print(round(math.pi,len(d)))
#
# # вариант3
# a = int(input('введите нужную точность 1#= '))
#  pi_target = 0
#  for i in range(1, 1000000):
#      pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
#  print(str(pi_target)[:a + 2])


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# def simple_number(n: int):
#     i = 2
#     while n % i != 0 or i == n - 1:
#         i += 1
#     if i == n:
#         return n

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

# second variant
#
# n = int(input("Введите число N: "))
# i = 2
# list = []
#
# while i <= n:
#     if n % i == 0:
#         list.append(i)
#         n //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители введенного числа указаны в списке: {list}")


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

# 2
numbers = list(map(int, input("Введите числа через пробел:\n").split()))
print(numbers)
new_numbers = []

for i in numbers:
    if i not in new_numbers:
        new_numbers.append(i)
print(new_numbers)

# 3
def elements(nums):
    nums = [int(i) for i in nums.split()]
    return list(set(nums))

numbers = '1 1 2 2 3 455 66 66 2 1'
print(elements(numbers))
a= [1,2,2,2,2,3,1,4]

print(set(a))

# 4
b = [1, 1, 2, 3, 3, 4, 5]
 a = []
 for i in b:
    if b.count(i) == 1:
         a.append(i)

 print(a)



# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random
#
#
# def write_file(st):
#     with open('num4.txt', 'a') as data:
#         data.write(st)
#
#
# def rnd():
#     return random.randint(0, 101)
#
#
# def create_mn(k):
#     lst = [rnd() for i in range(k + 1)]
#     return lst
#
#
# def create_str(sp):
#     lst = sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst) - i - 1}'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr
#
#
# k = int(input("Введите натуральную степень k = "))
# koe = create_mn(k)
# write_file(create_str(koe))


# 2
from random import randint

k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
    koefs.append(randint(1, 100))

ans = list()
for i in range(len(koefs)):
    if k == 1:
        ans.append(f'{koefs[i]}*x')
    elif k == 0:
        ans.append(f'{koefs[i]}')
    else:
        ans.append(f'{koefs[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        ans.append('+')
    elif flag == 0:
        ans.append('-')
    k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(ans))
fout.close()

# 3
import random
from numpy.polynomial import Polynomial as P

p = P([0, 0, -2,])

print(p)

k = random.randint(1, 4)
print(k)
poly = p ** k
print(poly)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов.

with open('num5_1.txt', 'r') as data:
    st1 = data.readlines()
with open('num5_2.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = [st1]
lst2 = [st2]

lst_new = [lst1[i]+lst2[i] for i in range(len(lst2))]
# print (lst_new)
st3=str(lst_new)

with open('num5_3.txt', 'w') as data:
    data.writelines(st3)
with open('num5_3.txt', 'r') as data:
    st4 = data.readlines()
print(f"Результирующий многочлен {st4}")


import random
def nmnogochlen1(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res
рандом в функции

# import random
# def x(b=None):
#     if b is None:
#         b = random.randint(1, 10)
#
#     a=b+1
#     print(a)
# x_random1=x()
# x_random2=x()


def nmnogochlen2(a=random.randint(1, 100), b=random.randint(0, 100), c=random.randint(0, 100), res='') -> str:
    if b > 0:
        res += '+' + str(b) + '*x'
    if c > 0:
        res += '+' + str(c)
    return f'{a}*x^2' + res


# 2
f = open('dz40.txt', 'w')
f.write(nmnogochlen1())
f = open('dz40.txt', 'r')
list_5 = str(f.readline()).split('x')
c1 = b1 = a1 = 0
if len(list_5) == 3:
    c1 = list_5[2][1:]
if len(list_5) >= 2:
    b1 = list_5[1][3:-1]
a1 = list_5[0][:-1]
f.close()

f = open('dz41.txt', 'r')
list_51 = str(f.readline()).split('x')
c2 = b2 = a2 = 0
if len(list_51) == 3:
    c2 = list_51[2][1:]
if len(list_51) >= 2:
    b2 = list_51[1][3:-1]
a2 = list_51[0][:-1]
f.close()

f = open('dz42.txt', 'w')
f.write(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
print(nmnogochlen1(int(a1) + int(a2), int(b1) + int(b2), int(c1) + int(c2)))
f.close()

# 3
# ffile1 = open('file1.txt', 'r')
# ffile2 = open('file2.txt', 'r')
# ffile3 = open('file3.txt', 'w')
# file1 = ffile1.readline()
# file2 = ffile2.readline()
# for i in range(len(file1)):
#     if file1[i-1] != '^':
#         if file1[i].isnumeric():
#             ffile3.write(str(int(file1[i])+int(file2[i])))
#         else:
#             ffile3.write(str(file1[i]))
#     else:
#         ffile3.write(str(file1[i]))
# ffile1.close
# ffile2.close
# ffile3.close

