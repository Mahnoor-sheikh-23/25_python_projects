# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Loop until the value is 100 or greater
while curr_value < 100:
    curr_value *= 2  # Double the number
    print(curr_value, end=" ")  # Print the current value
