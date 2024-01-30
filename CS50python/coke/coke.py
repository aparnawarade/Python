"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
 implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due.
 Once the user has inputted at least 50 cents,
 output how many cents in change the user is owed.
 Assume that the user will only input integers,
   and ignore any integer that isn’t an accepted denomination.
"""
def main():
    amountDue=50
    print("Amount Due:", amountDue)
    while amountDue > 0:
        coin=int(input("insert Coin:" ))
        if(coin ==25 or coin==10 or coin==5):
            amountDue=amountDue-coin
            if(amountDue <=0):
                print("Amount Due:", 0)
            else:
                print("Amount Due:", amountDue)
        else:
            print("Amount Due:", amountDue)
    change_owed=abs(amountDue)
    if(change_owed>0):
        print("Change Owed:",change_owed)
    else:
        print("Change Owed:",0)
main()
