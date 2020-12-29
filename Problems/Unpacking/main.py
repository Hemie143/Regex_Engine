def unpack(input_tuple):
    # your code here
    unpacked = tuple()
    for i in input_tuple:
        if isinstance(i, str):
            unpacked = unpacked + (i, )
        else:
            unpacked = unpacked + tuple(list(i))
    return unpacked
