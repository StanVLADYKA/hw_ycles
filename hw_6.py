# 6. Напишите программу для решения уравнения Aх = В - А - 1. Па-
# раметры А и В вводятся пользователем. Уравнение имеет решение
# х =(B - 1) / А - 1 если A ± 0. При A = 0 и В = 1 решением является любое число,
# а при А = 0 и В + 1 решений у уравнения нет. Предложите разные варианты программы,
# в том числе и с использованием обработки исключительных ситуаций.

a = int(input("enter A:  "))
b = int(input("enter B:  "))

if a != 0:
        x = (b - 1) / a - 1
        print(x)
elif a == 0 and b == 1:
    try:
        x = (b - 1) / a - 1
    except ZeroDivisionError:
        print("!!! * / 0")
        x = 42
        print(x)
elif a == 0 and b > 1:
    try:
        x = (b - 1) / a - 1
    except ZeroDivisionError:
        print("no solution to the equation")
elif a == 0 and b == 0:
    try:
        x = (b - 1) / a - 1
    except ZeroDivisionError:
        raise ValueError
    finally:
        print(" 0/0")

