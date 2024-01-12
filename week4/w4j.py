import sys
import pprint
import pandas as pd # alias, abbrevation


df = pd.read_csv( "w4_cc_small.csv" )
#* type(df) ==> DataFrame
# df ==> DATA FRAME, DATA SHEET
#* TABLE, MATRIX, DATA FRAME, SHEET = all same meaning

print(df)
print(type(df))

# LINE BY LINE
"""
SK_ID_CURR	TARGET	NAME_CONTRACT_TYPE	CODE_GENDER
100002	1	Cash loans	M
100003	0	Cash loans	F
100004	0	Revolving loans	M
100006	0	Cash loans	F
"""

#! ORDINARY, If we want to add more items, as records/lines/rows... the below format is more suitable
mydata = [
    {'SK_ID_CURR':100002, 'TARGET': 1, 'NAME_CONTRACT_TYPE': 'Cash loans', 'CODE_GENDER': 'M'},
    {'SK_ID_CURR':100003, 'TARGET': 0, 'NAME_CONTRACT_TYPE': 'Cash loans', 'CODE_GENDER': 'F'},
    {'SK_ID_CURR':100004, 'TARGET': 0, 'NAME_CONTRACT_TYPE': 'Revolving loans', 'CODE_GENDER': 'M'},
    {'SK_ID_CURR':100006, 'TARGET': 0, 'NAME_CONTRACT_TYPE': 'Cash loans', 'CODE_GENDER': 'F'},
]


#! However, in data science
mydata = {
    'SK_ID_CURR':         [100002, 100003, 100004, 100006],
    'TARGET'    :         [1, 0, 0, 0],
    'NAME_CONTRACT_TYPE': ['Cash loans', 'Cash loans', 'Revolving loans', 'Cash loans'],
    'CODE_GENDER':        ['M', 'F', 'M', 'F']
}

# Advantages
# all same, all simple/atomic
# easy to make operation, easy to make analysis

# DATA FRAME IS LIKE A DICTINARY OF ITEMS, WHERE KEYS ARE THE COLUMN NAMES, VALUES ARE THE LIST OF VALUE FOR THE COLUMN

for c in mydata:
    print(c)

for c in df:
    print(c)


print(mydata['TARGET'])
print(df['TARGET'])

# DATAFRAME = complex, special format!!


print("df.shape", df.shape)
print("df.rows", df.shape[0]) # records, rows, lines, objects...
print("df.columns", df.shape[1])  # columns, features, attributes, fields
print("len(df)", len(df))

print(df)
print("=" * 80)
# Return me only the first 20 rows (start from head)
print(df.head(20))

# Return me only the last 20 rows
print(df.tail(20))

# Return me only the rows with index between 50000 and 50021
print(df[50000:50021])  # START:END

# Return me only the rows after 100000
print(df[100000:]) # START: ---> until it finishes
# df.tail(44)

# HEAD 
print(df[:500])

print("df.columns", df.columns)  # PD.SERIES
# WHEN YOU PRINT SOMETHING IN PANDAS, DATAFRAME OR SERIES, IT ONLY PRINTS SOME PART OF THEM!!!
# BUT THE DATA EXISTS
print("df.columns", list(df.columns))

col_info = {}

for c in df.columns:

    col_info[ c ] = {
        'name': c,
        'type': str(df[c].dtype),
        'nunique': int(df[c].nunique()),
        'values': list(df[c].unique()[0:3]),
        'empty': (len(df) - sum(df[c].notnull())) / len(df)
    }

    # TOTAL = null + non_null
    # null = TOTAL - non_null


    """
    nu = df[c].nunique()
    if nu == 2:
        print(c, f"type={df[c].dtype}, FLAG")
    elif nu < 5:
        print(c, f"type={df[c].dtype}, unique values={df[c].unique()}")
    else:
        print(c, f"type={df[c].dtype}, #of unique values={nu}, some = {df[c].unique()[0:3]} cibi")
    """

#* DATAFRAME
#* df[ ] --> kolon ismi(str), SELECTS THE COLUMN!
    
# DATAFRAME == object ==> str
# DATAFRAME == float64 ==> float
# DATAFRAME == int64 ==> int

# nan ==> not a number

#! pprint.pprint(col_info)

#import json
#print( json.dumps(analysis) )



for c in col_info:
    print(c, col_info[c])




col_info_2 = []

for c in df.columns:

    # for the column c, we get the frequency of values for each, transform it into "faiz"
    # transform it into dictionary
    ratios = df[ c ].value_counts(normalize=True).to_dict()

    mean = None
    maxvalue = None
    minvalue = None

    if str(df[c].dtype) != 'object':  # int64, float64 ==> scalar, numeric
        #* IF THE COLUMN IS NOT A STRING COLUMN, THEN IT IS A NUMERIC COLUMN
        mean = df[c].mean() #* WE CAN CALCULATE THE MEAN - AVERAGE
        maxvalue = df[c].max() #* WE CALCULATE THE MAX of VARIABLE
        minvalue = df[c].min()

    col_info_2.append( {
        'name': c,
        'type': str(df[c].dtype),
        'nunique': int(df[c].nunique()),
        'values': list(df[c].unique()[0:3]),
        'empty': (len(df) - sum(df[c].notnull())) / len(df),
        'maxitem':   df[c].mode()[0],
        'maxratio':  ratios[ df[c].mode()[0]  ],
        'mean': mean,
        'maxvalue': maxvalue,
        'minvalue': minvalue
    })


print("*" * 80)




print(col_info_2)

#! LIST OF ITEMS, WHERE ITEMS ARE DICTIONARIES
"""
col_info_2 = [
    {'name': 'SK_ID_CURR', 'type': 'int64', 'nunique': 100044, 'values': [100002, 100003, 100004], 'empty': 0.0, 'maxitem': 100002, 'mean': 158031.6978929271}, 
    {'name': 'TARGET', 'type': 'int64', 'nunique': 2, 'values': [1, 0], 'empty': 0.0, 'maxitem': 0, 'mean': 0.08095438007276798}, 
    {'name': 'NAME_CONTRACT_TYPE', 'type': 'object', 'nunique': 2, 'values': ['Cash loans', 'Revolving loans'], 'empty': 0.0, 'maxitem': 'Cash loans', 'mean': None}, 
    {'name': 'CODE_GENDER', 'type': 'object', 'nunique': 3, 'values': ['M', 'F', 'XNA'], 'empty': 0.0, 'maxitem': 'F', 'mean': None}, 
    {'name': 'FLAG_OWN_CAR', 'type': 'object', 'nunique': 2, 'values': ['N', 'Y'], 'empty': 0.0, 'maxitem': 'N', 'mean': None}
    # ....
]
"""


print( pd.DataFrame( col_info_2 ) )

# READ_CSV ==> read
# TO_CSV ==> write
#* construct a dataframe with the following values [list of dictionary ==> col_info_2] and save it to a file
pd.DataFrame( col_info_2 ).to_csv("w4_analysis.csv")



# ACIKLA
print(df.describe())

df.describe().to_csv("w4_analysis2.csv")



# group by
#* SELECT gender, count(*) FROM members GROUP BY gender
print(df['CODE_GENDER'].value_counts() ) #* ITEMS COUNT
print(df['CODE_GENDER'].value_counts(normalize=True) ) #* FAIZ, RATIO
print(df['CODE_GENDER'].value_counts(normalize=True).to_dict() ) 



