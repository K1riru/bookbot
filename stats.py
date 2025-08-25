def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(chars):
    return chars["num"]


def listify(chars_dict):
    lists = []
    for char, num in chars_dict.items():
        if not char.isalpha():
            continue 
        lists.append({"char":char, "num": num})
    lists.sort(reverse = True, key = sort_on)    
    return lists