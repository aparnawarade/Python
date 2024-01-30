import sys
def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        fileName,ext=sys.argv[1].split(".")
        if ext =="py":
            count_lines(sys.argv[1])
        else:
            sys.exit("Not a Python file")


def count_lines(filename):
    try:
        with open(filename) as file:
            i=0
            for line in file:
                line=line.strip()
                if (not line.startswith("#")) and len(line.strip()) > 0 :
                    i=i+1
    except FileNotFoundError:
        sys.exit("File does not exist")
    else: print(i)


if __name__=="__main__":
    main()
