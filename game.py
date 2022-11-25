import random

for x in range(1,6):4
    guess=int(input("Enter your guess number="))
    randomnumber=random.randint(1, 5)

    if guess==randomnumber:
         print("You have won")
    else:
        print("You have loss")
        print("Random number was",randomnumber)