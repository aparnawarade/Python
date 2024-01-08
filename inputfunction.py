"""
typecasting is process of converting one datatype in another 
helps in avopid type error 
parse user input 
convert value to numeric values 
"""

#implicitTypecasting  : automatic 
int_value=5
float_value=5.0
#python automatically converts to float
result=int_value+float_value

#python automatically converts to float
a=3
complex_value=5+4j
print(a*complex_value)
print(result)

#EXplicit typecasting 
#int()
#float()
#str()



name=input("Enter your Name: ")
year_of_birth=input("Enter your year of Birth : ")
year_of_birth=int(year_of_birth)
age=2024-year_of_birth
print(name)
print(age)


num1=int(input("First Number :"))
num2=int(input("First Number :"))

addition=num1+num2
print(addition)

try:
    num=float(input("Enter NUmber :"))
    print(num)
except:
    print("Invalid Input")