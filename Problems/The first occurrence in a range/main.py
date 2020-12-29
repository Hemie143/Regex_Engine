def search(numbers, target, a, b):
    for i, n in enumerate(numbers[a:b]):
        if n == target:
            return a + i
    return -1

numbers = input().split(" ")
target = input()
a, b = input().split(" ")
a = int(a)
b = int(b)
print(search(numbers, target, a, b))
