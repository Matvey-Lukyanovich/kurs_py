d1= int(input('Введите день рождения 1: '))
m1 = int(input('Введите месяц рождения 1: '))
y1 = int(input('Введите год рождения 1: '))
if m1>12 or d1>31:
    print("Некорректная дата. Повторно запустите программу")

d2= int(input('Введите день рождения 2: '))
m2 = int(input('Введите месяц рождения 2: '))
y2 = int(input('Введите год рождения 2: '))
if m2>12 or d2>31:
    print("Некорректная дата. Повторно запустите программу")

d1 = d1 + (m1 * 30) + (y1 * 365);
d2 = d2 + (m2 * 30) + (y2 * 365);

if(d2 > d1) :
    print("Старше первый")
elif (d2 < d1):
    print("Старше второй")
elif (d2 == d1):
        print("Они равны! ")