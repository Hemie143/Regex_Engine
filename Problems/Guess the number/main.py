x = int(input())
lx, rx = (int(n) for n in input().split())
tries = 0

# put your code here
while lx <= rx:
    tries += 1
    middle = (lx + rx) // 2
    if middle == x:
        break
    elif x < middle:
        rx = middle - 1
    else:
        lx = middle + 1

print(tries)
