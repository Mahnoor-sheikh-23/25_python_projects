def find_averages(one,two):
    sum = one + two
    result = sum / 2 
    return result

def main():
    one = int(input("Enter the first number for find average . "))
    two = int(input("Enter the second number for find average . "))
    result = find_averages(one, two)
    print(f"Here is the average of {one} and {two} = {result}")

if __name__ == "__main__":
    main()