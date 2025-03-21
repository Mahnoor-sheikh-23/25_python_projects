def main():
    first_number = int(input("Please enter an integer to be divided : "))
    second_number = int(input("Please enter an integer to be divided : "))

    quotient = first_number // second_number
    reminder = first_number % second_number

    print(f"The result of this division is {quotient} with a remainder of {reminder}")

if __name__ == '__main__':
    main()