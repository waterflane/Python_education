import datetime
import calendar

def get_working_days(start_date, end_date, holidays):
    holiday_days = 0
    delta = end_date - start_date
    delta_days = delta.days

    for i in range(delta_days):
        current_day = start_date + datetime.timedelta(days=i)
        if current_day.weekday() > 4 or current_day in holidays: holiday_days += 1

    print(f'Начало отпуска сотрудника - {first}, середина - {start_date + datetime.timedelta(days=delta_days//2)}, конец отпуска - {end_date}.')  

    Y1 = start_date.strftime('%Y')
    M1 = start_date.strftime('%m')
    Y2 = end_date.strftime('%Y')
    M2 = end_date.strftime('%m')
    print(calendar.month(int(Y1),int(M1)))
    if M1 != M2: print(calendar.month(int(Y2),int(M2)))

    return holiday_days

def main():
    holidays = [
        datetime.date(2024, 11, 4),
        datetime.date(2024, 1, 1),
        datetime.date(2024, 2, 23),
        datetime.date(2024, 3, 8),
        datetime.date(2024, 5, 9)
    ]
    print(f'Ваш сотрудник будет на отпуске: {get_working_days(first, second, holidays)} выходных дней.')

start = '01.11.2024'
end = '08.11.2024'
first = datetime.datetime.strptime(start, '%d.%m.%Y').date()
second = datetime.datetime.strptime(end, '%d.%m.%Y').date()
main()