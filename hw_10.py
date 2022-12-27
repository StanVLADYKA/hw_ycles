# 10. Создать матрицу 3*3, заполнить ее рандомными значениями.
# Заменить все четные числа на нули.

from random import randint

# ml = []


# t = random.randint(1,99)
# for i in range(0,3):
#     for b in range(0,3):
#         print(i,b)
# #        ml[i][b].append(t)
# print(ml)

ml = [[randint(0,99) for _ in range(3)] for _ in range(3)]

print(ml,"матрица первый вариант")

for i in range(0,3):
    for b in range(0,3):
        if ml[i][b] %2 == 0:
            ml[i][b] = 0
print(ml,"матрица первый вариант")