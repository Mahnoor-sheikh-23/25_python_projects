def print_multiple(message, repeats):
    return message * repeats

def main():
    input1 = input("Enter a message .")
    input2 = int(input("Enter num of repetation  ."))
    result = print_multiple(input1 , input2)
    print(result )

if __name__ == "__main__":
    main()
    