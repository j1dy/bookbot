import sys
from stats import get_num_words, get_char_count, sort_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    words = get_num_words(text)
    chars = get_char_count(text)
    sorted = sort_chars(chars)
    report(path, words, sorted)

def get_book_text(path):
    with open(path) as book:
        return book.read()

def report(path, words, sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for x in sorted:
        if not x["char"].isalpha():
            continue
        print(f"{x['char']}: {x['num']}")
    print("============= END ===============")

main()