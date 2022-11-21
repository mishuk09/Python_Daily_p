'''calcial=30
farenhite=(calcial * 1.8)+32
print("farenhite",farenhite)'''

#farenhite to celcial

'''farenhit=10
celcial=(farenhit-32)/1.9
print(celcial)'''

num=100
temp=False
for i in range(2,num):
    if num%i==0:
        temp= True
        break

if temp:
    print("Number is prime")
else:
    print("Number is not prime")