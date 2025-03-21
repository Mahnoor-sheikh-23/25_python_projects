import random
print("Welcome to the Number Guessing Game! \nYou have 5 attempts to guess the number.")

number = random.randrange(50, 100)
chances = 5
guess_counter = 0
while guess_counter < chances:
    guess_counter += 1
    guess = int(input("Enter your guess: "))
    if guess == number:
        print(f"Congratulations! You guessed the number in {guess_counter} attempts.")
        break
    elif guess_counter >= chances and guess != number:
        print(f"oops the number is  {number}. better Luck next time!")
    elif guess < number:
        print("Try a higher number")
    elif guess > number:
        print("Try a lower number")