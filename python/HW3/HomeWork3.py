# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
#
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# list1=[]
# list1=[2,3,5,9,3]
# sum=0
# for i in range(0, len(list1)):
#     if i%2 > 0:
#         sum = sum + list1[i]
#         i+=1
#     else:
#         i+=1
# print(sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# list1=[2,3,4,5,6]
# list2=[]
# for i in range(0, len(list1)):
#     if i in range(0, len(list1)//2):
#         list2.append(list1[i]*list1[len(list1)-1-i])
#         i+=1
#     elif len(list1)%2>0:
#         if i in range(0, len(list1) // 2+1):
#             list2.append(list1[i] * list1[len(list1) - 1 - i])
#             i += 1
#
# print(list2)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# # была идея с разницей массивов, но не получилось, как элемент вычислить и  перевести в число
# и как избежать 0

# list1=[1.1, 1.2, 3.1, 5, 10.01]
# list2=[]
# for i in range(0, len(list1)):
#     list2.append(round(list1[i]*100))
#     i+=1
# list3=[]
# for j in range(0, len(list2)):
#     if list2[j]%100==0:
#         j+=1
#     elif list2[j] > 99:
#         list3.append(round(list2[j]) % 100)
#         j += 1
#     else:
#         list3.append(round(list2[j]))
#         j += 1
# print(list1)
# print(list2)
# print(list3)
# print(f'Different in fractional part is {max(list3)-min(list3)}')


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11

# print ("Input number ")
# n = int(input())
# num =''
# while n> 0:
#     num= str(n % 2) +num
#     n = n // 2
# print(num)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

print ("Input number ")
n = int(input())

def fib(n):
    fibo= []
    a, b = 1, 1
    for i in range(n):
        fibo.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibo.insert(0, a)
        a, b = b, a - b
    return fibo

fibo_nums =fib(n)
print(fib(n))
# print(fibo.index(0))