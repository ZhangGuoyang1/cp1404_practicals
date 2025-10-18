from operator import itemgetter

word_to_count = {}
word_count = 0
word_length = 0

text = input("Enter text: ")

words = text.split()
words = sorted(words)

for word in words:
    word_count = words.count(word)
    word_to_count[word] = word_count

word_to_count = dict(sorted(word_to_count.items(), key=itemgetter(0)))

for word in word_to_count:
    if len(word) > word_length:
        word_length = len(word)

for word, count in word_to_count.items():
    print(f"{word:<{word_length}} : {count}")
