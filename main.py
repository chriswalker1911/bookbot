import sys
from stats import count_characters
from stats import count_words
from stats import sort_character_count

def get_book_text(path):
    with open(path) as f: 
        return f.read()

def main ():
    book = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at: {sys.argv[1]}\n")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words\n")
    print("--------- Character Count -------\n")
    for characters in sort_character_count(count_characters(book)):
        #print(f"{characters[0]}: {characters[1]}\n")
        if characters["char"].isalpha(): 
            print(f"{characters['char']}: {characters['num']}\n")
    print("============= END ===============\n")

if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()