import sys
from stats import get_number_of_words
from stats import get_book_text
from stats import get_character_counts
from stats import get_list_of_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    number_of_words = get_number_of_words(book_text)
    character_counts = get_character_counts(book_text)
    character_counts = get_list_of_dictionary(character_counts)
    print(f"Found {number_of_words} total words")
    for char_count in character_counts:
        print(f"{char_count['char']}: {char_count['num']}")

main()