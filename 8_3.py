#Exercise 8.3

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('taco'))

# I created the function using is_palindrome and incorporated the slice [::-1]
# You use a print function to and input a word to determine if it is True or False
