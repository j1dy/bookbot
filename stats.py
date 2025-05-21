def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    temp = text.lower()
    chars = {}
    for char in temp:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_key(k):
    return k["num"]

def sort_chars(chars):
    char_list = []
    for char in chars:
        char_list.append({"char": char, "num": chars[char]})
    char_list.sort(reverse=True, key=sort_key)
    return char_list