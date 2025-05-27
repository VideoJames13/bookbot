import sys

#takes the file and returns all the text within
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents

from stats import word_count

from stats import character_count

from stats import list_sort

#this is where it all comes together
def main():
    if len(sys.argv) == 2:
        contents = get_book_text(sys.argv[1])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count(contents)} total words")
        print("--------- Character Count -------")
        for dict in list_sort(character_count(contents)):
            print(f"{dict["char"]}: {dict["num"]}")
    else:
        print("Hey dummy, Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()