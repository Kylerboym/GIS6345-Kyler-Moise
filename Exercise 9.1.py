# Open the file
with open(r'C:\Users\kyler\OneDrive\Desktop\GIS6345\Week5\words.txt', 'r') as file:
    # Read all lines in the file
    words = file.readlines()

# Loop through each word
for word in words:
    # Strip any whitespace characters and check the length
    if len(word.strip()) > 20:
        # Print the word
        print(word.strip())
