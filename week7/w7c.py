
#: Imports
import sys
import pandas as pd
#: 
df = pd.read_csv("w6_202010-divvy-tripdata_small.csv")

df['rideable_type_isnull'] = df['rideable_type'].isnull()

print( df[ ['rideable_type', 'rideable_type_isnull'] ] )

df = pd.read_csv("w5_application_data_small.csv")

col = 'NAME_EDUCATION_TYPE'


#= To transform a categoric variable into "sorted labels"
#* RANDOMLY ASSIGNED INDEXES
items = list(df[col].unique())
items = dict(zip( items, range(len(items)) ))
df[col + '_rai'] = df[col].map( items )

#* MANUALLY ASSIGNED
my_index = {
    'Higher education': 3, 
    'Secondary / secondary special': 1, 
    'Incomplete higher': 2, 
    'Lower secondary': 0, 
    'Academic degree': 4
}
df[col + '_mai'] = df[col].map( my_index )

#= To transform a categoric variable into "frequency"

df[col] = df[col].replace('Lower secondary', 'Secondary / secondary special')
df[col] = df[col].replace('Incomplete higher', 'Higher education')
ed_ty_di = df[col].value_counts(normalize=True).to_dict()
ed_ty_di = { k:1.0 - v for k,v in ed_ty_di.items() }
df[col + '_freq'] = df[col].map( ed_ty_di )

#= To transform a categoric variable into "dummy"
yeni_df = pd.get_dummies( df, columns=['OCCUPATION_TYPE'] )

#= To transform a categoric variable into "grouped dummy"
"""
Managers                 2161

Drivers                  1886
Security staff            628
Low-skill Laborers        212
Cleaning staff            470
Private service staff     303
Cooking staff             603
Waiters/barmen staff      135
Laborers                 5541
Secretaries               120

Sales staff              3223
Core staff               2746
High skill tech staff    1130
Medicine staff            884
Realty agents              66
HR staff                   53
IT staff                   41
Accountants              1040
"""

print("mode", df[col].mode())

#= To transform a categoric variable into "most or not"
df[col + '_most'] = df[col] == df[col].mode()[0]

#= To transform a categoric variable into "topN"
col = 'OCCUPATION_TYPE'
n = 5
topn = list(dict(df[col].value_counts().to_dict()).keys())[0:n]

df[col] = df[col].apply( lambda value: value if value in topn else 'Other')
df = pd.get_dummies( df, columns = [col])

#= To transform a categoric variable into "target - average"
col = 'NAME_FAMILY_STATUS'
target_family = df.groupby(by = [col]).agg( {'TARGET':'mean'} ).to_dict()['TARGET']
df[col] = df[col].map( target_family )

print( df[ [col, 'TARGET'] ] )
print(df[col].corr( df['TARGET'] ))

sys.exit(1)
freq = df[col].value_counts(normalize=True).to_dict()
topn = [f for f in freq.keys() if freq[f] > p]
df[col] = df[col].apply( lambda value: value if value in topn else 'Other')
df = pd.get_dummies( df, columns = [col])


#= To transform a categoric variable into "less than %.."
col = 'ORGANIZATION_TYPE'
p = 0.10
freq = df[col].value_counts(normalize=True).to_dict()
topn = [f for f in freq.keys() if freq[f] > p]
df[col] = df[col].apply( lambda value: value if value in topn else 'Other')
df = pd.get_dummies( df, columns = [col])


df.to_csv("w7_dummy.csv")


"""
select * ,	
	case when 'Accountant' THEN 1,
	     when 'Manager' THEN 2,
	     when 'Cooking' THEN 3,
	     when 'Lawyer' THEN 4
	end as label_encoded
	from table


dummy
SELECT
  UserID,
  SUM(IF(category = "Accountant", 1, 0)) AS Accountant,
  SUM(IF(category = "Manager", 1, 0)) AS Manager,
  SUM(IF(category = "Cooking", 1, 0)) AS Cooking
FROM
  YourTable
GROUP BY
  UserID
"""

