# name = input('Введите имя: ')
# name = None if not name else name
# match name:
#     case None:
#         print('привет')
#     case something:
#         print(f'привет {name}')

# mount = input('Введите месяца: ')
# match mount:
#     case 'январь': print('привет')
#     case 'февраль': print('здравствуй')
#     case 'март': print('здарова')
#     case 'апрель': print('здравия')
#     case 'май': print('qq')
#     case 'июнь': print('ку')
#     case 'июль': print('салам')
#     case 'август': print('hi')
#     case 'сентябрь': print('hello')
#     case 'октябрь': print('приветствую')
#     case 'ноябрь': print('рад видеть')
#     case 'декабрь': print('добрый день')
#     case something: print(f'это не месяц')

# l = input('Введите числа через пробел: ').split()
# match l:
#     case (a,): print(f'1D: {a}')
#     case (a,b,): print(f'2D: {a}, {b}')
#     case (a,b,c,): print(f'3D: {a}, {b}, {c}')


# languages = input('Напишите язык: ')
# match languages:
#     case 'старославянский': print('приветъ')
#     case 'новоцерковнославянский': print('​приветъ')
#     case 'академическй': print('прывет')
#     case 'тарашкевица': print('прывет')
#     case 'словенский': print('privjet')
#     case 'древнерусский': print('привѣтъ')
#     case 'славеница': print('ⱂⱃⰹⰲⰵⱅ')
#     case _: print('Такого языка нет в списке')

from datetime import datetime
import time
import random

i = 0
never = input('Нажмите Enter что-бы начать...')
timer = []
time = []
Win = True

while i < 5:
    first_numb = random.randint(1, 100)
    second_numb = random.randint(1, 100)
    sign = random.randint(1, 2)
    if sign == 1:
        result = first_numb + second_numb
        print(f'{first_numb} + {second_numb} = ')
    else:
        result = first_numb - second_numb
        print(f'{first_numb} + {second_numb} = ')
    start = datetime.now()
    timer.append(int(input()))
    # if result == timer[i]:
    #     Win = True
    # elif result != timer[i]:
    #     Win = False
    #     i = 9
    finish = datetime.now()
    time.append(finish - start)
    print(f'Время: {finish - start}')
    i = i + 1
    
if Win == True:
    Time = time[0] + time[1] + time[2] + time[3] + time[4]
    Time = Time / 5
    print(f'Ваш средний результат: {Time}')
if Win == False:
    print('Вы проиграли!')
