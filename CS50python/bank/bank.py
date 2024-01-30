def main():

    print("Greetings:" ,end=' ')
    greeting=input()
    greeting=greeting.strip().lower()
    result =greeting.startswith("hello")
    if(result==True) :
        print("$0")
    elif(greeting.startswith("h")) :
        print("$20")
    else:
        print("$100")

main()
