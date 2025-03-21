def count_list(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1  
    return count  # Return the count

def get_list():
    even_list = []
    while True:
        user = input("Enter an integer or press enter to stop: ")  # Read as a string
        if user == "":  # Stop if empty string
            break
        even_list.append(int(user))  # Convert to integer after checking
    return even_list

def main():
    result = get_list()
    even_count = count_list(result)  # Store the returned value
    print(f"Total even numbers: {even_count}")  # Print the result

if __name__ == "__main__":
    main()
