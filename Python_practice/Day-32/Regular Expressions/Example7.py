import re
pattern = "phone no:+44-8989-8984-0985"
m=re.sub(r'\d',"@",pattern)
print(m)
n=re.subn(r'\d',"@",pattern)
print(n)