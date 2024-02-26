

f = "w5_application_data_small.csv"
import pandas as pd

df = pd.read_csv(f)

df = df.select_dtypes(exclude = ['object'])
del df['Unnamed: 0']
del df['SK_ID_CURR']
del df['FLAG_MOBIL']

for c in df:
    if df[c].nunique() < 2:
        print(c)
        del df[c]

df = df.dropna()

for c in df:
    if df[c].nunique() < 2:
        print(c)
        del df[c]


y = df['TARGET']
del df['TARGET']

for c in df:
    df[c] = (df[c] - df[c].min()) / ( df[c].max() - df[c].min() )

df.to_csv("w10check.csv")

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=0, n_init="auto")
kmeans.fit(df)

df['cluster_index' ] = kmeans.predict(df)
df = pd.get_dummies(df, columns = ['cluster_index'])
df['TARGET'] = y

for c in df:
    print(c, df[c].corr(df['TARGET']))


print(df)
