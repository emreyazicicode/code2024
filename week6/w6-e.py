

path = "w6_Telecom_customer churn.csv"
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(path)

"""
print(df)
print(df.dtypes.to_dict())

for g in df.groupby(by = ['dwllsize']):
    plt.hist(g[1]['mou_Mean'], alpha = 0.7)

plt.show()
"""


target = "totcalls"
import numpy as np
df = df[df[ target ] > 0]
df['n2'] = np.sqrt(df[ target ])
df['n3'] = np.log(df[ target ])
plt.hist(df[target], alpha = 0.5)
plt.show()
plt.cla()
plt.hist(df['n2'], alpha = 0.5)
plt.show()
plt.cla()
plt.hist(df['n3'], alpha = 0.5)
plt.show()

"""
categoric = list(df.select_dtypes( include=['object']).columns)
numeric = list(df.select_dtypes( exclude=['object']).columns)


for c in categoric:
    for n in numeric:
        for g in df.groupby(by = [c]):
            plt.hist(g[1][n], alpha = 0.7)
        plt.savefig(f"w6images/w6_image_{c}_{n}.png")
        plt.cla()

"""


"""
index = 0
for n1 in numeric:
    for n2 in numeric:
        if n1 > n2:
            plt.scatter( df[n1], df[n2] )
            index += 1
            plt.savefig(f"w6images/w6_image_{index}_{n1}_{n2}.png")
            plt.cla()
    
"""
