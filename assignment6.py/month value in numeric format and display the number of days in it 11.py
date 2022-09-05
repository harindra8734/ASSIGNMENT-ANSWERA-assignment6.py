#11. Write a python script to take the month value in numeric format and display the number of days in it.


month=int(input("enter a month number"))
if (1,3,5,7,8,10,12):
    print("31 days")

elif month in(4,6,9,11):
    print("30 days")

else:
    print("28 or 29 days")        