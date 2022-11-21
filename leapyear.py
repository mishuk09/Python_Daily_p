

year=int(input("Enter year that you want to calculate="))
if(year%4==0 and year%100==0):
    print("Year is leap year ")
else:
    print("Year is not leap year")