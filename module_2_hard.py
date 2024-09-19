from random import random, randint

n = input('Введите число от 3 до 20 или нажмите "Enter" :')
if n == '':
    n = randint(3,20)
else:
    while int(n) < 3 or int(n) > 20:
        n = input('От 3-х до 20-и. Ещё раз :')
i=1
j=2
pass_list = []
password = ''
while i < j and i + j < int(n):
    while (i + j) <= int(n):
        if int(n) % (i + j) == 0:
            pass_list.append(i)
            pass_list.append(j)
        j += 1
    i += 1
    j = i + 1
for elem in pass_list:
    password += str(elem)
print(f'Пароль к числу {n}: {password}')
