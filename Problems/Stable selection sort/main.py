def sort_names(names):
    """Sort names by length in ascending order."""
    for i in range(len(names) - 1):
        index = i

        for j in range(i + 1, len(names)):
            if len(names[j]) < len(names[index]):
                index = j

        # names[i], names[index] = names[index], names[i]
        names.insert(i, names.pop(index))
    return names

n = int(input())
names = []
for i in range(n):
    names.append(input())
sort_names(names)
print("\n".join(names))
