s="The sky is blue"
#blue is sky the 
newlist=s.split(" ")
newlist.reverse()
str=" ".join(newlist)
print(str)


print(newlist)
str1=""
for i in newlist:
    str1=str1+i+" "
print(str1.rstrip())