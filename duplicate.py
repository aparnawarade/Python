num=[1,2,3,1]
num1=[1,2,3,4]
def containsDuplicate(list):
    for i in range(len(list)):
        if list.count(list[i])>1:
            return True
    return False

def containsDuplicate2(num):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]==num[j]: 
                return True
    return False
def containsDuplicate3(num):
    num.sort()
    for i in range(0,len(num)-1):
        if num[i]==num[i+1]: 
                return True
    return False

print(containsDuplicate(num1))
print(containsDuplicate2(num))
print(containsDuplicate3(num1))
