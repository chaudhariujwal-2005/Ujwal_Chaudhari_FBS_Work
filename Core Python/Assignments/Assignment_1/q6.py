# write a Program to Find the Roots of a Quadratic Equation
import math

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))

d=b**2-4*a*c

x1=(-b+math.sqrt(d))/(2*a)
x2=(-b-math.sqrt(d))/(2*a)

print("x1=",x1)
print("x2=",x2)



