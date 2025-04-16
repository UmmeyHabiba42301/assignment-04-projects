import random
import string

def generate_password(length):
    if length < 4:
        return "Password must be at least 4 characters long."

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_chars = lowercase + uppercase + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list to randomize character positions
    random.shuffle(password)

    return ''.join(password)

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    main()