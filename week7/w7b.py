

path = "headphones_data_trendyol.xlsx"
import pandas as pd

df = pd.read_excel(path)

df['product_name'] = df['product_link'].apply(lambda value: str(value).split('/')[-1])
df['product_name'] = df['product_name'].apply(lambda value: str(value).split('-p-')[0])
df['product_name'] = df['product_name'].apply(lambda value: str(value).replace('-', ' '))
df['product_name'] = df['product_name'].apply(lambda value: " ".join([i.title() for i in str(value).split(' ')]))


from turkish.deasciifier import Deasciifier

def deasc( my_ascii_turkish_txt ):
    deasciifier = Deasciifier(my_ascii_turkish_txt)
    return deasciifier.convert_to_turkish()



df['product_name'] = df['product_name'].apply(lambda value: deasc(value) )







print(df['product_name'])
