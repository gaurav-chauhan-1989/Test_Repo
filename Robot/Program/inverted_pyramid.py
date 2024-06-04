def inverted_pyramid(n):
    for i in range(1, n+1):
        for j in range(1, i):
            print(' ', end="")
        for k in range(0, (n+1)-i):
            print('*', end=" ")
        print()

inverted_pyramid(5)