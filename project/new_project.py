

# welcome message

print(("Welcome to our resturant"))

# mamue

print("1.Non-Veg")
print("2.Veg")

ch1 = int(input("Enter your choose="))

if (ch1 == 1):
    print("Non-Veg Item\n")
    print("1.Chiken")
    print("2.Mutton")
    print("3.Chiken fry")
    print("4.Mutton masala")

elif (ch1 == 2):
    print("Veg")
    print("1.Potato curry")
    print("2.Been curry")
    print("3.Mixed Veg")
    print("4.Ponir")




ch2 = int(input("Enter your choose="))

if (ch2 == 1):
    print("Chiken------100inr")
elif (ch2 == 2):
    print("Mutton------130inr")
elif (ch2 == 3):
    print("Cicken fry------80inr")
elif (ch2 == 4):
    print("Mutton masala------120inr")


quantity = int(input("Enter your quantity="))

if (ch2 == 1):
    print("You select", + quantity, "Cicken=", + 100 * quantity)
elif (ch2 == 2):
    print("You select", + quantity, "Mutton=", + 130 * quantity)
elif (ch2 == 3):
    print("You select", + quantity, "Cicken Fry=", + 80 * quantity)
elif (ch2 == 4):
    print("You select", + quantity, "Mutton Masala=", + 120 * quantity)
