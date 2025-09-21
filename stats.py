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