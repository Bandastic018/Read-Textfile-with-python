# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from itertools import count


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, "r") as f:
        words = f.read()
    return words


print(read_file_content(
    "C:/Users/Larous/Desktop/banda/Khady-Kubs folder/i4Zuri Training/Reading-Text-Files/story.txt"))


def count_words():
    text = read_file_content(
        "C:/Users/Larous/Desktop/banda/Khady-Kubs folder/i4Zuri Training/Reading-Text-Files/story.txt")
# [assignment] Add your code here
    split_text = text.split()
    count = {}
    for k in split_text:
        if k in count:
            count[k] += 1
        else:
            count[k] = 1
    return count


print(count_words())

#  return {"as": 10, "would": 20}
