


import pandas as pd

df = pd.read_csv("w6_Online Retail.csv")
df = df.dropna()

KNOWN_COLORS = ['WHITE', 'BLACK']


color_names = {}

for color in KNOWN_COLORS:
    print("!", color)
    da = df[ df['Description'].str.contains(color) ]
    da = da['Description'].unique().tolist()

    for item in da:
        #* item = BLACK TEA,COFFEE,SUGAR JARS
        something = item.replace(color, '')
        #* something =  TEA,COFFEE,SUGAR JARS
        if len(something) > 0 and '+' not in something: # seems like an operator
            #* bring me the ones, which have a description like "something"
            dx = df[ df['Description'].str.contains( something ) ]
            #* bring me the ones, which are not SAME as given color
            dx = dx[ ~dx['Description'].str.contains( color ) ]
            #* If there is a data matching with "something"
            if len(dx) > 0:
                #* bring me a list of distinct items
                dx = dx['Description'].unique().tolist()
                dx = [i.split(' ')[0] for i in dx if ' ' in i and len(i.split(' ')) > 0]
                

                for i in dx:
                    if i not in color_names:
                        color_names[i] = 0
                    color_names[i] += 1
                

print(color_names)


MY_COLORS = ['Red','Orange','Yellow','Green','Blue','Indigo','Violet','Pink','Purple','Turquoise','Gold','Lime','Maroon','Navy','Coral','Teal','Brown','White','Black','Sky','Berry','Grey','Straw','Silver','Sapphire']
MY_COLORS = [i.upper() for i in MY_COLORS]
KNOWN_COLORS = ['WHITE', 'BLACK', 'PINK', 'GREEN', 'BLUE']

for k in KNOWN_COLORS:
    df[k] = df['Description'].str.contains(k)
    df[k] = df[k].astype(int)

print(df)


words = {}

for d in df['Description'].unique():
    for word in d.split(' '):
        if word not in words:
            words[word] = 0
        words[word] += 1


l = [1,2,3,4]
m = [i * 2 for i in l if i < 4]

words = {k:v for k,v in words.items() if v > 30}

print(words)





for c in KNOWN_COLORS:
    print( c, df[c].corr( df['UnitPrice']) )

for c in KNOWN_COLORS:
    print( c, len(df[ df[c] == True]))



def chatgpt( text: str ) -> str:

    pass


mytext = """
create a table of usages for the products below. the table must have the following columns: product name, mostly used by, where as the "mostly used by" column will contain, which gender - age group uses the product most
"""

most = list(dict(df['Description'].value_counts().to_dict()).keys())[0:100] 

for i in range(10):
    sub = most[i*10:(i+1)*10]
    sub = "\n".join(sub)
    print(mytext + sub)
    print("===============")



uniqueitems = list(df['Description'].unique())
uniqueitems = [len(i) for i in uniqueitems]


import matplotlib.pyplot as plt
plt.hist( uniqueitems )
plt.show()




xs = []
ys = []
df['len'] = df['Description'].str.len()
df['#words'] = df['Description'].apply(lambda value: len(value.split( ' ' )))
for l in range(3, 10):
    xs.append( l )
    ys.append( df[ df['#words'] == l ]['Quantity'].sum() ) # ['UnitPrice'].mean() )

plt.scatter(xs, ys)
plt.show()

