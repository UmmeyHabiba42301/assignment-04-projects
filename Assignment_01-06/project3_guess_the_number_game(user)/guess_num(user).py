import random

def main():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100...")

    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congrats! You guessed it in {attempts} attempts.")
                guessed_correctly = True

        except ValueError:
            print("❗ Please enter a valid integer.")

if __name__ == '__main__':
    main()