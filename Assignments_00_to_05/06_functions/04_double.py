def double(num):
    multiply = num * 2
    return multiply

def main():
    number = int(input("Enter the number for double it .. "))
    result = double(number)
    print(f"The answer is : {result}")

if __name__ == "__main__":
    main()