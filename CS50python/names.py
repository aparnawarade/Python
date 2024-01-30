"""
name=input("What's the Name?")

file=open("name.txt","a")
file.write(f"{name}\n")"""


with open("CVSFile.txt","a") as file1:
    file1.write("Aparna,charlotte\n")
    file1.write("Ajay,Washington DC\n")
    file1.write("Roy,New Jercey\n")
    file1.write("Robby,Main\n")
