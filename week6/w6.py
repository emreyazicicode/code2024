

#* FUNCTION DEFINITION EXISTS!!!
def f( x ):
    if x < 10: return 'very cold'
    if x < 15: return 'cold'
    if x < 20: return 'mid'
    if x < 30: return 'hot'
    return 'very hot'

def tax_hesapla( incomes, charges, personel ):
    return (incomes - charges - personel * 0.80) * 0.15


for x in range(35):
    #* INPUT EXISTS!!!
    #! OUTPUT UNKNOWN
    print("INPUT=", x, "OUTPUT=", f(x))


#* TAX - VERGI 
#*  (KAZANCLAR (TOTAL GAIN) - MASRAFLAR (CHARGES) - PERSONEL COSTS -...... ) * 0.15 - 0.....
    

print(tax_hesapla(100000, 30000, 10000))
print(tax_hesapla(200000, 50000, 20000))
print(tax_hesapla(150000, 30000, 20000))

"""
income  costs  persone   taxt
a       b      c
100000, 30000, 10000 ==> 9300           equation  esitlik denklem
200000, 50000, 20000 ==> 20100
150000, 30000, 20000 ==> 15600



3a + 2b + c = 15
a + 2b + c = 10
a - b + 2c = 5



3a + 2b + c = 15
1a + 2b + c = 10

2a + 0  + 0 = 5
a = 2.5


2.5 - b + 2c = 5
- b + 2c = 2.5
-b = 2.5 - 2c
b = 2c - 2.5


2.5 + 2(2c - 2.5) + c = 10

c = 1...00

"""


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("w4_cc_small.csv")
print(df.dtypes)

# Avg Monthly Long Distance Charges
# Total Refunds

def parse(value):
    if value == None: return 0
    s = str(value)
    if s == '': return 0
    if s == ' ': return 0
    return float(s)



"""
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

df = df.dropna()
df['TotalCharges'] = df['TotalCharges'].apply(parse)
print(df['TotalCharges'])
"""


for c in df.select_dtypes(exclude=['object']):
    print(c, df[c].mean(), df[c].std())



xs = df['AMT_INCOME_TOTAL'].values
ys = df['AMT_CREDIT'].values
#plt.scatter( xs, ys )
plt.hist(ys)

plt.show()


#* HIGH STANDARD DEVIATION
#* 1- veri cok daginik, veri tutarli olmayabilir [data is wide spread]
#* 2- veri ile ilgili cikarim yapamayabiliriz    [we cannot make a decision, generalization]
#* 3- veri de muhtemel olarak birden fazla grup  [there are some groups]
#* 4- verinin dogrulunu gosterebilir             [it may show how correct your data is]
#* 5- kalite kontrol icin kullanilabilir         [it may be used to check quality]
