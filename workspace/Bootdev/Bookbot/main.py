import sys

from stats import chars_dict_to_sorted_list, get_character_dict, get_num_words

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main() -> None:
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_character_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)



def get_book_text(book_path: str) -> str:
    with open(book_path) as f:
        return f.read()


def print_report(book_path: str, num_words: int, chars_sorted_list: list[tuple[str, int]]):
    print(f"""============ BOOKBOT ============
        Analyzing book found at {book_path}...
        ----------- Word Count ----------
        Found {num_words} total words
        --------- Character Count -------""")
    for char_tup in chars_sorted_list:
        char = char_tup[0]
        count = char_tup[1]
        if char.isalpha() == True:
            print(f"{char}: {count}")
    print("============= END ===============")


main()
