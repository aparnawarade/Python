list=[9,1,5,6,7,8,9]
print(list[::1])

list.append(10)
list.append(15)
print(list)
list[1]=2
print(list)
print(list[2:4])
list.append(9)
print(list)

list.extend([10,20])
print(list)
list.insert(0,1)
print(list)
list.remove(1)
print(list)
list.pop()
print(list)
list.sort()
print(list)

print(list[-1])#last element
print(list[-2])#2nd last element
list=list*2
list.sort()
print(list)
print(list.count(9))
del list[1:6]
print(list)

squares=[x*2 for x in list]
print(squares)


list =[0,1,2,3,4,5,6,7,8,9]
print(list[1:5])
print(list[1:9:2])
print(list[::2])
print(list[::])
print(list[-3:])
print(list[-5:-2])
print(list[::-1])