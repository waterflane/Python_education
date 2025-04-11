import logging
import requests
import bs4

logging.basicConfig(
    filename='Python/log_.log', 
    filemode='w', 
    level=logging.DEBUG, 
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def fetch(url):
    get = requests.get(url)
    ret = bs4.BeautifulSoup(get.text, "html.parser")
    logging.info(f'Текст {url}, успешно получен')
    ret = ret.text[:100]
    logging.info(f'Завершение работы с {url}')
    print(ret)
    print('-----------------------------------------------------------')
    return 0 

def fetch_all(urls):
    for i in urls:
        logging.info(f'Отправляем запрос по адресу {i}')
        try:
            r = requests.get(i)
            logging.info(f'Статус {r.status_code}, успешно')
            fetch(i)
        except Exception as Error:
            logging.error(f'Ошибка - {Error}')


URLS = [
    "https://example.com",
    "https://httpbin.org/delay/2",
    "https://python.org",
    "https://thisurldoesnotexist12345.com"  # намеренная ошибка
]

logging.debug('Функция запустилась')
fetch_all(URLS)