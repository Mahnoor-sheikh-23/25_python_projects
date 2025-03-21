import random

print("🎉 Welcome to the High-Low Game! 🎉\n")
print("--------------------------------")

Round = 0
Score = 0
while Round < 5:
    random_number = random.randint(1, 100)
    computer_numb = random.randint(1, 100)
    Round += 1
    print(f"🔄 Round : {Round}\n")
    print("🔢 Your number is : ", random_number)
    user_input = input("🤔 Do you think your number is higher or lower than the computer's? (type 'higher' or 'lower') ")

    if user_input.strip().lower() == "lower":
        if random_number < computer_numb:
            print(f"✅ You were right! The computer's number was : {computer_numb}")
            Score += 1
            print("🏆 Your score is now ", Score)
        else:
            print(f"❌ Aww, that's incorrect. The computer's number was : {computer_numb}")
    elif user_input.strip().lower() == "higher":
        if random_number > computer_numb:
            print(f"✅ You were right! The computer's number was : {computer_numb}")
            Score += 1
            print("🏆 Your score is now ", Score, "\n")
        else:
            print(f"❌ Aww, that's incorrect. The computer's number was : {computer_numb}")
    else:
        print("⚠️ Please just choose 'lower' or 'higher'!")