
def matchchar(regexchar, char):
    if regexchar == char or regexchar == '.' or regexchar == '':
        return True
    elif char == '':
        pass
    return False

def matchstring(regex, text):
    if len(regex) == 0:
        return True
    if len(text) == 0:
        if regex == '$':
            return True
        return False
    if matchchar(regex[0], text[0]):
        return matchstring(regex[1:], text[1:])
    else:
        return False


def match(regex, text):
    len_text = len(text)
    len_reg = len(regex)
    stop = len_text - len_reg + 1
    if regex and regex[-1] == '$':
        stop += 1
    if regex and regex[0] == '^':
        return matchstring(regex[1:], text)
    for i in range(stop):
        if matchstring(regex, text[i:]):
            return True
    return False

regex, text = input().split('|')
print(match(regex, text))
