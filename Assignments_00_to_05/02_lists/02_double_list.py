def main():
    numbers_list :list[int] = [2,3,4,5]

    for i in range(len(numbers_list)):
        at_index = numbers_list[i]
        numbers_list[i] = at_index * 2
    print(numbers_list)



if  __name__ == '__main__':
    main()
