import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin


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
            dados_sku = soup.find_all(class_='showcase-item js-event-search')
            id_seller = soup.find_all(class_='item-discount')

            # pegar o texto de todas as instancias da tag <a> dentro da div showcase-item-name
            """ lista_nome_produto_items = lista_nome_produto.find_all('showcase-item js-event-search', 'data-event') """


            # loop para iterar sobre todos os itens da lista
            for dados_skus in dados_sku:
                sleep(0.2)
                data_event = print(dados_skus['data-event'][1:-1])
                """   response = {
                    'sku': dados_skus('sku'),
                    'produto': dados_skus.get('productName'),
                    'price': dados_skus.get('price')
                }
                print(response) """


if __name__ == "__main__":
    app = BelezaWeb('https://www.belezanaweb.com.br/busca/?q=kit%20truss%20miracle%20duo%20(2%20produtos)', 10)
    app.scraping()



    








