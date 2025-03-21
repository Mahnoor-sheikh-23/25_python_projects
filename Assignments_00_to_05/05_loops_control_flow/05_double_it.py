def main():
    number = int(input("Enter a number: "))  
    double_num = number * 2  

    if double_num >= 100:  # Check if the first doubled number is already 100+
        print("The doubled number is already 100 or more.")
        return  # Exit the function

    while double_num < 100:  
        print(double_num)
        double_num *= 2  # Update double_num in each iteration

if __name__ == "__main__":
    main()
