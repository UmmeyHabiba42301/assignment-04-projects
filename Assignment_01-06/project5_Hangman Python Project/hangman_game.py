import random

def get_random_word():
    words = ["python", "hangman", "challenge", "programming", "computer", "openai", "notebook"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def main():
    print("Welcome to Hangman! 🎉")
    word = get_random_word()
    guessed_letters = set()
    tries = 6

    while tries > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guesses left: {tries}")
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            print("Incorrect guess! ❌")
            tries -= 1
        else:
            print("Nice guess! ✅")

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 You guessed the word: {word}")
            break
    else:
        print(f"\n😢 You ran out of tries. The word was: {word}")

if __name__ == "__main__":
    main()