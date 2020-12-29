from nltk.corpus import gutenberg

file = input()
print(len(gutenberg.sents(file)))
