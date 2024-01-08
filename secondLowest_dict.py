"""
iven the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example

The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
"""
if __name__ == '__main__':
    mydict={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mydict[name]=score

#get 2nd lowest score 
secondlowest=sorted(set(mydict.values()))[1]

#get all the emailmnets with 2nd lowest score and sort them  
myset=set()
for key,value in mydict.items():
    if value==secondlowest:
        myset.add(key)

for i in sorted(myset):
    print(i)