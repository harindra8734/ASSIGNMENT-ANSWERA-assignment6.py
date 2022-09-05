#4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.

a=int(input("enter a number"))
b=int(input("enter a number"))
if a>b:
    print("a is greater then b",a)

elif a<b:
    print("b is greater then a",b)

else:
    print("a is equal to b",a) 

'''

print("enter a two number")
a,b=int(input()),int(input())
print(a if a>b else b)'''