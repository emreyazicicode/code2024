import sys
import pandas as pd

path = "w5_salesforcourse-4fe2kehu.csv"
df = pd.read_csv(path)


# ========================================
#* QUESTION 1
# ========================================
print(df)
print(df['Country'].value_counts())
countries = list(df['Country'].dropna().unique())
print(countries)

print('=====================')
dataframes = []
for c in countries:
    customers_from_country = df[ df['Country'] == c ]
    customers_from_country = customers_from_country.sample(n = 1000)
    dataframes.append( customers_from_country )
#* dataframes = [ df1, df2, df3, df4 ]
#* list of dataframe
merged = pd.concat( dataframes )
merged = merged.sample(frac = 1.0) # faiz 100 hepsini karistir

print(merged['Country'].value_counts())

print(merged[['Country', 'Month', 'Year', 'Cost']])

# ========================================
#* QUESTION 2
# ========================================

#* For the dataframe in question 1, find the "two" countries, 
#* where their average age is very close. For example, the average age of customer in Turkey is 45,
#* Usa is 48, Azerbajian is 38, England is 39. 
#* The closest two countries (which has closest ages) are Azerbaijan and England where 
#* the difference is only 1 


ages = {}

for g in df.groupby( by = ['Country'] ):
    ages[ g[0] ] = g[1]['Customer Age'].mean()

# combination
for a1 in ages:
    for a2 in ages:
        if a1 != a2:
            if a1 > a2:
                print(a1, a2, abs(ages[a1] - ages[a2]))

print("----------------")


country_diff = {}

for a1 in ages:
    for a2 in ages:
        if a1 > a2:

            country_diff[ a1 + "-" + a2 ] = abs(ages[a1] - ages[a2])

            print(a1, a2, abs(ages[a1] - ages[a2]))


print(country_diff)
#* Get the key of item, where the value is minimum (smallest)
print(min(country_diff, key=country_diff.get))

"""
[Germany France] 0.3598155614870464
[United Kingdom France] 0.3577318678600534
[United Kingdom Germany] 0.7175474293470998
[United States France] 2.2112851945380925
[United States Germany] 2.571100756025139
[United States United Kingdom] 1.853553326678039
"""

"""
a = 3 > 4
b = "France" < "Germany"
c = "Germany" < "UK"
#* F G .... U
#d = "France" - "Germany"
e = ages["France"] - ages["Germany"]
print(b, c)
"""

#! distance = | a - b | no direction
#!  |a-b| = |b-a|
sys.exit(1)
# ========================================
#* QUESTION 3
# ========================================

#* For the dataframe in question 1,
#* I want to get customers with Age greater than 30 and less than 20. 

# a 
da = df[ (df['Customer Age'] < 20) | (df['Customer Age'] > 30) ]

# b
d1 = df[ df['Customer Age'] < 20 ]
d2 = df[ df['Customer Age'] > 30 ]
da = pd.concat( [ d1, d2 ] )

# c
#* da = df.query("'Customer Age' < 20 OR 'Customer Age' > 30")



print(d2)


"""
Question 1- I have table as following  (3 columns of 10.000 rows) 

Name: str 

Gender: str 

Age: int 

Country: str  ( Azerbaijan, Turkiye, USA, England …. ) 



I want to get a (subset) sample of the dataframe. 
But, I want to get a subset where number of customers from each country are same 
(so the resulting table must have EQUAL size of each country) 

 

Write a code in python using pandas to achieve this 

 

Question 2- For the dataframe in question 1, find the "two" countries, where their average age is very close. For example, the average age of customer in Turkey is 45, Usa is 48, Azerbajian is 38, England is 39. 

 

The closest two countries (which has closest ages) are Azerbaijan and England where the difference is only 1 

 

Question 3- For the dataframe in question 1, I want to get customers with Age greater than 30 and less than 20. 


"""