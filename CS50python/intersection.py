print("Hello world")
a= [2, 2, 1, 3, 2],
b= [1, 100, 2, 2, 20, 99, 100]

dict_a={}
for i in a:
    print(i)
    if i in dict_a.items():
        dict_a[i] +=1
    else:
        dict_a[i]=1

dict_b={}
for i in b:
    if i in dict_b:
        dict_b[i] +=1
    else:
        dict_b[i]=1

intersection=[]
for num in dict_a:
    if num in dict_b:
        intersection.append(num * min(dict_a[num],dict_b[num]))

print(intersection)
