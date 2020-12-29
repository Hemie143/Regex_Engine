def fixed_search(numbers):
    for i, n in enumerate(numbers):
        if i == int(n):
            return True
    return False

numbers = input().split(" ")
print(fixed_search(numbers))
