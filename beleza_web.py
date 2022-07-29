import json
import requests
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urljoin
import pandas as pd
from datetime import datetime
import os


print("###############################################################")
print("# Beleza na Web Scraper - Dev. By Marcos Vinicius Madeira     #")
print("#         \033[1;33;40mhttps://wellyington.github.io/\033[0;37;40m               #")
print("#########################################################\n\n") 

try:

    from bs4 import BeautifulSoup   

except:
    upgrade_pip = lambda: os.system('pip3 install --upgrade pip')
    install_bs4 = lambda: os.system('pip3 install bs4')
    install_pandas = lambda: os.system('pip3 install pandas')
    install_requests = lambda: os.system('pip3 install requests')
    install_openpyxl = lambda: os.system('pip3 install openpyxl')
    install_time = lambda: os.system('pip3 install time')
    install_json = lambda: os.system('pip3 install json')
    install_datetime = lambda: os.system('pip3 install datetime')
    install_os = lambda: os.system('pip3 install os')

    print("Upgrading Pip")
    print("----------------------------------------------------------")
    upgrade_pip()
    print("Downloading Bs4 Library an BeautifulSoup class ")
    print("----------------------------------------------------------")
    install_bs4()
    print("Instalation Pandas Library")
    print("----------------------------------------------------------")
    install_pandas()
    print("Instalation Requests Library")
    install_requests()
    print("Instalation Openpyxl Library")
    install_openpyxl()
    print("Instalation Time Library")
    install_time()
    print("Instalation Json Library")
    install_json()
    print("Instalation Datetime Library")
    install_datetime()
    print("Instalation OS Library")
    install_os()
    print("----------------------------------------------------------")
    print("\033[1;33;40mInstalation Complete\033[0;37;40m")



def scraping(class_id) :
    file = pd.read_excel("SkuHairPro22.xlsx", sheet_name="truss")
    url = file['urls']
    sellers_df_list = []
    hairpro_df_list = []
    columns = [
            "sku",
            "brand",
            "category",
            "name",
            "price",
            "seller_name",
            
            
        ]          
        
    for i in url:
        search = requests.get(i, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(search.content, 'html.parser')        
        id_sellers = soup.find_all('a', class_=f'{class_id}')
                
        for id_seller in id_sellers:           
            sellers = id_seller.get('data-sku')            
            row = json.loads(sellers)[0]
            "\n"
            print(
                f"extract data from seller id: {row['seller']['id']} \
                    | name: {row['seller']['name']} ")
            sellers_row = [
                row['sku'],
                row['brand'],
                row['category'],
                row['name'],
                row['price'],                
                row['seller']['name'],                
                               
            ]            
            sellers_df_list.append(sellers_row)
            hairpro_df_list.append(sellers_row)
            
           
    sellers_df = pd.DataFrame(sellers_df_list, columns=columns)
    seller_name = sellers_df.groupby('seller_name')
    """ hairpro_filter = seller_name.get_group('HAIRPRO')
    print(hairpro_filter)

    hairpro_df = pd.DataFrame(hairpro_filter, columns=columns)
    hairpro_df.to_excel("hairpro_df.xlsx", index=False)  """
    

    sellers_df.to_excel('pricing_29_07_2022.xlsx', index=True)       
scraping('btn btn-primary btn-block js-add-to-cart')            

        
        

            
                             


             


        
                
            

        








