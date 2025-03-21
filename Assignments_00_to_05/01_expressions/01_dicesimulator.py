import random 
num_of_sides = 6
def roll_dice():
    """Simulate rolling two dice, three times. Prints the results
    of each die roll. This program is used to show how variable scope works."""
    dice1 = random.randint(1 , num_of_sides)
    dice2 = random.randint(1 , num_of_sides)
    total = dice1 + dice2
    print("The total of two dice are : ",total)

def main():
    roll_dice()
    roll_dice()
    roll_dice()
    

    

if __name__ == '__main__':
    main()