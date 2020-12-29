def kth(numbers, target, k):
    occ = 0
    for i, n in enumerate(numbers):
        if n == target:
            occ += 1
            if occ == k:
                return i
    return -1

numbers = input().split(" ")
target = input()
k = int(input())
print(kth(numbers, target, k))
