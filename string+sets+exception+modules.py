import math

try:
    # Take sentence as input
    sentence = input("Enter a sentence: ")

    # Check for empty input
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")

    # Extract unique words
    words = sentence.lower().split()
    unique_words = set(words)

    # Print unique words in sorted order
    print("\nUnique Words (Sorted):")
    for word in sorted(unique_words):
        print(word)

    # Number of unique words
    count = len(unique_words)

    # Print count raised to power 2
    print("\nTotal Unique Words:", count)
    print("Square of Total Unique Words:", math.pow(count, 2))

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("An unexpected error occurred:", e)