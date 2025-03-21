import random

sides_in_dies = 6

def main():
    dice1 = random.randint(1, sides_in_dies)
    dice2 = random.randint(1, sides_in_dies)

    total = dice1 + dice2

    print(f"Dice have , {sides_in_dies} sides each. ")
    print(f"First Dice {dice1}")
    print(f"Second Dice {dice2}")
    print(f"Total of two dice {total}")

if __name__ == '__main__':
    main()
