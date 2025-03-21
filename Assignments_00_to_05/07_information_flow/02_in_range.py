def in_range(n, low, high):
    """ Returns True if n is between low and high, inclusive. """
    return low <= n <= high  # Simplified condition

def main():
    parameter1 = int(input("Enter the first number: "))
    parameter2 = int(input("Enter the second number: "))
    parameter3 = int(input("Enter the third number: "))
    
    result = in_range(parameter1, parameter2, parameter3)
    print(result)

if __name__ == '__main__':
    main()
