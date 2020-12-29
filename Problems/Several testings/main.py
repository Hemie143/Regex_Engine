def check(x):
    if x.isnumeric():
        x = int(x)
        if x >= 202:
            print(x)
        else:
            print("There are less than 202 apples! You cheated on me!")
    else:
        print("It is not a number!")