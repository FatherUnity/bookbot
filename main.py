from stats import get_num_words, count_chars

def main():
    word_count = get_num_words("./books/frankenstein.txt")
    chars = count_chars("./books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(chars)
    
main()