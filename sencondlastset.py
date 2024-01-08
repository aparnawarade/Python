if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist=sorted(list(set(arr)), reverse=True)
    print(mylist[1])
