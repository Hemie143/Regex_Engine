# implement the binary search here
n, w, h = [int(x) for x in input().split()]
area = n * w * h

def bin_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle - 1] < target <= arr[middle]:
            return middle
        elif target < arr[middle]:
            right = middle - 1
        else:
            left = middle + 1    
    return middle

print(bin_search(frames, area ** 0.5))
