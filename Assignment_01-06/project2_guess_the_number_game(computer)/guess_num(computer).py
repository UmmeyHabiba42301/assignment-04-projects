def main():
    print("🔢 Think of a number between 1 and 100, and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    guesses = 0
    guessed_correctly = False

    while not guessed_correctly and low <= high:
        guess = (low + high) // 2
        guesses += 1
        print(f"My guess is {guess}.")

        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").strip().lower()

        if feedback == "c":
            print(f"🎉 I guessed your number in {guesses} tries!")
            guessed_correctly = True
        elif feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        else:
            print("⚠️ Please enter 'h' for high, 'l' for low, or 'c' for correct.")

    if not guessed_correctly:
        print("Hmm 🤔 seems like something went wrong... Did you change your number?")

if __name__ == '__main__':
    main()