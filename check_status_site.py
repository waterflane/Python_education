import logging
import requests

logging.basicConfig(
    filename='test_log.log', 
    filemode='w', 
    level=logging.DEBUG, 
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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
def fetch_url(url):
    logging.info('Отправляем запрос по адресу {url}')
    try:
        r = requests.get(url)
        logging.info(f'Статус {r.status_code}, успешно')
        return r.status_code
    except Exception as Error:
        logging.error(f'Ошибка - {Error}')

logging.debug('Функция запустилась')
fetch_url('https://examprle.com')