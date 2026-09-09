import re
string1 = "ShivaTeja2510@gmail.com"
# print vowels from the string
m = re.findall(r'[aeiou]',string1)
print(m)  # matches all the vowels
n = re.findall(r'[^aeiou]',string1)
print(n)  # matches all the characters **except** vowels
o = re.findall(r'[0-9]',string1)
print(o)  # matches all the digits from 0-9
p = re.findall(r'[a-z]',string1)
print(p)  # matches all the lowercase letters
q = re.findall(r'[a-zA-Z0-9.]',string1)
print(q)  # matches all the lowercase, uppercase and digits including a dot(.)
