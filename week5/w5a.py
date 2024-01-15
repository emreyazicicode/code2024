
import pandas as pd # There are many variations, speed -- volume

path = "w4_cc_small.csv"
df = pd.read_csv(path)

df2 = pd.read_html('w5.html')
#df3 = pd.read_sql_query("SELECT * FROM studets", con)

print(len(df2), type(df2))

print(df2[0])

print("columns", df2[0].columns)

df2[0].columns = ['Hours', 'AZN']

print(df2[0])

df2[0] = df2[0][1:] # Start from 1 go to end
print(df2[0])

# OPPOSITE OF READ ==> WRITE (TO_)
df2[0].to_csv("w5x.csv")
import pprint
pprint.pprint(df2[0].to_json())
print("*" * 80)
print("dict", df2[0].to_dict())
print( df2[0].to_html()  )
# print( df2[0].to_sql()  )
print("*" * 80)
print("*" * 80)
print(df)



#* df[ 'string' ] ==> select the column 
#* df[ ['string', 'string' ] ==> select the columns! (list of strings)

#* SELECT TARGET, NAME_CONTRACT_TYPE FROM .....
df3 = df[   ['TARGET', 'NAME_CONTRACT_TYPE']   ]
print( df3 )



#*  df[ bool - şart - koşul - kıyas ] ==> filter ROWS

a = df['NAME_CONTRACT_TYPE'] == 'Cash loans'

#! A LIST/SERIES OF BOOLEANS

print(a)
print(type(df['NAME_CONTRACT_TYPE']))



print( df[  df['NAME_CONTRACT_TYPE'] == 'Cash loans'  ] )
#* SELECT * FROM TABLE WHERE NAME_CONTRACT_TYPE = 'Cash loans'

# df =  df[  df['NAME_CONTRACT_TYPE'] == 'Cash loans'  ] # overwrite to existing dataframe


# .... inplace = True





