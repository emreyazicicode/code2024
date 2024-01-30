
import sys
path = "w6_Telecom_customer churn.csv"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
df = pd.read_csv(path)


target = 'totmrc_Mean'

#* matplotlib --> 3x3 subplots 3cols 3rows
fig, (ax1, ax2, ax3) = plt.subplots(3, 3)

df['xlog'] = np.log(df[target] + 1)
df['xpow'] = np.power(df[target], 2)
df['xsqrt'] = np.sqrt(df[target])
df['xp1'] = np.power(df[target], 0.1)
df['xp3'] = np.power(df[target], 0.6)
df['xz'] = (df[target] - df[target].mean()) / df[target].std()
df['xnorm'] = (df[target] - df[target].min()) / (df[target].max() - df[target].min())
df['xmean'] = (df[target] / df[target].mean())

ax1[0].hist(df[target], color='red')
ax1[1].hist(df['xlog'])
ax1[2].hist(df['xpow'])

ax2[0].hist(df['xsqrt'])
ax2[1].hist(df['xp1'])
ax2[2].hist(df['xp3'])

ax3[0].hist(df['xz'])
ax3[1].hist(df['xnorm'])
ax3[2].hist(df['xmean'])

ax1[0].set_title(f'Original: |skew{round(df[target].skew(), 2)}')
ax1[1].set_title(f'Log: |skew{round(df["xlog"].skew(), 2)}')
ax1[2].set_title(f'Power: |skew{round(df["xpow"].skew(), 2)}')

ax2[0].set_title(f'Sqrt: |skew{round(df["xsqrt"].skew(), 2)}')
ax2[1].set_title(f'Pow01: |skew{round(df["xp1"].skew(), 2)}')
ax2[2].set_title(f'Pow06: |skew{round(df["xp3"].skew(), 2)}')

ax3[0].set_title(f'Zscore: |skew{round(df["xz"].skew(), 2)}')
ax3[1].set_title(f'Normalized: |skew{round(df["xnorm"].skew(), 2)}')
ax3[2].set_title(f'Mean: |skew{round(df["xmean"].skew(), 2)}')

#! BINS
#! PERCENTILE

plt.show()