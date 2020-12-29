def contains(text, pattern, start):
    for i in range(start, len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                # found = False
                break
        else:
            return i
    return -1


def find_no_overlaps(text, pattern):
    result = []
    start = 0
    while True:
        i = contains(text, pattern, start)
        if i > -1:
            result.append(str(i))
            start = i + len(pattern)
        else:
            if result:
                return " ".join(result)
            return "-1"

text = input()
pattern = input()
print(find_no_overlaps(text, pattern))
