affirmation = "I believe in myself and my abilities."

def main():
    print(f"Please type the following affirmation: {affirmation}")

    while True:
        user_input = input()  # Taking user input
        if user_input == affirmation:  # Checking if input matches the affirmation
            print("That's right! :)")
            break  # Exit the loop if correct
        else:
            print("Hmmm, that was not the affirmation.")
            print(f"Please type the following affirmation: {affirmation}")

if __name__ == "__main__":
    main()

