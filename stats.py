def get_num_words(filepath):
    with open(filepath) as book:
        raw = book.read()
        count = raw.split()
        return len(count)

def count_chars(filepath):
    dictionary = {}
    with open(filepath) as book:
        text = book.read()
        lower_text = text.lower()
        for ch in lower_text:
            if ch in dictionary:
                dictionary[ch] += 1
            else:
                dictionary[ch] = 1
    return dictionary
# Key to sort items
def sorter(items):
    return items["num"]
# if character is not alphanumeric, skip, else add to items dictionary
def convert_to_list(chars):
    items = []
    for ch, num in chars.items():
        if not ch.isalpha():
            continue
        items.append({"char": ch, "num": num})
    return items
        
def sort_count(items):
    items.sort(key=sorter, reverse=True)
    return items