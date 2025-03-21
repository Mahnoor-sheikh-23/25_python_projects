peturksbouipo = 16
stanlau = 25
mayengua = 48

def main():
    user_age = int(input("How old are you ? "))
    if user_age >= peturksbouipo:
        print(f"You can vote in Peturksbouipo where the voting age is : {peturksbouipo} ")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is : {peturksbouipo}")
    if user_age >= stanlau:
        print(f"You can vote in Stanlau where the voting age is : {stanlau}")
    else:
        print(f"You cannot vote in Stanlau where the voting age is : {stanlau}")
    if user_age >= mayengua:
        print(f"You can vote in Mayengua where the voting age is : {mayengua}")
    else:
        print(f"You cannot vote in Stanlau where the voting age is : {mayengua} ")

if __name__ == '__main__':
    main()

