from nltk.corpus import treebank

file = input()
print(treebank.tagged_words(file)[0])
