def greet(name):
    return "hello" + " " +  name + "!"

def main():
    greetings = input("What's your name? ")
    name = greet(greetings)
    print(name)

if __name__ == '__main__':
    main()