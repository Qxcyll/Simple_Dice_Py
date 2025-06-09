import random
import time
# Dice Roller Game
a = "y"
while a == "y":
    
    print("-----------------------------------------")
    print("               DICE ROLLER")
    print("-----------------------------------------")
    print("Welcome to the Dice Roller!")
    print("Rolling the Dice...")
    time.sleep(1)  # Pause for 1 seconds to simulate rolling the dice
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
        print("[  ●  ]")
        print("[     ]")
        print("You rolled a one! So Bad!")
        print()

    if (num == 2): 

        print("[●    ]")
        print("[     ]")
        print("[    ●]")
        print()

    if (num == 3): 

        print("[●    ]")
        print("[  ●  ]")
        print("[    ●]")
        print()

    if (num == 4): 

        print("[●   ●]")
        print("[     ]")
        print("[●   ●]")
        print()
   
    if (num == 5): 

        print("[●   ●]")
        print("[  ●  ]")
        print("[●   ●]")
        print()

    if (num == 6): 

        print("[●   ●]")
        print("[●   ●]")
        print("[●   ●]")
        print("You rolled a six! WOW!😎")
        print()

    a = input("Do you want to roll the dice again? (y/n): ")
    if a.lower() != "y":
            print("-----------------------------------------")
            print("Thank you for playing!")
            print("-----------------------------------------")
            break
