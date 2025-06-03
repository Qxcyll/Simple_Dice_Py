import random
a = "y"
while a == "y":
    
    print("-----------------------------------------")
    print("               DICE ROLLER")
    print("-----------------------------------------")
    print("Welcome to the Dice Roller!")
    print("Rolling the Dice...")
    num = random.randint(1, 6)
    
    print()
    print(f"You Rolled: {num}!")
    
    # Check if the number is even or odd
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
    
    if (num == 1):
       
        print()
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("You rolled a one! So Bad!")
        print()

    if (num == 2): 

        print("[  0  ]")
        print("[     ]")
        print("[  0  ]")
        print()

    if (num == 3): 

        print("[  0  ]")
        print("[  0  ]")
        print("[  0  ]")
        print()

    if (num == 4): 

        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print()
   
    if (num == 5): 

        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print()

    if (num == 6): 

        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("You rolled a six! WOW!😎")
        print()

    a = input("Do you want to roll the dice again? (y/n): ")
    if a.lower() != "y":
            print("-----------------------------------------")
            print("Thank you for playing!")
            print("-----------------------------------------")
            break