# print ("a")
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

print ("Input number of  day in week");
a=int (input());
if 6>a>0:
    print ("workday")
elif a>=8 or a<=0:
    print ("Error")
else:
    print ("weekend")
