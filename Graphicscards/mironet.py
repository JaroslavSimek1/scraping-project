from bs4 import BeautifulSoup
from Graphicscards.mironetProduct import MironetProduct
import requests
import re


def find_all_products_mironet():
    baseurl = 'https://www.mironet.cz'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    }

    r = requests.get('https://www.mironet.cz/graficke-karty+fc14402/?modal=0&pn10658[]=+Jen+nov%C3%A9&pn6227[]=Skladem')
    soup = BeautifulSoup(r.content, 'lxml')

    product_list = soup.find_all('div', class_='item_obr')

    product_urls = []

    max_page = soup.find('a', class_='PageNew').text.strip()
    for l in range(1, int(max_page)):
        for product in product_list:
            for link in product.find_all('a', href=True):
                product_urls.append(baseurl + link['href'] + '#parametry')
        for i in range(0,len(product_urls)):
            m = MironetProduct(product_urls[i])

if __name__ == '__main__':
    find_all_products_mironet()
