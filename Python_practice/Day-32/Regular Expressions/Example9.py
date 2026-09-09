import re
# '^' checks if the strings startswith a specified character or not
m = re.match(r'^a','abc')
print(m)  # Match Object gets printed if matched
print(m.start())
# '$' checks if the strings startswith a specified character or not
n = re.search(r'a$','abcbcaa')
print(n)
print(n.start())