MINIMUM_HEIGHT: int = 50  # arbitrary units :)

def main():
    while True:  # Keeps asking for input until the user decides to stop
        try:
            height = float(input("How tall are you? (Enter 0 to exit) ")) 
            if height == 0:
                print("Exiting program.")
                break  # Exit the loop

            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!") 
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Call the main function
main()
