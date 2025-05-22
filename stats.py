# takes string and returns word count
def word_count(file_contents):
    count = len(file_contents.split())
    return count

# takes string and returns number of times each character appears
def character_count(file_contents):
    char_list = list(file_contents.lower())
    char_count = {}
    for character in char_list:
        if f"{character}" in char_count:
            char_count[f"{character}"] += 1
        else:
            char_count[f"{character}"] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def list_sort(dictionary):
    dict_list = []
    for character in dictionary:
        count = dictionary[character]
        dict_list.append({"char":f"{character}", "num": count})
        dict_list.sort(reverse=True, key=sort_on)
    return dict_list
