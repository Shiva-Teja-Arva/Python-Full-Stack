import re
pattern = re.compile(r'\d') # [0-9]
string="123 Hello I am Shiva I am 20 years old"
m=pattern.finditer(string) # to find all occurances
print(m)
for i in m:
    print(i)  # printing the matched object(callable)
print("="*100)
n=pattern.finditer(string)
# printing the matched starting index nums and ending(index+1) nums
for i in n:
    print(i.start(),' ',i.end(),' ',i.group())

