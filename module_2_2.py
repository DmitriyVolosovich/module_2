first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first == third:
    print('Вы ввели 3 одинаковых числа')
elif(
        first == second
     or first == third
     or second == third):
    print('Вы ввели 2 одинаковых числа')
else:
    print('нет одинаковых чисел')