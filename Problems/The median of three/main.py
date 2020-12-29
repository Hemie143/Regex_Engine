def choose_median(lst, start, middle, end):
    # finish the method for finding the median
    a = lst[start]
    b = lst[middle]
    c = lst[end]
    if a <= b <= c or c <= b <= a:
        return middle
    if a <= c <= b or b <= c <= a:
        return end
    return start

def partition(lst, pivot, start, end):
    # add necessary modifications
    # don't forget to print the result of the partition!
    j = start
    for i in range(start + 1, end):
        if lst[i] <= pivot:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


# read the input list
# and call the methods
# numbers = [int(n) for n in input().split(" ")]
# numbers = [int(n) for n in "30 60 50 20 40".split(" ")]
numbers = [int(n) for n in "60 10 30 20".split(" ")]

middle = len(numbers) // 2
pivot = choose_median(numbers, 0, middle, len(numbers) - 1)
print(pivot)
partition(numbers, pivot, 0, len(numbers))
print(numbers)