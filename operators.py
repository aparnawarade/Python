"""
Addition +
substraction -
multiplication *
power **
division /
floore dividion //
modulo %
"""
a=9
b=4
print("Addition :",a+b)
print("Substraction :",a-b)
print("Multiplication :",a*b)
print("Division :",a/b)
print("Floor dividion :",a//b)
print("MOdulo :",a%b)
print("Power :",a**b)



"""
greater than x>y return boolean
less than x<y return boolean
equal to ==
not equal !=
greater than equal to x>=y
"""
print("-"*10)
a=10 
b=a
print(a)
print(b)

b=b+10
print("b after adding 10:",b)

b+=10
print("b after adding 10:",b)

b-=10
print("b after substracting 10:",b)
print("-"*10)



"""

x<=y
x is y x is same as y 
x is not y 
"""
a=13
b=20
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print("-"*10)
"""
logial 

x and y  "both should be true"
x or y   "one should be true"
logical not  not x "negation "

"""

x= [1,2,3]
y = [1,2,3]
z = 3
print(x is y)  #pointing to same part of memory
print(id(x))#memory
print(id(y))
print(x==y) #are equal in value 