def has_no_e(word):
    """Returns True if the given word doesn't have the letter 'e' in it."""
    return 'e' not in word


def main():
    # Open the file
    with open(r'C:\Users\kyler\OneDrive\Desktop\GIS6345\Week5\words.txt', 'r') as file:
        # Read all lines in the file
        words = file.readlines()

    # Initialize a list to hold words with no 'e'
    no_e_words = []

    # Loop through each word
    for word in words:
        # Strip any whitespace characters
        stripped_word = word.strip()
        # Check if the word has no 'e'
        if has_no_e(stripped_word):
            # Add the word to the list
            no_e_words.append(stripped_word)
            # Print the word
            print(stripped_word)

    # Compute the percentage of words with no 'e'
    no_e_percentage = (len(no_e_words) / len(words)) * 100
    print(f"Percentage of words with no 'e': {no_e_percentage:.2f}%")


# Call the main function
if __name__ == '__main__':
    main()
