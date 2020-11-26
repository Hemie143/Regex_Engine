
def match(regex, text):
    if regex == text or regex == '.' or regex == '':
        return True
    elif text == '':
        pass
    return False

regex, text = input().split('|')

print(match(regex, text))
