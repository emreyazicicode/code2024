
import sys
import pandas as pd


path = "w5_Telco_customer_churn.csv"

df = pd.read_csv(path)

columnsToSelect = ['OnlineSecurity','OnlineBackup','DeviceProtection','TechSupport','StreamingTV','StreamingMovies']

#: Same operations below 
# REPLACES IN ALL COLUMNS
df.replace('No internet service', 'No', inplace=True)
df.replace('No phone service', 'No', inplace=True)

# df = df.replace('No internet service', 'No')


print( df[ columnsToSelect ] )

# SELECT_DTYPES SELECTS THE COLUMNS ONLY !!
print( df.select_dtypes( exclude = ['object'] ) ) # DO NOT RETURN ME THE ONES WHOSE TYPE IS OBJECT
print( df.select_dtypes( include = ['object'] ) ) # RETURN ME THE ONES WHOSE TYPE IS OBJECT



df[ df['SeniorCitizen'] == 1 ][ 'MultipleLines' ]
# SELECT MultipleLines FROM TABLE WHERE SeniorCitizen = 1


#   ROW FILTERING                   COLUMN FILTERING
df[ df['SeniorCitizen'] == 1 ][ ['MultipleLines', 'InternetService'] ]
#df[ ['MultipleLines', 'InternetService'] ][ df['SeniorCitizen'] == 1 ]

# SELECT MultipleLines, InternetService FROM TABLE WHERE SeniorCitizen = 1


# WE CAN CHANGE THE FILTERS
print( df[ ['MultipleLines', 'InternetService'] ][ df['SeniorCitizen'] == 1 ] )


# MULTIPLE ROW FILTERS
# SELECT * FROM ... WHERE a = 3 AND b = 4


df[ ['MultipleLines', 'InternetService'] ][ (df['SeniorCitizen'] == 1) & (df['gender'] == 'Male') ]
df[ ['MultipleLines', 'InternetService'] ][ (df['gender'] == 'Male') & (df['SeniorCitizen'] == 1) ]
# SELECT MultipleLines', 'InternetService FROM TABLE WHERE SeniorCitizen = 1 and gender = 'Male'


#  THIS IS ONLY THE COMMAND TO EFFECTIVELY DELETE A COLUMN FROM A DATAFRAME
# The below are same
#df = df.drop(columns = ['Offer'])  # DROP = DELETE
#df.drop(columns = ['Number of Referrals'], inplace=True)



print("BEFORE", df.columns)
#* 1 df = df.drop(columns = ['Offer']) #! KEEPS THE ORIGINAL
#* 2 df.drop(columns = ['Offer'], inplace=True) #! CHANGES THE ORIGINAL
print("AFTER", df.columns)




"""
not a good approach
df = ....
df1 = df.replace()
df2 = df1.drop......
df3 = df2. .....
"""


# TO DELETE A COLUMN
# df = df.drop(columns = ['gender'])
# df.drop(columns = ['gender'], inplace=True)






a = 3
a = 4 # ustune yazmak over write, REPLACE

a = a + 1  # 4 + 1

b = 35 # initialization
b = b + 1 # overwrite, update



# Return the list of columns
print( list(df.columns) )

# Return the list of "textual" columns only
print( list(df.select_dtypes(include = ['object']).columns) )

# Return the list of non"textual" columns only
print( list(df.select_dtypes(exclude = ['object']).columns) )


print( df.shape )

print(df)
# NaN = Not a number

#* ============================================================================
# Empty values are always problem
#! 1- We can delete the rows which has empty value
# --> if there only few number of rows (20, 50, ..) we remove the rows
print(df.shape)
# df = df.dropna()
print(df.shape)
# TODO, go to database admin ask why they are empty?
# TODO, goal is to think is there any way to fill this up?
# TODO, go to business department, ask why ?
#! 2- If the empties are mostly on a single column, then DELETE the column, not rows
df = df.drop(columns = ['PhoneService'])
#! 3- Fill the empty cells with "0"
df['tenure'] = df['tenure'].fillna( 0 )
#! 4- Fill the empty cells with mean (!)
mean = df['tenure'].mean()
df['tenure'] = df['tenure'].fillna( mean )
#* IF THE TYPE OF DATA IS NOT NUMERIC
#most = df['PhoneService'].mode()[0]
#df['PhoneService'] = df['PhoneService'].fillna( most )
#! 5- Fill with [some logic]
#df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['TotalCharges'] / df['tenure'])
#* Try to fill the empty area with most appropriate value
#! 6- Fill with a trained model
#* Will be practised later
#! 7- Split


dfA = df[ df['InternetService'].isnull() ]
dfA = dfA.drop( columns = ['InternetService'] )

dfB = df[ df['InternetService'].notnull() ]
print("===================================")
print(dfA)
print(dfB)
print("===================================")

sys.exit(1)
#* 
# ============================================================================


def karealma(n):
    return n * n


a = 4
b = karealma(a) # store, keep, write
print(a)
print("b", b)









