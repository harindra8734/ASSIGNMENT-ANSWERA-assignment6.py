#10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same.


print("enter a three number")
a,b,c=int(input()),int(input()),int(input())
if a>b:
    print("a is greater then b")
    if a>c:
        print("a is greater then c")
    else:
        print("c is greater then a")
if b>c:
    print("b is greater then c")
else:
    print("c is greater then b")

#print((a if a>c else c)if a>b else (b if b>c else c))