# 8. Напишите программу, в которой решается уравнение вида
# А(А - 1)* x=sin(A) , причем при значении A = 0 должно вычисляться решение x= -1.

import math

a = int(input("enter A for А(А - 1)* x=sin(A):   "))


try:
    x = math.sin(a) / a * (a - 1)
    print("x =  :", x)
except ZeroDivisionError:
    x = -1
    print("x =  :", x)