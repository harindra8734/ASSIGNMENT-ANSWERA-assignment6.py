#5. Write a python script to print two given words in dictionary order


print("enter two words")
a,b=input(),input()
print((b,a)if a>b else (a,b))