from nltk.corpus import brown

category = input()
print(brown.fileids(categories=category)[:3])
