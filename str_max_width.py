def wrap(string, max_width):
    n = 1
    for char in string:
        print(char, end='')
        if n == max_width:
            print()
            n = 0
        n += 1
    print()
    return


wrap("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 4)
