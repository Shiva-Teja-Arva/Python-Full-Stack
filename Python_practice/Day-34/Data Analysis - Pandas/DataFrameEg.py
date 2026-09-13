import pandas as pd
# Creation of 2D table using DataFrame
data={
    'name':['raju','harish','rajesh'],
    'age':[23,34,32],
    'marks':[90,78,96]
}
df=pd.DataFrame(data)
print(df)
print()
# get a single column
print(df['name'])
print()
# get multiple columns
print(df[['name','age']])
print()
# get first 2 rows
print(df.head(2))
# get last 2 rows
print()
print(df.tail(2))
print()
# accessing dataframe cells using loc and iloc functions
print(df.loc[0,'marks'])
print(df.loc[2,'marks'])
print()
print(df.iloc[0,2])
print(df.iloc[2,2])
df["grade"]=["A","B","A+"]
print(df)
print()
new_row={'name':'shiva','age':20,'marks':99,'grade':"O"}
df.loc[3]=new_row
print(df)
