def main():
  #  print_column(3)
  #  print_row(3)
    print_square(3)
    print_square1(5)

def print_column(height):
    for i in range(height):
        print("*")

def print_row(width):
    print("*" * width)

def print_square(size):
    for i in range (size):
        print_row(size)

def print_square1(size):
    for i in range (size):
        for j in range(size):
            print("#",end="")  #for each row in square
        print()

main()
