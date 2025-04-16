import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Choose rock, paper, or scissors: ").strip().lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = get_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
