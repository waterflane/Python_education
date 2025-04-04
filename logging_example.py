import logging
import requests

logging.basicConfig(
    filename='Python/test_log.log', 
    filemode='w', 
    level=logging.DEBUG, 
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug('Это дебаг файлик')
logging.info('как дебаг стик в майне но не то')
logging.info('пока всё хорошо')

try:
    1/0
except ZeroDivisionError:
    logging.critical('Ты тупой зачем запустил программу которая делит на ноль! О чем ты вообще думал когда запускал эту программу, а если я бы вирус тебе подкинул? Вот пойди и подумай о своём поступке!')


logging.debug('Я программа выполняю то что ты написал и говорю что сеё час я использую декораторы!')

def call_log(func):
    def wrapper(*args, **kwargs):
        logging.info(f'''
                     имя функции {func.__name__}
                     args для функции {args}
                     kwargs {kwargs}''')
        result = func(*args, **kwargs)
        logging.info(f'Функция вернула {result}')
        return result
    return wrapper

@call_log
def add(a,b):
    return a + b

add(12, 8)


# @call_log
# def fetch_url(url):
#     logging.info('Отправляем запрос по адресу {url}')
#     try:
#         r = requests.get(url)
#         logging.info(f'Статус {r.status_code}, успешно')
#         return r.status_code
#     except Exception as Error:
#         logging.error(f'Ошибка - {Error}')

# logging.debug('Функция запустилась')
# fetch_url('https://examprle.com')