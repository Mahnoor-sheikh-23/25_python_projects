import requests
import random

def fetch_random_word():
    url = "https://www.randomlists.com/data/words.json"
    response = requests.get(url)
    data = response.json()
    words = data["data"]
    return random.choice(words).lower()

def hangman():
    word = fetch_random_word()
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()   # User's guessed letters
    tries = 8                 # Maximum attempts

    print("\n🎮 Welcome to Hangman!")
    print("_ " * len(word))  # Display blanks for the word

    while tries > 0 and word_letters:
        guess = input("\nGuess a letter: ").lower()

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print("✅ Correct guess!")
        else:
            guessed_letters.add(guess)
            tries -= 1
            print(f"❌ Wrong guess! {tries} tries left.")

        # Display current progress
        display_word = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display_word))

    # Check win/lose condition
    if not word_letters:
        print("\n🎉 You won! The word was:", word)
    else:
        print("\n💀 You lost! The word was:", word)

# Run the game
hangman()
