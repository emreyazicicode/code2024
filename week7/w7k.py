






import requests
from bs4 import BeautifulSoup 
import pandas as pd
import time
import random
df = pd.DataFrame(columns = ['name', 'price'])

for i in range(1, 6):
    #: Wait
    time.sleep( random.randint(1, 3) ) # WAIT randomly, between 1 and 3 seconds (1,2,3)


    url = f'https://www.bakuelectronics.az/catalog/telefonlar-qadcetler/smartfonlar-mobil-telefonlar/?page={i}'
    r = requests.get(url) # bring me
    soup = BeautifulSoup(r.content, 'html.parser')  # parse
    for c in soup.find_all('div', {'class': 'catalog__col'}):
        title = c.find('a', {'class': 'product__title'})
        price = c.find('div', {'class': 'product__price--cur'})
        
        if price != None:
            print(title.text.strip(), price.text.strip())
            df.loc[ len(df) ] = [ title.text.strip(), price.text.strip()  ]



df.to_csv("w7k.csv")












"""
import requests 
from bs4 import BeautifulSoup 

url = 'https://www.trendyol.com/sr?wc=103716&sst=BEST_SELLER'

r = requests.get(url) # bring me
soup = BeautifulSoup(r.content, 'html.parser')  # parse

for c in soup.find_all('div', {'class': 'p-card-chldrn-cntnr card-border'}):
    name = c.find('span', {'class': 'prdct-desc-cntnr-name hasRatings'})
    price = c.find('div', {'class': 'prc-box-dscntd'})

    print(name.text, "==>", price.text)
"""
"""
import requests 
from bs4 import BeautifulSoup 

url = 'http://oxu.az/'

r = requests.get(url) # bring me
soup = BeautifulSoup(r.content, 'html.parser')  # parse

for c in soup.find_all('div', {'class': 'title'}):
    print(c.text)

#! watch
"""