'''
Variables and Data Types
its help to change database or data sheet data .its help to replace data

'''

name1 = " Mehedi "
name2 = "sheikh"
old1 = 23
old2 = 35
name3= "masum"
name4 = "moinul"

print           ("My friend name is " + name1)
print           (name1+" live in india last 1 month")
print           (name1+"   is " ,old1," years old")
print           (name1+" read in RK university Gujrat ")
print           ("His contact number is \"01740106176\" ")
print           (name1+"  father name is  " + name2)
print            (name2+ "  ",old2," years old")


print(name3+ 'is good boy')
print (name3+'read in class 3 ')
print(name3+'father  name is '+ name4)
print(name4+' is a farmer ')

'''
Basic numerical  operator 
its like variable data type


'''

a=10
b=5
c=20
d=15


print(a+b)
print(a-b)
print(b+c)
print(b-c)
print(a*b)
print(b%a)




#Gettibg user input




name1=input('Enter your name?')
name2=input('Enter your moobile numbar?')
name3= input('enter your age?')


print('Student informatio')
print('-----------------')
print("Name: "+name1)
print("Mobile:"+name2)
print("Age:"+name3)





#Type Casting





num1= int (input('Enter first number'))
num2= int (input( 'Enter second numbar'))
num3 = int (input(' Enter third numbar'))


sum= num1+num2+num3
minus= num1-num2-num3

print('result',sum)
print( 'minus',minus)


# Print area


base=float(input('Enter Base'))

height=float(input('Enter height'))

area=0.5 * base * height

print(area)


#print Radious



radious=float(input('Enter radious'))

area= 3.141 * radious* radious

print(area)



#Math store

from math import*

print(max(20,10))
print(min(30,20))
print(pow(2,3))
print(sqrt(25))
print(round(3.40))

print(floor(3.46))
print(ceil(3.78))




#Formating string and type function

Number="12"

print(type("Number"))

num1=10
num2=20

print(f'{num2}+{num1}={num1+num2}',end=" ")




# Relational operator and bulian

> বড়
< ছোট
<= সমান অথবা ছোট
>= সমান অথবা বড়
== সমান
!= সমান নয়
a=b   = b এর মান এ এঁর মধ্যে আছে
a==b এ আন্ড বি সমান

print(12>16)
print(12<16)
print(12>=16)
print(12<=16)
print(12==16)
print(12!=16)


print('mishuk'=="mishuk")



# if and else statement

mark=80

if mark>=33:
    print("pass")
    print('congratulations')

if mark<=33:
    print("fail")


if mark>=33:
    print('pass')
    print("congratulations")

else:
    print('fail')
    print('Do batter next')




# largest numbar

num1 = 20
num2 = 30
num3 = 60

if num1 > num2:
    print(num1)
else:
    print(num2)






# eveen odd number


num1=20

if num1%2==0:
    print('even')

else:
    print('odd')



#else and elif

mark=90

if mark>=80:
    print('a+')
elif  mark>=70:
    print('a')
elif mark>=60:
    print('a-')
elif mark>=50:
    print('b')

else:
    print('fail')


