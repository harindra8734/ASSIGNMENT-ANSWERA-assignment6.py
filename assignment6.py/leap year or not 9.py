#to chech the year is leap year
year=int(input("enter an year"))
if year%4==0 and year%100!=0 or year%400==0:
    print("is the leap year",year)
    
else:
    print("is not leap year",year)