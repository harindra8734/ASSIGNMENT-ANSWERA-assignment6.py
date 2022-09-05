#12. Write a python script to accept one complex number from the user and display thegreater number between real part and imaginary part

x=complex(input("enter a complex number:"))

if x.real:
    print("real part")
else:
    print("imaginary part")
