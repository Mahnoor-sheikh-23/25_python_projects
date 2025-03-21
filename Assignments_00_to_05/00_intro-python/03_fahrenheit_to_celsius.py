def main():
    print("Temperature converted to Celsius")
    user_input = int(input("Enter the temperature in Fahrenheit ❔ "))
    degrees_celsius = (user_input - 32) * 5.0/9.0 
    print(f"Temperature =  {degrees_celsius}C")

if __name__ == "__main__":
    main()
