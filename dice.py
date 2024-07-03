import random

# Ask user for the type of they want!
while True:
    dice_type = (input("Pick a Dice type: \n1. D4\n2. D6\n3. D8\n4. D10\n5. D12\n6. D20\n7. D100\n\n"))

    if dice_type.lower() == 'stop':
        print("Good bye!")
        break
    # use switch cases introduced in Python 3.10
    try:
        dice_type = int(dice_type)
    except ValueError:
        print("Not an valid option, please enter a number between 1 to 7, or 'stop' in case you want to exit")
        continue

    match dice_type:
        case 1:
            number = random.randint(1, 4)
            print(f"You rolled... {number}")
        case 2:
            number = random.randint(1, 6)
            print(f"You rolled... {number}")
        case 3:
            number = random.randint(1, 8)
            print(f"You rolled... {number}")
        case 4:
            number = random.randint(1, 10)
            print(f"You rolled... {number}")
        case 5:
            number = random.randint(1, 12)
            print(f"You rolled... {number}")
        case 6:
            number = random.randint(1, 20)
            print(f"You rolled... {number}")
        case 7:
            number = random.randint(1, 100)
            print(f"You rolled... {number}")
        case _:
            print("Not a valid option, please enter a valid number between 1 and 7, if you want exit tipe 'stop'.")
      