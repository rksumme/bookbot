from stats import count_words, count_char, organize
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    words = count_words(text)
    characters = count_char(text)
    output = organize(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for line in output:
        print(f"{line["char"]}: {line["num"]}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

main()