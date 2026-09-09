# New way of writing the same example1
import re
m=re.finditer(r'\d',"123I am Shiva I am 20 years old")
for i in m:
    print(i.start(),' ',i.end(),' ',i.group())