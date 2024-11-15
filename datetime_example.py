import datetime


somedate = datetime.date(2012, 9, 1)
print(somedate)

today = datetime.date.today()
print(today)

print(f'Сегодня {today.day}, {today.weekday()}, месяц {today.month}, год {today.year}!')

timer = datetime.time(12, 2, 6)
print(timer)

today2 = datetime.datetime.now()
print(today2)
print(f'Время: {today2.time()}')