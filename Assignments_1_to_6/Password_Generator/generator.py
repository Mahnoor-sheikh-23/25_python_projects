import random 

# Define the character set for passwords
CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()1234567890"

print("Welcome to the Password Generator!")

# Get user input with basic validation
try:
    number = int(input("Amount of passwords to generate: "))
    length = int(input("Enter the length of the password: "))
    
    if number <= 0 or length <= 0:
        print("Please enter positive numbers!")
    else:
        print("\nHere are your passwords:")
        # Generate passwords using list comprehension and join
        passwords = [''.join(random.choice(CHARS) for _ in range(length)) for _ in range(number)]
        
        # Print each password
        for password in passwords:
            print(password)

except ValueError:
    print("Please enter valid numbers!")
