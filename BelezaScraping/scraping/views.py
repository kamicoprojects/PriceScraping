from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin
import os
clear = lambda: os.system("clear")
clear()
#from config import total


print("###############################################################")
print("# Beleza na Web Scraper - Dev. By Marcos Vinicius Madeira     #")
print("#         \033[1;33;40mhttps://wellyington.github.io/\033[0;37;40m               #")
print("#########################################################\n\n")

class BelezaWeb:
    def __init__(self, url, number_pages):
        
        self.url = url
        self.number_pages = number_pages
    
    
    def scraping(self):        
        for i in range(self.number_pages):
            url = self.url + '&page=' + str(i)
            search = requests.get(
                url, headers={'User-Agent': 'Mozilla/5.0'})
            
            # Crian objeto BeautifulSoup
            soup = BeautifulSoup(search.content, 'html.parser')

            # pegar todo texto da class showcase-item-name
            dados_skus = soup.find_all(class_='showcase-item js-event-product-click')
            id_sellers = soup.find_all(class_='btn btn-primary btn-block js-add-to-cart')

            # pegar o texto de todas as instancias da tag <a> dentro da div showcase-item-name
            """ lista_nome_produto_items = lista_nome_produto.find_all('showcase-item js-event-search', 'data-event') """


            # loop para iterar sobre todos os itens da lista
            for dados_sku, id_seller in zip (dados_skus, id_sellers):
                #sleep(0.2)
                teste = print(dados_sku['data-event'][2:-2],"\n")
                #datas = print(dados_sku['data-event'][2:-2],"\n" + ' - ' + id_seller['data-sku'][2:-2], "\n")
                #sellers = print(id_seller['data-sku'][2:-2],"\n")

                print(teste['sku'], "\n", teste['produto'], "\n", teste['price'], "\n")
            """ for seller in id_sellers:
                print(seller['data-sku'] + ' - ' + seller['data-seller'])
                sleep(0.2)
 """


if __name__ == "__main__":
    app = BelezaWeb('https://www.belezanaweb.com.br/truss?tab=produtos',10)
    app.scraping()



    









