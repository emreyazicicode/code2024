import pandas as pd

df = pd.read_csv("w5_application_data_small.csv")

#* NOTE, if a variable is a flag, binary, then AVERAGE = MEAN give us how many percentage it has been written as "1"
print( len(df[ df['FLAG_EMP_PHONE'] == 1]) / len(df) )
print( df['FLAG_EMP_PHONE'].value_counts(normalize=True))
print( df['FLAG_EMP_PHONE'].mean() )
print(df['FLAG_EMAIL'].value_counts(normalize=True).to_dict()[1])



for f in ['FLAG_MOBIL','FLAG_EMP_PHONE','FLAG_WORK_PHONE','FLAG_CONT_MOBILE','FLAG_PHONE','FLAG_EMAIL']:
    print(f, df[f].mean())

df = df.drop(columns = ['FLAG_MOBIL', 'FLAG_CONT_MOBILE', 'Unnamed: 0'])

print(df['OCCUPATION_TYPE'].value_counts(normalize=True))

print(df['OCCUPATION_TYPE'].describe())

for g in df.groupby(by = ['REGION_RATING_CLIENT_W_CITY']):
    print(g[0])
    print(g[1]['AMT_INCOME_TOTAL'].mean())



