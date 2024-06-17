def most_frequent(input_string):
    # Remove spaces and convert to lowercase
    input_string = input_string.replace(" ", "").lower()

    # Create a dictionary to count letter frequencies
    frequency_dict = {}
    for char in input_string:
        if char.isalpha():  # Consider only alphabetic characters
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1

    # Sort the dictionary by frequency in descending order
    sorted_freq = sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)

    # Print the letters in decreasing order of frequency
    for char, freq in sorted_freq:
        print(f"{char}: {freq}")


# Test the function with text samples in different languages
english_text = "This is a simple example text in English."
spanish_text = "Esto es un texto de ejemplo en español."
french_text = "Ceci est un texte d'exemple en français."
german_text = "Dies ist ein Beispieltext auf Deutsch."

print("English Text:")
most_frequent(english_text)
print("\nSpanish Text:")
most_frequent(spanish_text)
print("\nFrench Text:")
most_frequent(french_text)
print("\nGerman Text:")
most_frequent(german_text)

