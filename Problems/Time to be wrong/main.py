def print_list(some_list):
    for i in range(len(some_list)):
        some_list[i] = int(some_list[i])
        if some_list[i] % 2 == 0:
            print(some_list[i])
        if some_list[i] % 3 == 0:
            print(some_list[i] % 3)