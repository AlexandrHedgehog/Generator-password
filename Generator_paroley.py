import random

alfa = ['q','w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',]
inter = ['1','2','3','4','5','6','7','8','9','0']
sign = ['!','@','#','$','%','&','*','<','>']

print('Добро пожаловать в генератор паролей!')
number_of_alfa = int(input('Колличество букв в пароле: '))
number_of_inter = int(input('Колличество цифр в пароле: '))
number_of_sign = int(input("Колличество знаков в пароле: "))
passw = []
for i in range(1, number_of_alfa + 1):
    passw += random.choice(alfa)
for i in range(1, number_of_inter + 1):
    passw += random.choice(inter)
for i in range(1, number_of_sign + 1):
    passw += random.choice(sign)
random.shuffle(passw)
passw_1 = ''
for i in passw:
    passw_1 += i

print('Твой пароль: ', passw_1)