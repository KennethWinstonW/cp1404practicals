"""
Word Occurrences
Estimate: 30 minutes
Actual: 26 minutes
"""

word_to_count = {}
text = input("Text: ")

words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(word_to_count.keys())
words.sort()

word_length = max((len(word) for word in words))
for word in words:
    print(f"{word:<{word_length}} : {word_to_count[word]}")
    # sorted and formatted the words in alphabetical order and for easy reading

