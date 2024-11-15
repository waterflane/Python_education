import calendar
import datetime

print(f'Сейчас: {datetime.datetime.now()}')
custom_date = input('Введите дату в формате День.Meсяц.Год: ')
custom_date = datetime.datetime.strptime(custom_date, '%d.%m.%Y').date()
custom_date_Year = custom_date.strftime('%Y')
custom_date_Month = custom_date.strftime('%m')
delta = datetime.datetime.now().date() - custom_date


print(f'Ваша дата: {custom_date}')
print(f'Календарь на{calendar.month(int(custom_date_Year), int(custom_date_Month))}')
print(f'Через 7 дней будет: {custom_date + datetime.timedelta(days=7)}')
print(f'Разница между сегодня и {custom_date}: {delta.days} дней!')