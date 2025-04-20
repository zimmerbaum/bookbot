import sys
from stats import count_words
from stats import count_chars
from stats import sort_count

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  file_path = sys.argv[1]
  get_book_text(file_path)

def get_book_text(file_path):
  #file_path = input("File path: ")
  with open(f"{file_path}") as f:
    file_contents = f.read()
  #print(file_contents)
  word_count = count_words(file_contents)
  character_count_sorted = sort_count(count_chars(file_contents))
  print_result(word_count, character_count_sorted, file_path)
  
def print_result(word_count, character_count_sorted, file_path):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {file_path}...")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char in character_count_sorted:
    if (char["character"].isalpha()):
      print(f"{char["character"]}: {char["count"]}")
  print("============= END ===============")


main()