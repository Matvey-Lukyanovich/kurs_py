for i in range(2):
    try:
        years = int(input('Введите год рождения: '))
        month = int(input('Введите месяц рождения: '))
        years_now = 2024
        month_now = 6

        #сколько лет (без расчета месяцев)
        s = years_now - years
        #сколько полных месяцев
        month_age = month + month_now

        if month_age >= 12:
           s -= 1
        print(s)
    except TypeError:
        print('TypeError')
    except ValueError:
        print('ValueError')

