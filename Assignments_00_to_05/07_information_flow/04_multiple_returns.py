def get_user_data():
    f_name = input("Enter your first name ! ")
    l_name = input("Enter your first name ! ")
    email = input("Enter your first name ! ")
    return f_name , l_name , email 

def main():
    data = get_user_data()
    print("User data:", data)

if __name__ == '__main__':
    main()