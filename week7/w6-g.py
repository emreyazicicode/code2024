
import sys
path = "w6_Telecom_customer churn.csv"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
df = pd.read_csv(path)


t1 = 'mou_Mean'
t2 = 'totcalls'


#df['t1'] = (df[t1] - df[t1].min()) / (df[t1].max() - df[t1].min())
#df['t2'] = (df[t2] - df[t2].min()) / (df[t2].max() - df[t2].min())


df['t1'] = (df[t1] - df[t1].mean()) / (df[t1].std())
df['t2'] = (df[t2] - df[t2].mean()) / (df[t2].std())

plt.scatter( df['t1'], df['t2'])
plt.show()