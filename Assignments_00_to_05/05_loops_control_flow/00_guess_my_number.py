import random 
def main():
    random_num = random.randint(0,99)
    print('I am thinking of a number between 0 and 99... Enter a guess: ')
    user_guess = int(input(" Enter a guess 🔎: "))
    while user_guess > 0  :
        if user_guess > random_num:
            print("Your guess is too high ☝ ")
        elif user_guess < random_num:
            print("Your guess is too low 👇  ")
        else:
            print(f"Congrats! The number was: {random_num}  🎉 ")
            break
        user_guess = int(input("Enter a guess: "))  #

if __name__ == "__main__":
    main()
        
