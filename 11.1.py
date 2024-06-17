def create_word_dict(file_path):
    word_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            word_dict[word] = None  # The value can be anything, None in this case
    return word_dict

# Example usage
file_path = '/mnt/data/words.txt'
word_dict = create_word_dict(file_path)

# To check if a word is in the dictionary
word_to_check = 'example'
if word_to_check in word_dict:
    print(f"'{word_to_check}' is in the dictionary.")
else:
    print(f"'{word_to_check}' is not in the dictionary.")
