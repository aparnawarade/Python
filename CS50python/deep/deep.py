#
#In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
#outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.


value=input("the answer to the Great Question of Life, the Universe and Everything :")
value=value.lower().strip()                   
if value =="42" or value=="forty-two" or value=="forty two":
    print("Yes")
else:
    print("No")

