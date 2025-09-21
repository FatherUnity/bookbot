def get_num_words(filepath):
    with open(filepath) as book:
        raw = book.read()
        count = raw.split()
        return len(count)
