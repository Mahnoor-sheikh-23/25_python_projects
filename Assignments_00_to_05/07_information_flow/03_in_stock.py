def num_in_stock(fruit):
    if fruit == "apple":
        return 2
    elif fruit == "litchi":
        return 4
    elif fruit == "cherry":
        return 10
    else:
        return 0

def main():
    fruit = input("Enter a fruit name to check it is in stock or not ? ")
    result = num_in_stock(fruit)
    if result == 0:
        print("It is not in stock!")
    else:
        print(f"This fruit is in stock! Here is how many: {result}")

if __name__ == '__main__':
    main()