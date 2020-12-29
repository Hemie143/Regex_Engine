def partition(lst, start, end):
    j, k = start, end
    i = j
    while i <= k:
        if lst[i] < lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
        elif lst[i] > lst[start]:
            lst[i], lst[k] = lst[k], lst[i]
            k -= 1
            i -= 1
        i += 1
    lst[start], lst[j] = lst[j], lst[start]
    return j, k

def quick_sort(lst, start, end):
    if start >= end:
        return

    j, k = partition(lst, start, end)
    # if j>0 and k>0:
    print(j, k)
    # quick_sort(lst, start, j - 1)
    # quick_sort(lst, k + 1, end)

numbers = [int(n) for n in input().split(" ")]
if len(numbers) == 1:
    print("0 0")
    print(numbers[0])
else:
    quick_sort(numbers, 0, len(numbers) - 1)
    print(" ".join([str(n) for n in numbers]))
