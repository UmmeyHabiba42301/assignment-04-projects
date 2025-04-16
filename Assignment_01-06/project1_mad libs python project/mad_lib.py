def main():
    print("Welcome to Mad Libs!\nLet's create a funny story together!")

    # Collect user input
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb (past tense): ")
    adverb = input("Enter an adverb: ")
    place = input("Enter a place: ")
    emotion = input("Enter an emotion: ")

    # Story template
    story = f"""
    It was a {adjective} day. I went outside and saw a {noun}.
    I {verb} it {adverb}, then ran all the way to {place}.
    Everyone looked at me and felt so {emotion}.
    What a day!
    """

    # Print the story
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == '__main__':
    main()