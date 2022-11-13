'''def myfunction():
    print("Mahadi")
    print("Hasan")
    print("Mishuk")
myfunction()

hello()
def hello():
    print("mahadi")
 


def welcome():
    name=input()
    print("Welcome "+name)
welcome() 



def function(word):
    print(word +  "!")

function("mango")
function("apple")
function("orange")

print(2* 3) 

 
def sum(x,y):
    print(x+y)
    print(x-y)
sum(20,10) 


password = input()
repeat = input()

def validate(text1, text2):
	
	if text1==text2:
		print("Correct")
	else:
		print("Wrong")
		
validate(password,repeat) 


def function(variable):
    variable += 1
    print(variable)

function(10)
print(variable)
 



def max(x,y):
    if x>y:
        return x

    else:
        return y
    
 
print(max(10,20))

z=max(5,8)
print(z)'''



'''
s = input()

def hashtagGen(text):
	#your code goes here
	text1= text.replace(' ','')
	return text1
 
print('#'+ hashtagGen(s))

'''

'''def sum(word):
    print(word+"!")

sum("Mahadi")'''

'''
def multi(x,y):
    return x*y

result=multi(10,20)
print(result)'''



'''def add(x, y):
    return x + y

def do_twice(func, x, y):
    return func(func(x, y), func(x, y))

a = 5
b = 10

print(do_twice(add, a, b))'''

'''import random

for i in range(5):
    Value=random.randint(1, 6)
    print(Value)'''

import math
num = 10
print (math.sqrt(num))