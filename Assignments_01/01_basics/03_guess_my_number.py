import random

def main():
    random_num = random.randint(0,99)
    print("I am thinking of a number between 1 and 99...")
    user_guess = int(input("Enter number.."))
    while user_guess != random_num:
        if user_guess < random_num:
            print("Your guess is too low")
        else:
            print("Your guess is too high")   
        user_guess = int(input("Enter number.."))

    print(f"Congrats! The number was: {random_num}")

if __name__ == "__main__":
    main()

        
    
