
#: Imports
import sys
import pandas as pd
#: 







df = pd.read_csv("w5_application_data_small.csv")


for col in df.select_dtypes(include = ['object']).columns:
    target_family = df.groupby(by = [col]).agg( {'TARGET':'mean'} ).to_dict()['TARGET']
    df[col] = df[col].map( target_family )

    print(col, df[col].corr( df['TARGET'] ))
