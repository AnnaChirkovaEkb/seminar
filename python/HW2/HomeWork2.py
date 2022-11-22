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

print ("Input number ")
n = int(input())
lst = [round((1+1/a)**a, 3) for a in range(1, n+1)]


print(f'Sequence is: {lst}')
print(f'Summa is: {round(sum(lst), 3)}')


# 4. (ЕСЛИ НЕ ЗНАЕТЕ КАК ДЕЛАТЬ, МОЖНО НЕ ВЫПОЛНЯТЬ)
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


#5. Реализуйте алгоритм перемешивания списка.

