def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count

def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(f"{word_count(contents)} words found in the document")

main()