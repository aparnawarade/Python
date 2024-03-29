"""In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase. Structure your program per the below,
wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str.
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""
def main():
    plate=input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
    characters=[".","+", " ","*","?", "^", "$", "(", ")", "[", "]", "{", "}", "|"]
    length=len(s)
    if not islength(s,length): #vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
        return False
    elif not Check_allAplha(s[:2]):  #All vanity plates must start with at least two letters.
        return False
    elif check_special(s,characters):
        return False
    elif check_Zero(s):
        return False
    elif Check_allAplha(s):
        return True
    elif not check_Zero(s) and s[-1].isnumeric():
        return True

def check_special(s,characters):
    for i in s:
        if i in characters:
            return False
def check_Zero(s):
    for i in s :
        if(i.isnumeric()):
            if(i=="0"):
                return True
            else:
                return False

def islength(s,length):
    if(2<=length<=6):
        return True

def Check_allAplha(s):
    return s.isalpha()

main()
