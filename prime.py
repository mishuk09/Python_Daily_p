num=int(input("Enter number="))

count=False
for i in range(2,num-1):
    if (num%i)== 0:
       count=True
       break 
if (count):
    print("Number is prime")
else:
    print("Number is not ")     
    