'''print("Hello world")
# add two number
num = 10
num2 = 20

print(num+num2)
'''

# find the root

'''num = 4
root = 2

print( num ** root)
'''


# area of triangle
'''
height = 3
weight = 4

print("Area of triangle", 0.5*height*weight)
'''


# swap two value

'''a = 10
b = 20

temp = a
a = b
b = temp

print("A=", a)
print("B=", b)
'''


# Random number

'''
import random
print(random.randint(1, 10))
'''


# km to meter

# we know that 1 km =1000 meter

'''num = int(input("Enter km="))

print(num + "Kilomete", + 1000 * num)'''


# celcias to farenhite

'''celcial = 100
farenhite = (celcial*1.8)+32
print(farenhite)
'''


# positive and negative number

'''num = int(input("Enter number"))

if num > 0:
    print("Number is positive")
else:
    print("Number is negative")


    '''


# even odd

'''num = int(input("Enter number="))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
'''


# leap year

'''year = int(input("Enter year="))

if (year % 4 == 0) or (year & 400 == 0):
    print("Leap year")
else:
    print("Not leap year")'''


# LArgest number

'''a = 100
b = 20
c = 30

if (a > b and a > c):
    print("A is larger")
elif (b > a and b > c):
    print("B is larger")
else:
    print("C is larger")
'''

# multiplecation table

'''n = 10

for i in range(1, 11):
    print(n , "*" ,i,'=', n * i)'''


# prime number
 
num = 20

for i in range(2, num):

    if num % i == 0:
    
     print("Number is not prime")


'''
num = 29
flag = False
if num > 1:
    
    for i in range(2, num):
        if (num % i) == 0:
           
            flag = True
           
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")'''
