def is_odd(val):
    if val % 2 == 0 :
        return val

def main():
    for i in range(1,10+1):
        if is_odd(i):
            print("odd!")
        else:
            print("Even!")

if __name__ == "__main__":
    main()
