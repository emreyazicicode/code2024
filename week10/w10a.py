#: Imports
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import sys
import pandas as pd

df = pd.read_csv("w10.csv")
for c in df:
    df[c] = (df[c] - df[c].min()) / ( df[c].max() - df[c].min())
print(df.mean())

#* Load the dataset
df = pd.read_csv("w10hotel.csv")
#* For now, we drop the rows which have empties
df = df.dropna()
#* For now, we drop the columns which are categoric
df = df.select_dtypes(exclude = ['object'])
# NOTE, in clustering, try not to use Dummy variables

#! NOTE, IN CLUSTERING, NORMALIZATION IS A MUST!
#* Normalize the dataset
for c in df:
    df[c] = (df[c] - df[c].min()) / (df[c].max() - df[c].min())

#* Find and delete items whose correlation are very close each other
for c1 in df:
    for c2 in df:
        if c1 > c2:
            cc = df[c1].corr(df[c2])
            if abs(cc) > 0.70:
                print(c1, c2, cc)

#* Delete the intercorrelated columns
del df['DaysSinceFirstStay']
del df['DaysSinceLastStay']
del df['PersonsNights']


#* Try for k (cluster count, NOTE: keep it less than 8)
print("==============================")
df = df.sample(n = 10000)
for ci in [2,3,4,5,6]:
    #* Fit the means
    kmeans = KMeans(n_clusters=ci, random_state=0, n_init="auto")
    kmeans.fit(df)
    #* Get the cluster indexes
    cluster_indexes = kmeans.predict(df)
    #* Calculate the silhoutte score
    silhouette_avg = silhouette_score(df, cluster_indexes)
    print(ci, silhouette_avg)

sys.exit(1)

#* Assign the indexes as new variable
df['cluster_index'] = cluster_indexes
df.to_csv("w10_indexes.csv")

# NOTE
#* If there are too many items in a cluster (%90), no need cluster
#* If there are very few items in a cluster (%1), no need cluster
#* If a feature is same or very similar for each cluster, ignore the feature

cols = list(df.columns)
cols.append('count')
centers = pd.DataFrame(columns = cols)

for g in df.groupby(by = ['cluster_index']):
    center = g[1].mean().to_dict()
    center = {q: round(center[q],3) for q in center}
    print("CLUSTER", g[0], "MEAN", center)
    values = list(center.values())
    values.append( len(df[ df['cluster_index'] == g[0]]) )
    centers.loc[len(centers)] = values

print(centers)
centers.to_csv("w10_centers.csv")


