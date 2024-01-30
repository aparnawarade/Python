with open("name.txt") as file:
    for line in sorted(file):
        print(line.rstrip())

with open("CVSFile.txt") as file:
    for line in file:
        row=line.rstrip().split(",")
        print(f"{row[0]} is from {row[1]} city")
