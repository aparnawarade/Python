
list=[10, 20, 50, 30, 40, 80, 60]

print("Get the loop in backwards")
for i in range(len(list) -1, -1,-1):
  print(list[i])


list1=[]
    
i= len(list)-1
while i>=0:
  list1.append(list[i])
  i=i-1
print(list1)

list1.clear()

for i in reversed(list):
  list1.append(i)
print(list1)

num=list.reverse()
print(num)


