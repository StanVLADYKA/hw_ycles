# 4. Напишите программу, в которой пользователь вводит три целых чила,
# а программа проверяет, являются ли эти числа тремя последовательными
# элементами арифметической последовательности. В арифметической
# последовательности каждый новый член получается прибавления к
# предыдущему определенного фиксированного числа.

n_1 = int(input("enter 1 number :"))
n_2 = int(input("enter 1 number :"))
n_3 = int(input("enter 1 number :"))

a_1 = n_1 - n_2
a_2 = n_2 - n_3

if abs(a_1) == abs(a_2):
 print("arithmetic sequence")
else:
 print("arithmetic not sequence")

