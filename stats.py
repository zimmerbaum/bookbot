def count_words(file_contents):
  file_contents_wordsplit = file_contents.split()
  #print(f"{len(file_contents_wordsplit)} words found in the document")
  return len(file_contents_wordsplit)

def count_chars(file_contents):
  file_contents_lower = file_contents.lower()
  #print(file_contents_lower)
  char_count = {}
  for char in file_contents_lower:
    #print(char)
    if (char not in char_count):
      #print(True)
      char_count.update({char : 1})
    else:
      char_count[char] += 1
  #print(char_count)
  return char_count



def sort_count(char_count):
  #print(char_count)
  result = []
  for char, count in char_count.items():
    char_entry = {"character": char, "count": count}
    result.append(char_entry)

  def sort_on(dict):
    return dict["count"]
  result.sort(reverse=True, key=sort_on)
  return result