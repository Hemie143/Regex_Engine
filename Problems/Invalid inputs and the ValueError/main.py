def check():
    try:
        x = int(input())
    except ValueError:
        print("Correct the error!")
    if 25 <= x <= 37:
        print(x)
    else:
        print("Correct the error!")
