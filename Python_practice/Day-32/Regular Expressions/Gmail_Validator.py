import re
email = input("Enter your Gmail address: ")
pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
if re.fullmatch(pattern, email):
    print("Valid Gmail address")
else:
    print("Invalid Gmail address")