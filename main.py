import sys
from stats import get_num_words, count_chars, convert_to_list, sort_count

def main():
    if len(sys.argv) != 2:
        print("Usage: Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    
    word_count = get_num_words(filepath)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    counts = count_chars(filepath)
    items = convert_to_list(counts)
    sorted_items = sort_count(items)

    print("--------- Character Count -------")
    for item in sorted_items:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
