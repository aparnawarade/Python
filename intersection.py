"""
nums1=[1,2,2,1] 
num2=[2,2]

list=[]
for i in nums1:
    if i in num2 and i not in list:
        list.append(i)

print(list)"""

a = [2, 2, 1, 3, 2]
b = [1, 100, 2, 2, 20, 99, 100]
#0/p=[1,2,2]

list2=[]
if len(a)<len(b):
    for i in a:
        if i in b:
            list2.append(i)
else:
    for i in b:
        if i in a:
            list2.append(i)
print(list2)
