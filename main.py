from stats import get_num_words

def main():
    word_count = get_num_words("./books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    
main()