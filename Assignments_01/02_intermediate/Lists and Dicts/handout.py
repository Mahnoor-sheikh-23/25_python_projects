def main():
    # PROBLEM " 01 "
    fruit_list :list = ["apple", "banana", "cherry","date","pineapple"]
    print(f"\n🍎 Initial fruit list length: {len(fruit_list)}")
    fruit_list.append("mango")
    print(f"\n🍇 Updated fruit list: {fruit_list}\n")

if  __name__ == "__main__":
    main()

# PROBLEM 02
list_1 = ["onion", "potato", "tomato", "ginger", "garlic"] 


# ACCESS ELEMNST 
def accessing_element(list , index):
    try:
        print(f"\n🔍 Accessed element: {list[index]}\n")
    except :
        print("\n❌ Element not found\n")
accessing_element(list_1, 4)



# MODIFYING FUNCTION 
def modifying_element(list, index, element):
    try:
        list[index] = element
        print(f"\n✏️ Modified list: {list}\n")
    except :
        print("\n❌ Element not found\n")

modifying_element(list_1, 3, "carrot")


# SLICING FUNCTION 
def slicing_list(list, start, end):
    try:
        print(f"\n🔪 Sliced list: {list[start:end]}\n")
    except :
        print("\n❌ Elements are out of range!!\n")

slicing_list(list_1, 1, 4)




# GAMESS FUNCTION 
def game():
    list_of_brands = ["gucci", "prada", "louis vuitton", "chanel", "dior","versace"]
    print(f"\n👜 List of brands: {list_of_brands}\n")
    user = input("Select an operation (access, modify, slice): ").strip().lower()
    if user == "access":
        index = int(input("Enter the index of the element you want to access: "))
        try:
            print(f"\n🔍 Accessed brand: {list_of_brands[index]}\n")
        except:
            print("\n❌ Element not found\n")
    elif user == "modify":
        index = int(input("Enter the index of the element you want to modify: "))
        element = input("Enter the element you want to replace with: ")
        try:
            list_of_brands[index] = element
            print(f"\n✏️ Modified list of brands: {list_of_brands}\n")
        except:
            print("\n❌ Element not found\n")
    elif user == "slice":
        start = int(input("Enter the starting index: "))
        end = int(input("Enter the ending index: "))
        try:
            print(f"\n🔪 Sliced list of brands: {list_of_brands[start:end]}\n")
        except:
            print("\n❌ Elements are out of range!!\n")
    else:  
        print("\n❌ Invalid input\n")

game()






