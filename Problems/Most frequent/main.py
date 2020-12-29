from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        "I may be off my dot but I want a cup of coffee from a proper coffee pot.")

n = int(input())
word_count = Counter(text.split())

for word, count in word_count.most_common(n):
    print(f'{word} {count}')
