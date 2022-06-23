from unicodedata import name
from bs4 import BeautifulSoup
import requests
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

from Graphicscards.models import GraphicsCards

class MironetProduct:
    name = ''
    graphics_chip = ''
    price = ''

    def set_name(self):
        self.name = self.soup.find('div', class_='product_name').text.strip()

    def set_graphics_chip(self):
        self.graphics_chip = self.soup.find('td', class_='ParamValue').find_next('td', class_='ParamValue').find_next('td', class_='ParamValue').text.strip()
        self.graphics_chip = self.graphics_chip.replace(' ','')
        self.graphics_chip = self.graphics_chip.replace('-','')
        self.graphics_chip = self.graphics_chip.replace('AMD','')
        self.graphics_chip = self.graphics_chip.replace('NVIDIA','')
    
    def set_price(self):
        non_break_space = u'\xa0'
        
        self.price = self.soup.find('div',class_='product_cena_box')
        self.price = self.price.find('span',class_='product_dph').text.strip()
        self.price = self.price.replace(non_break_space,'')
        self.price = self.price.replace('Kč','')


    def __init__(self,url):
        r = requests.get(url)
        self.soup = BeautifulSoup(r.content, 'lxml')

        self.set_name()
        self.set_graphics_chip()
        self.set_price()
        
        gc = GraphicsCards(name=self.name, url=url, price=self.price, graphics_chip=self.graphics_chip)
        gc.save()
