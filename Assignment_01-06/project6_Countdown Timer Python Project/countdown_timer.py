import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end='\r')  # Overwrites the previous line
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up! 🚨")

def main():
    print("🕒 Countdown Timer")
    user_input = input("Enter time in seconds: ")

    if user_input.isdigit():
        countdown(int(user_input))
    else:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()