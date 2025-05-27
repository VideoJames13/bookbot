def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count

from stats import character_count

from stats import list_sort

#fake comment for streak!

def main():
    contents = get_book_text("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(contents)} total words")
    print("--------- Character Count -------")
    for dict in list_sort(character_count(contents)):
        print(f"{dict["char"]}: {dict["num"]}")

main()