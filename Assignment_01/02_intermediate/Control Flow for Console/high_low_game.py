import random

# Constant for the number of rounds to play
NUM_ROUNDS = 5

def play_round(round_num):
    """
    Plays a single round of the High-Low game.
    The round prints the result and updates the score.
    """
    # Generate random numbers for the user and the computer
    computer_number = random.randint(1, 100)
    user_number = random.randint(1, 100)
    
    # Print the current round and user's number
    print(f"Round {round_num}")
    print(f"Your number is {user_number}")
    
    # Get the user's guess (higher or lower)
    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    
    # Ensure valid input from the user
    while guess not in ['higher', 'lower']:
        print("Please enter either 'higher' or 'lower'.")
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    
    # Compare the user's guess with the computer's number and calculate the result
    if (guess == 'higher' and user_number > computer_number) or (guess == 'lower' and user_number < computer_number):
        print(f"You were right! The computer's number was {computer_number}")
        return True
    elif user_number == computer_number:
        print(f"The numbers are the same. The computer's number was {computer_number}. You didn't score this round.")
        return False
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        return False

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0  # Initialize the score

    # Play the game for the specified number of rounds
    for round_num in range(1, NUM_ROUNDS + 1):
        if play_round(round_num):
            score += 1
        print(f"Your score is now {score}\n")  # Print score after each round

    # Print the final score and a message based on the score
    print("Thanks for playing!")
    print(f"Your final score is {score}")
    
    # Ending messages based on performance
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()