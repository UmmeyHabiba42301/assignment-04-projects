def main():
    curr_value = int(input("Enter a number: "))  # Get the user input as an integer
    
    # While the current value is less than 100, keep doubling and printing it
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the current value
        print(curr_value, end=' ')  # Print the current value with a space on the same line
    
    print()  
if __name__ == '__main__':
    main()
