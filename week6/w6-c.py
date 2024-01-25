
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_excel("w6_Online Retail.xlsx")
df = pd.read_csv("w6_Online Retail.csv")

#: Remove the items where the quantity is less than 1
df = df[ df['Quantity'] > 0 ]
print(df)



# series = df['Quantity'] pd.Series

def findOutliers( series ) -> dict:
    output = {}

    output['mean'] = series.mean()
    output['std'] = series.std()
    output['q3'] = series.quantile(0.75) # q0.75
    output['q1'] = series.quantile(0.25) # q0.25

    output['upper'] = output['mean'] + 3 * output['std']
    output['lower'] = output['mean'] - 3 * output['std']

    output['iqr'] = output['q3'] - output['q1']
    output['upper2'] = output['q3'] + 1.5 * output['iqr']
    output['lower2'] = output['q1'] - 1.5 * output['iqr']

    for o in output:
        output[o] = round( output[o], 2 )

    return output

"""
TARGET = 'UnitPrice'
info = findOutliers( df[TARGET] )
print(info)
df = df[ df[TARGET] < info['upper2'] ]
df = df[ df[TARGET] > info['lower2'] ]
plt.hist( df[TARGET] )
"""



TARGET = 'Quantity'
info = findOutliers( df[TARGET] )
df = df[ df[TARGET] < info['upper2'] ]
print("info", info)

data = []
for g in df.groupby(by = ['InvoiceNo']):
    # g[0] ==> 536365
    data.append(g[1]['Quantity'].sum())

data = pd.Series(data)
data_info = findOutliers( data )
print(data_info)

data = data[ data < data_info['upper2'] ]

df['QuantityLevel'] = df['Quantity'] > 12


plt.hist(data)


plt.show()