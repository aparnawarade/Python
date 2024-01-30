"""In a file called pizza.py, implement a program that expects exactly
 one command-line argument, the name (or path) of a CSV file
 in Pinocchio’s format, and outputs a table formatted as ASCII art
 using tabulate, a package on PyPI at pypi.org/project/tabulate.
   Format the table using the library’s grid format.
     If the user does not specify exactly one command-line argument,
     or if the specified file’s name does not end in .csv,
     or if the specified file does not exist, the program should
     instead exit via sys.exit.
"""

import csv
from tabulate import tabulate
import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        fileName,ext=sys.argv[1].split(".")
        if ext =="csv":
                tabulate_file_regular(sys.argv[1])
        else:
            sys.exit("Not a CSV file")

def tabulate_file_regular(filename):
    list_of_dict=[]
    try:
        with open(filename) as file:
            reader=csv.DictReader(file)
            for row in reader:
                list_of_dict.append(row)
            print(tabulate(list_of_dict, headers='keys', tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

main()


