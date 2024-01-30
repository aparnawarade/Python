import csv
students=[]
       #student
#gffjhgkgfhk


with open("student.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"FName":row["FName"],"LName":row["LName"]})

for student in sorted(students,key=lambda student :student["FName"]):
    print(f"{student['FName']} has Last Name : {student['LName']}")
