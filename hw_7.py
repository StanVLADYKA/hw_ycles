# 7. Напишите программу для решения квадратного уравнения.
# В процессе поиска решения использовать обработку исключитель-
# ных ситуаций.

#ax2 + bx + c = 0

# находим дискриминанту

a = 1
b = -3
c = -4

d = b**2 - 4*a*c

if d < 0:
    print("Нет действительных корней - дискримината отрицательна",d)
elif d ==0:
    x_1 = -b / 2 * a
    print(x_1, " - одно решение, дискримината равно нулю")
else:
    x_1 = (-b + d**0.5) / 2*a
    x_2 = (-b - d**0.5) / 2*a

    print(f"{x_1}  - первое решение,{x_1} - второе решение, (дискримината положительна)")