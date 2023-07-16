import requests
from bs4 import BeautifulSoup
import logging

def post_from_link(url):
    response = requests.get(url)

    logging.info(f'Запрошен URL: {url}.')
    logging.info(f'Время доступа: {response.elapsed.total_seconds()} сек.')

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html,'html.parser')
        tags = soup.find_all(['h1','h2','h3','h4','h5','h6','p','span'])
        for tag in tags:
            print(tag.text)
    else:
        logging.error(f'Ошибка при получении контента. Код ошибка: {response.status_code}')


logging.basicConfig(filename='post_from_link.log',level=logging.INFO,format='%(asctime)s : %(levelname)s : %(message)s')

url = input("Введите URL: ")

post_from_link(url)
