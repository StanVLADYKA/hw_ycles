# написать программу, которая будет запрашивать у пользователя пароль до тех пор,
# пока он не удовлетворит условиям:
# длина пароля не менее 8 символов
# пароль не содержит в себе имя пользовател

n_1 = input("Input Name: ")
p_1 = input("Input Password: ")

while len(p_1) < 8 or n_1 in p_1:
    print("password is not correct")
    p_1 = input("Input Password :")