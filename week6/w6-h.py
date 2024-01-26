
import sys
path = "w6_Telecom_customer churn.csv"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
df = pd.read_csv(path)

t = 'totcalls'
print(df[t])

def outlier( series ) -> dict:
    out = {
        'max': series.max(),
        'min': series.min(),
        'mean': series.mean(),
        'std': series.std(),
        'q3': series.quantile(0.75),
        'q1': series.quantile(0.25),
    }

    out['iqr'] = out['q3'] - out['q1']
    return out


#* AGES
#* 10, 18, 17, 16, 15, 22, 29, 90, 45, 45, 67
#* clip (18, 60)
#* 18, 18, 18, 18, 18, 22, 29, 60, 45, 45, 60



info = outlier( df[t] )


upper = info['mean'] + info['std'] * 3
upper2 = info['q3'] + 1.5 * (info['iqr'])
df[ t ] = df[t].clip( 0, upper )

df[f'scaled_{t}'] = (df[t] - df[t].min()) / (df[t].max() - df[t].min())
print(df[f'scaled_{t}'].describe())


plt.hist(df[t])
plt.show()

sys.exit(1)



plt.hist(df[t])
plt.show()