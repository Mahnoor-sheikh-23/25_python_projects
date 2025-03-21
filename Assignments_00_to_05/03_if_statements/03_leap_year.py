def main():
    user_year = int(input("Enter year to check weather it s a aleap year or not : "))
    if user_year % 4 == 0 :
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                print("It is a leap year !")
            else:  # (Not divisible by 400)
                print("That's not a leap year.")
        else:
            print("It is a leap year !")
    else:
        print("That's not a leap year.")

if __name__ == "__main__":
    main()