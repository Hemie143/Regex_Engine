def bin_search(elements, target):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == target:
            return middle
        elif target < elements[middle]:
            right = middle - 1
        else:
            left = middle + 1

    return -1

list1 = [int(x) for x in input().split()]
list2 = [int(x) for x in input().split()]
result = [str(bin_search(list2, n)) for n in list1]
print(" ".join(result))
