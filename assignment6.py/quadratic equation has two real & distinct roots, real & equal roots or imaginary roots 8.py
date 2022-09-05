#8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots



import math
a=int(input("enter a:(a!=0)"))
b=int(input("enter b"))
c=int(input("enter c"))

print("General From:a*x**2+b*x+c=0")
d=(b**2)-(4*a*c)

print(f"result for equation,a*x**2+b*x+c=0,are:\n")
if d>0:
    print("type root:two distinct real root")
    sol1=(-b-math.sqrt(d))/2*a
    sol2=(-b+math.sqrt(d))/2*a
    print(f"the solution are {sol1} and {sol2}")
    
elif d==0:
    print("type root:two distinct equal root")
    sol1=(-b-math.sqrt(d))/2*a
    sol2=(-b+math.sqrt(d))/2*a
    print(f"the solution are {sol1} and {sol2}")
    
elif d<0:
    print("type root:two distinct complex root")
    
'''
print("enter a,b and c in quadratic equation:")
a,b,c=int(input()),int(input()),int(input())
d=b**2-4*a*c
if d>0:
    print("real and distinct root")

elif d==0:
    print("real and equal root")
else:
    print("imaginary root")'''