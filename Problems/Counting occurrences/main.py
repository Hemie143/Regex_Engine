def count(numbers, target):
    result = 0
    for n in numbers:
        if n == target:
            result += 1
    return result

numbers = input().split(" ")
target = input()
print(count(numbers, target))
