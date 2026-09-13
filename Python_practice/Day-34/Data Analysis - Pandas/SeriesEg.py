import pandas as pd
# creation of series data structure of 1-D
s=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
print(s)
print()
print(s['a']) # access by index
print()
print(s+5,'  ',s.mean()) # element wise arithmetic operation