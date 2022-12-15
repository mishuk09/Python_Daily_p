
# print welcome message

print("Welcome To Our Restaurant,We are here to give you best service \n")

# displaying manue

print("Our special menue:\n")

print("1.Tea")
print("2.Cofe")
print("3.Sandwise")
print("4.Bargar")
print("5.Pizza")

ch = int(input("Enter your choose Item="))


if (ch == 1):
    print("Tea-----20inr \n")
    print("How many cup of tea you want?")

elif (ch == 2):
    print("Cofy-----40inr \n")
    print("How many cup of Cofe you want?")

elif (ch == 3):
    print("Sandwise-----100inr \n")
    print("How many Sandwise you want?")

elif (ch == 4):
    print("Bargar-----80inr \n")
    print("How many Bargar you want?")

elif (ch == 5):
    print("Pizza------250inr \n")
    print("How many Pizza you want?")


# Quantity of product

quantity = int(input("Enter Quantity & see tha total price="))


if (ch == 1):
    print(quantity, " Cup Tea=", + 20 * quantity, "INR \n")
elif (ch == 2):
    print(quantity, "Cofy=", + 40 * quantity, "INR \n")
elif (ch == 3):
    print(quantity, "Sandwise=", + 100 * quantity, "INR \n")
elif (ch == 4):
    print(quantity, "Bargar=", + 80 * quantity, "INR \n")
elif (ch == 5):
    print(quantity, "Pizza=", + 250 * quantity, "INR \n")


# Show billing message

if (ch == 1):
    print("You select", + quantity,
          "Cup of tea and you have to pay", + 20 * quantity, "INR \n")

elif (ch == 2):
    print("You select", + quantity,
          "Cup of cofee and you have to pay", + 40 * quantity, "INR \n")
elif (ch == 3):
    print("You select", + quantity,
          "  Sandwise and you have to pay", + 100 * quantity, "INR \n")
elif (ch == 4):
    print("You select", + quantity,
          " Bargar and you have to pay", + 80 * quantity, "INR \n")
elif (ch == 5):
    print("You select", + quantity,
          " Pizza and you have to pay", + 250 * quantity, "INR \n")


# payment option


print("Select your payment option")
print("1.Cash")
print("2.Online \n ")

ch2 = int(input("Enter your choose="))

if (ch2 == 1):
    print("Download Recipt \n ")
elif (ch2 == 2):
    print("Select Your option=")
    print("1.UPI")
    print("2.Bank card")

    ch3 = int(input("Enter your choose="))

    if (ch3 == 1):
        print("UPI Add: 7069078661@upiidbi \n")

print("Thank for choose Us")
