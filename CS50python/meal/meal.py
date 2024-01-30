#Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00.
#Wouldn’t it be nice if you had a program that could tell you what to eat when?
def main():
    time=input("What time is it ?")
    mealTime=convert(time)
    if(7.0 <=mealTime <=8.0):
        print("breakfast time")
    elif(12.0 <=mealTime <=13.0):
        print("lunch time")
    elif(18.0 <=mealTime<=19.0):
         print("dinner time")

def convert(time):
    hours,minutes=time.split(":")
    x=float(minutes)/float(60)
    return(float(hours)+float(x))

if __name__ == "__main__":
    main()
