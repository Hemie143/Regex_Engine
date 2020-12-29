def partition(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i][1] < lst[start][1]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]
        elif lst[i][1] == lst[start][1] and lst[i][0] < lst[start][0]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j

def quick_sort(lst, start, end):
    if start >= end:
        return

    j = partition(lst, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, j + 1, end)

n = int(input())
students = []
for _ in range(n):
    students.append(tuple([s for s in input().split(" ")]))
quick_sort(students, 0, len(students) - 1)
for s in students:
    print(f'{s[0]}')
