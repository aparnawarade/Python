num=64
found=False
for i in range(2,num):
    if found:
        break
    for j in range(i+1,num):
        if i* j==num:
            print("The pair of Fdivisor :",i,j)
            found=True
            break