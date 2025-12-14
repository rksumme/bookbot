from stats import count_words, count_char

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    words = count_words(text)
    characters = count_char(text)

    print(f"Found {words} total words")
    print(characters)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

main()