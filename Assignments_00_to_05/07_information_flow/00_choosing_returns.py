adult_age = 18 
def check_age ():
    user_age = int(input("Enter Your Age : "))
    if user_age >= adult_age:
        return True
    return False

def main():
    checking = check_age()
    print(checking)

if __name__ == '__main__':
    main()

