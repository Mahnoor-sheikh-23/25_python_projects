def print_divisors(num):
    print("Here are the divisors of", num)
    for i in range(num):
        divider = i + 1
        if num % divider == 0:
            print(divider)

def main():
    user_input = int(input('Enter the number . '))
    print_divisors(user_input)

if __name__ == "__main__":
    main()
