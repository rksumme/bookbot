def count_words(book):
    words = book.split()
    num_words = len(words)
    return num_words

def count_char(book):
    characters = {}
    lower_case = book.lower()
    for letter in lower_case:
        if letter not in characters:
            characters[letter] = 1
        else:
            characters[letter] += 1
    return characters

def sort_by_num(items):
    return items["num"]

def organize(dictionary):
    dict_list = []
    
    for char in dictionary:
        dict_list.append({
            "char":char,
            "num":dictionary[char],
            })
    
    dict_list.sort(reverse=True, key=sort_by_num)
    return dict_list
