mylist=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date=input("Date:").strip()
        if "/" in date:
            month,day,year=date.split("/")
            if month.isnumeric():
                if 1<=int(month)<=12 and 1<=int(day)<=31:
                    print(f"{year}-{int(month):02}-{int(day):02}")
                    break
            else:
                break
        elif "," in date:
            my_new_string = date.replace(",", "")
            month,day,year=my_new_string.split(" ")
            if month.title() in mylist and 1<=int(day)<=31:
                index_month=mylist.index(month.title())
                index_month=index_month+1
                print(f"{year}-{int(index_month):02}-{int(day):02}")
                break
    except valueError:
        pass


