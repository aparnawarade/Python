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
    mylist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist.append([name, score])

list_score=set()
for i in mylist:
    list_score.add(i[1])

second_lowest=sorted(list(list_score))[1]

namelist=set()
for i in mylist:
    if second_lowest==i[1]:
        namelist.add(i[0])

for i in sorted(namelist):
    print(i)   