import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin
import pandas as pd
#from config import total


""" print("###############################################################")
print("# Beleza na Web Scraper - Dev. By Marcos Vinicius Madeira     #")
print("#         \033[1;33;40mhttps://wellyington.github.io/\033[0;37;40m               #")
print("#########################################################\n\n") """

class BelezaWeb:
    def __init__(self, url, class_id):        
        self.url = url
        
        self.class_id = class_id
    
    def scraping(self):

        url = self.url 
        search = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

        # Crian objeto BeautifulSoup
        soup = BeautifulSoup(search.content, 'html.parser')

        # pegar todo texto da class showcase-item-name
        dados_skus = soup.find_all('p', class_='btn btn-primary btn-block js-add-to-cart')
        id_sellers = soup.find_all('a', class_=f'{self.class_id}')
        #print(dados_skus)

        dados = []        
        # loop para iterar sobre todos os itens da lista
        for id_seller in id_sellers:
            #print(dados_sku['data-event'][2:-2],"\n")
            seller = id_seller['data-sku'][3:-3]
            print(seller)
            dados.append(seller)
            for line in dados:
                print(line)
            df = pd.DataFrame(dados, columns=['scraping'])
            
            df.to_excel('report_web.xlsx', index=True)

            
                             

if __name__ == "__main__":
    file = pd.read_excel('belezaa_web.xlsx')
    url = file['url'].astype(str)     
    class_id = 'btn btn-primary btn-block js-add-to-cart' 


    df = pd.DataFrame()
    for i in url:          
        result = BelezaWeb(i, str(class_id))      
        result.scraping()
        
        """ for line in result:
            df = df.append(line, ignore_index=True)
        df.describe()
        df.to_excel('report_web.xlsx') """



        
                
            

        








