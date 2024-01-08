if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist=sorted(list(arr),reverse=True)
    if n==1:
        print(list(arr)[0]) 
    else:
        first=mylist[0]
        for i in mylist:
            if i!=first:
                print(i)
                break;
        