def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count

from stats import character_count

from stats import list_sort

def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(f"{word_count(contents)} words found in the document")
    print(list_sort(character_count(contents))\n)

main()