from stats import get_word_count

def get_book_text(fp):
    txt = ""
    with open(fp) as f:
        txt = f.read()
    return txt


def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")

main()