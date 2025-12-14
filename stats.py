def count_words(book):
    words = book.split()
    num_words = len(words)
    return num_words

def count_char(book):
    characters = {}
    lower_case = book.lower()
    for letter in lower_case:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    return characters