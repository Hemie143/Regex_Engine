def has_suffix(word, suffix):
    l = len(word) - len(suffix)
    for i in range(len(suffix)):
        if word[l + i] != suffix[i]:
            return False
    return True


# Change the next line
extension = ".py"
n = int(input())

for i in range(n):
    file = input()
    if has_suffix(file, extension):
        print(file)