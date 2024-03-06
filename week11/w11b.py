import sys
import pandas as pd

df = pd.read_csv("Telecom_customer churn.csv")

TARGET = 'churn'

print(df.shape)

df = df.select_dtypes(exclude = ['object'])
df = df.dropna()


y = df[TARGET]
del df[TARGET]

print(df.shape)

from sklearn.decomposition import PCA
pca = PCA(n_components=1)


low_corr = []
for c in df:
    corr = df[c].corr(y)
    if abs(corr) < 0.03:
        print(c, corr)
        low_corr.append(c)



print(low_corr)


#* LDA is a dimension reduction technique but it is SUPERVISED, There is a TARGET !!
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
clf = LinearDiscriminantAnalysis()


clf.fit( df, y )
TAHMIN = clf.predict( df )

df['TAHMIN'] = TAHMIN
print("LDA ile tahmin edilen sonuc ve gercek Output arasindaki iliski", df['TAHMIN'].corr(y))
sys.exit(1)


pca.fit(df[ low_corr ])
results = pca.transform( df[low_corr] ) 
df[ 'PCA_LOW' ] = results[:,0]
df[ 'TARGET' ] = y
for c in low_corr:
    del df[c]

print(df['PCA_LOW'].corr(df['TARGET']))

print(df)

sys.exit(1)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(df)
results = pca.transform(  df) 

# NOTE: DO NOT FORGET: We use PCA to sequeze columns which may not be useful

#* How much the pca has explained the LINEAR variance in the data
#* How much it can explain / understand
#* STD =~ VAR
#* Variance = Farklilik, difference, degisim miktari
#* Variance = oz - self - data

print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.cumsum())

df.corr().to_csv("w11_corr.csv")

print(results)

# Get the first and second component as new features to our dataset
df['pca0'] = results[:,0]
df['pca1'] = results[:,1]

df.to_csv("w11b_pca.csv")

"""
pca0	pca1
44447.5227409501	-12068.8905983105

"""


row0 = df.iloc[0]

inversed = pca.inverse_transform([ row0['pca0'], row0['pca1']  ])
inversed = inversed


print("=========================")
print("row0")
del row0['pca0']
del row0['pca1']
print(row0.shape, row0)
print("=========================")
print("inversed")
print(inversed.shape, inversed)
print("=========================")

for i in range(78):
    print(row0.values[i], inversed[i])




"""
rev_Mean	mou_Mean	totmrc_Mean	da_Mean	ovrmou_Mean	ovrrev_Mean	vceovr_Mean	datovr_Mean	roam_Mean	change_mou	change_rev	drop_vce_Mean	drop_dat_Mean	blck_vce_Mean	blck_dat_Mean	unan_vce_Mean	unan_dat_Mean	plcd_vce_Mean	plcd_dat_Mean	recv_vce_Mean	recv_sms_Mean	comp_vce_Mean	comp_dat_Mean	custcare_Mean	ccrndmou_Mean	cc_mou_Mean	inonemin_Mean	threeway_Mean	mou_cvce_Mean	mou_cdat_Mean	mou_rvce_Mean	owylis_vce_Mean	mouowylisv_Mean	iwylis_vce_Mean	mouiwylisv_Mean	peak_vce_Mean	peak_dat_Mean	mou_peav_Mean	mou_pead_Mean	opk_vce_Mean	opk_dat_Mean	mou_opkv_Mean	mou_opkd_Mean	drop_blk_Mean	attempt_Mean	complete_Mean	callfwdv_Mean	callwait_Mean	churn	months	uniqsubs	actvsubs	totcalls	totmou	totrev	adjrev	adjmou	adjqty	avgrev	avgmou	avgqty	avg3mou	avg3qty	avg3rev	avg6mou	avg6qty	avg6rev	hnd_price	phones	models	truck	rv	lor	adults	income	numbcars	forgntvl	eqpdays	Customer_ID
23.9975	219.25	22.5	0.2475	0	0	0	0	0	-157.25	-18.9975	0.666666667	0	0.666666667	0	6.333333333	0	52.33333333	0	42.33333333	0	45	0	0	0	0	18	0	90.64333333	0	97.17666667	0	0	0	0	58	0	132.6	0	24	0	55.22	0	1.333333333	52.33333333	45	0	0.333333333	1	61	2	1	1652	4228	1504.62	1453.44	4085	1602	29.66	83.37	32.69	272	116	30	322	136	38	149.9899902	2	2	0	0	15	1	4	3	0	361	1000001




pca0	pca1
44447.5227409501	-12068.8905983105


"""



