# 3. Напишите программу, которая на основе списка из натуральных чисел формирует целое число.
# Число формируется «объединением» элементов списка: например,
# если исходный список [12, 3, 456, 78], то программа должна получить число 12345678.

num_1 = [2,4,234,11,9,5]
num_2 = []
for i in num_1:
    i = str(i)
    for a in i:
        num_2.append(a)

num_3 = "".join(num_2)
num_3 = int(num_3)
print(num_3)
