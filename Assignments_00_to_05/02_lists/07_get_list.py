def main():
    lists=[]
    user = input("Please enter an element of the list or press enter to stop.")
    while user:
        lists.append(user)
        user = input("Please enter an element of the list or press enter to stop.")
    print("The list is here : ",lists)

if __name__ == "__main__":
    main()
