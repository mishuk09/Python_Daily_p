'''
#print welcome message

print("Welcome To Our Restaurant,We are here to give you best service")

#displaying manue

print("Our special menue:")

print("1.Tea")
print("2.Cofe")
print("3.Sandwise")
print("4.Bargar")
print("5.Pizza")

ch=int(input("Enter your choose="))

if (ch==1):
    print("Tea-----20inr")
elif(ch==2):
    print("Cofy-----40inr")
elif(ch==3):
    print("Sandwise-----100inr")
elif(ch==4):
    print("Bargar-----80inr")
elif(ch==5):
    print("Pizza------250inr")


#Quality of product

Quality=int(input("Enter quality of product="))


if (ch==1):
    print( "Tea=", + 20 * Quality)
elif(ch==2):
    print("Cofy=",+ 40 * Quality)
elif(ch==3):
    print("Sandwise=",+ 100 * Quality)
elif(ch==4):
    print("Bargar=",+ 80 * Quality)
elif(ch==5):
    print("Pizza=",+ 250 * Quality)
 '''


num = int(input("Enter="))

for i in range(num):
    print(i)
