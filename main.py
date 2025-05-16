def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        return file_contents
def word_count(file_contents):
    count = len(file_contents.split())
    return count

def main():
    contents = get_book_text("./books/frankenstein.txt")
    print(f"{word_count(contents)} words found in the document")

main()