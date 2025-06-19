def get_book_text(path_to_file): 
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    char_counts = {}
    for char in text:
        if not char.isalpha():
            continue
        lowered_char = char.lower()
        if lowered_char in char_counts:
            char_counts[lowered_char] += 1
        else:
            char_counts[lowered_char] = 1
    return char_counts

def get_list_of_dictionary(dict):
    list_of_dict = []
    for key, value in dict.items():
        list_of_dict.append({"char": key, "num": value})
    list_of_dict.sort(key=lambda x: x["num"], reverse=True)
    return list_of_dict