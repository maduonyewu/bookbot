from stats import get_word_count, get_character_count, sort_dict
import sys

def get_book_text(fp):
    txt = ""
    with open(fp) as f:
        txt = f.read()
    return txt


def main():
    #text = get_book_text("./books/frankenstein.txt")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    word_count = get_word_count(text)
    #print(f"{word_count} words found in the document")
    char_count = get_character_count(text)
    print(char_count)
    print("============ BOOKBOT ============")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_char_count = sort_dict(char_count)
    for k,v in sorted_char_count.items():
        if k.isalpha():
            print(f"{k}: {v}")
    print("============= END ===============")
    #print(sort_dict(char_count))


main()