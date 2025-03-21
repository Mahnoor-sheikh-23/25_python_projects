Max_term = 10000
def main():
    current_num = 0
    next_num = 1
    while current_num <= Max_term:
        print(current_num)
        after_next = current_num + next_num
        current_num = next_num
        next_num = after_next


if __name__ == "__main__":
    main()
