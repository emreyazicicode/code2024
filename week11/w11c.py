
import pandas as pd


df = pd.read_csv("Telecom_customer churn.csv")
del df['churn']

df = df.select_dtypes(exclude = ['object'])
df = df.dropna()

for c in df:
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())

from sklearn.ensemble import IsolationForest

clf = IsolationForest(max_samples=100, contamination=0.002)
clf.fit(df)
y_pred_train = clf.predict(df)


df['ANOMALY'] = y_pred_train

y_pred_train = list(y_pred_train)

freq = {}
for i in set(y_pred_train):
    freq[ i ] = y_pred_train.count(i)



print(freq)


df.to_csv("w11c_anomaly.csv")


