"""
In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs,
as a percentage rounded to the nearest integer, how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0,
instead prompt the user again. (It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

def main():
    print(getFuelCondition("Fraction:"))

def getFuelCondition(prompt):
    while True:
        try:
            fraction=input(prompt)
            x,y=fraction.split("/")
            x=int(x)
            y=int(y)
            if x > y:
                continue
            else:
                return get_Fuel_percent(round(x*100/y))
        except (ValueError,ZeroDivisionError):
            pass

def get_Fuel_percent(value):
    if value <= 1:
        return "E"
    elif value >=99:
        return "F"
    else:
        return str(value)+"%"

main()
