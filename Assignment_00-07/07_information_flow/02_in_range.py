def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # We could have also used an else statement, but since we are returning, it's fine without!
    return False

def main():
    # Example usage, you can modify or ask for user input as needed
    num = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    if in_range(num, low, high):
        print(f"{num} is in the range between {low} and {high}.")
    else:
        print(f"{num} is NOT in the range between {low} and {high}.")

if __name__ == '__main__':
    main()