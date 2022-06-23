from bs4 import BeautifulSoup
import requests
import os
import django
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from Graphicscards.models import GraphicsCards

class CzcProduct:
    name = ''
    graphics_chip = ''
    price = ''

    def set_name(self):
        self.name = self.soup.find('h1').text.strip()

    def set_graphics_chip(self):
        self.graphics_chip = self.soup.find('div', class_='pd-parameter-item clearfix')
        self.graphics_chip = self.graphics_chip.find('p').find_next('p').text.strip(' \n\t')
        self.graphics_chip = self.graphics_chip.replace('Grafický čip:','')
        self.graphics_chip = re.sub(r"[\n\t\s]*", "", self.graphics_chip)
    
    def set_price(self):
        non_break_space = u'\xa0'
        self.price = self.soup.find('div', class_='total-price')
        self.price = self.price.find('span',class_='price-vatin').text.strip()
        self.price = self.price.replace(non_break_space,'')
        self.price = self.price.replace('Kč','')

    

    def __init__(self, url):
        r = requests.get(url)
        self.soup = BeautifulSoup(r.content, 'lxml')

        self.set_name()
        self.set_graphics_chip()
        self.set_price()

        gc = GraphicsCards(name=self.name, url=url, price=self.price, graphics_chip=self.graphics_chip)
        gc.save()