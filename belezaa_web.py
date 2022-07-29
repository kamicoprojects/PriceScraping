from numpy import index_exp
import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
import re   
#from config import total


""" print("###############################################################")
print("# Beleza na Web Scraper - Dev. By Marcos Vinicius Madeira     #")
print("#         \033[1;33;40mhttps://wellyington.github.io/\033[0;37;40m               #")
print("#########################################################\n\n") """

def scraping(class_id) :
    file = pd.read_excel("SkuHairPro22.xlsx", sheet_name="truss")
    url = file['urls']
    
    for i in url:
        search = requests.get(i, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(search.content, 'html.parser')        
        id_sellers = soup.find_all('a', class_=f'{class_id}')            
            
        with open('reportSku.xls', 'a', newline='') as f:
           for id_seller in id_sellers:
                sellers = id_seller.get('data-sku')[3:-3]
                
                sku_beleza = re.compile('sku":"[0-9]*')
                check_sku = sku_beleza.findall(sellers)
                
                print(sellers)
                
                
                
               
                """ check_sku = dic['sku']
                print(check_sku) """

                
                
                #print(sku.findall(sellers))
               # print(sellers)
                f.write(str(sellers + '\n'))
scraping('btn btn-primary btn-block js-add-to-cart')            

        
        

            
                             


             


        
                
            

        








