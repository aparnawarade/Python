import re

try:
    email=input("What's your Email?").strip()
    if re.search(r"^[a-zA-Z0-9_.]+@[^@]+\.edu$",email):
        #
        print("Valid")
    else:
        print("Invalid")
except ValueError:
    pass
