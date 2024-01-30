#implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case.
# Assume that the user’s input will indeed be in camel case.

def main():
    str= input("CamelCase:")
    convert_python(str)


def convert(newstring,pos):
    newstring=newstring[ :pos]+"_"+newstring[pos:]
    return newstring

def findposition(str,c):
    return str.find(c)

def convert_python(str):
    for c in str:
        if(c.isupper()):
            pos=findposition(str,c)
            newstring=convert(str,pos)
            str=newstring
    print(str.tolower())
main()
