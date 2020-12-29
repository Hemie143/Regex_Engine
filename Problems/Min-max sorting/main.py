def minmax_sort(elements):
    for i in range(0, len(elements) - (len(elements) % 2), 2):
        min_i = i
        max_i = i + 1
        if elements[min_i] > elements[max_i]:
            elements[min_i], elements[max_i] = elements[max_i], elements[min_i]
        for j in range(i, len(elements)):
            if elements[j] < elements[min_i]:
                min_i = j
            if elements[j] > elements[max_i]:
                max_i = j
        elements[i], elements[min_i], elements[i + 1], elements[max_i] = elements[min_i], elements[i], elements[max_i], \
                                                                         elements[i + 1]


el = [int(e) for e in input().split(" ")]
minmax_sort(el)
print(" ".join([str(e) for e in el]))
