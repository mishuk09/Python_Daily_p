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

'''num = 20

for i in range(2, num):

    if num % i == 0:
    
     print("Number is not prime")
'''

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


# prime number

'''num = 20
count = 0

for i in range(2, num):
    if (num % i == 0):
        count++
        break

if count == 0:
    print("Prime")
else:
    print("None Prime")

'''


# print all prime number
# Python program to display all the prime numbers within an interval

'''
for num in range(1, 100):

    if num>1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
'''


# factorial number

'''num = 5
fact = 1

for i in range(1, num+1):
    fact = fact*i
print(fact)
'''


# pattern

'''n=6
for i in range(n):
    print(i *  'B')
'''


'''str = "MAHADI HASAN MISHUK"
str2 = "HASAN"
print(str.split())'''

'''str = "MAHADI HASAN MISHUK"
str2 = "HASAN"
print(str.join(str2))
'''


'''srt = "MAHADI HASAN MISHUK"
print(str.lower())'''


'''string = "hasan"

print(string.capitalize())
'''

'''str = "MAHADI"

a = str.replace("i","")
print(a)
'''

'''name = "Mahadi"

for i in name:
    print(i)
'''


# LIST


'''num = [1, 2, 3, 4, 5, 6, 7, 8]
num2 = num.copy()
print(num2)
'''

'''num = [1, 2, 3, 4, 5, 6, 7, 8]

print(num.count(4))'''

'''name=["MAHADI","HASNA","MISHUK"]
a=name.index("HASAN")
print(a)'''


# reverse number

'''num = [1, 2, 3, 4, 5, 6]
num.reverse()
print(num)


name = ["MAHADI", "MISHUK"]
name.insert(1, "HASAN")
print(name)
'''


# tuple


'''
name=(1,2,3,4,5)
print(Reverse(name))

'''

'''num = [1, 2, 3, 4, 5, 6, 7, 8]
sum = sum(num)
print(sum)
'''


'''num=[1,2,3,4,5,6,7]
result=1
for i in num:
    result=result*i
print(result)'''
'''


num=[1,2,5,2,4,7,3,4]
num.sort()
print(num)
print("The largest number =",num[-1])'''

'''
tuple = (1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1)
print(tuple.count(5))
print(tuple.index(7))
'''


# python recurssion
'''
def name(n):
    print(n)


name(46)
'''


# maximum number by function


'''def func(a, b, c):
    if (a > b and a > c):
        print("A i max")
    elif (b > a and b > c):
        print("B is max")
    else:
        print("C is max")


func(100, 20, 30)'''
