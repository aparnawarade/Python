for i in range(10,15):
    print(i,"Hello")

for i in range(10,20,2): #skip by 2 
    print(i)

add=0
for x in range(1,5):
    add +=x
print("Addition from 1 to 4 :",add)

msg=""
for i in range(1,5):
    msg +=str(i)
print("Mesaage after COncatination is :",msg)


for i in range(5):
    if i==3:
        break
    print(i , end=" ")

print()
for i in range(5):
    if i==3:
        continue
    print(i, end=" ")
    
print()

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

for row in matrix:
    for ele in row:
        print(ele,end=" ")
    print()

for i in range(len(matrix)):
    print(matrix[i])
