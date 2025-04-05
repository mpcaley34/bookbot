from stats import num_words, letter_count, sort_d
import sys


def get_book_text(filepath):
    # returns contents of file as string
    with open(filepath) as f:

        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = num_words(book_text)
    char_counts = letter_count(book_text)
    letter_only_counts = {char: count for char,
                          count in char_counts.items() if char.isalpha()}
    sorted_counts = sort_d(letter_only_counts)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_path}')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char, count in sorted_counts:
        print(f'{char}: {count}')
    print('============= END ===============')


main()
