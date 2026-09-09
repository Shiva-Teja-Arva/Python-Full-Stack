import re
p=input().strip()
m=re.match(p,"ababbcabb") # works like startswith() in strings
print(m)  # prints the match object
# it returns none type if there is no match in the string
if m!=None:
    print("Match Found")
    print(m.start(),' ',m.end(),' ',m.group())
else:
    print("No Match Found")