# print ("a")
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# print ("Input number of  day in week");
# a=int (input());
# if 6>a>0:
#     print ("workday")
# elif a>=8 or a<=0:
#     print ("Error")
# else:
#     print ("weekend")

# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("????????????????")

# 3.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# print ("Input coorditate if point X")
# x=float (input())
# print ("Input coorditate if point Y")
# y=float (input())

# print ("The point is in quarter number")
# if x>0 and y>0:
#     print ("1")
# elif x<0 and y>0:
#     print ("2")
# elif x<0 and y<0:
#     print ("3")    
# else:
#     print ("4")

# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# print ("Input quarter for point")
# a=int (input())

# if a==1:
#     print ("Diapozone coorditate of point x (0;+...) and y (0;+...)")
# elif a==2:
#     print ("Diapozone coorditate of point x (-...;0) and y (0;+...)")
# elif a==3:
#     print ("Diapozone coorditate of point x (-...;0) and y (-...;0)")
# elif a==4:
#     print ("Diapozone coorditate of point x (0;+...) and y (-...;0)")
# else:
#      print ("Error")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние 
# между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print ("Input coorditate of first point X1")
x1=float (input())
print ("Input coorditate of first point Y1")
y1=float (input())

print ("Input coorditate of second point X2")
x2=float (input())
print ("Input coorditate of second point Y2")
y2=float (input())