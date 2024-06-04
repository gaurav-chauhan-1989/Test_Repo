def full_pyramid(n):
    mid = (n // 2) + 1
    for i in range(1, n + 1):
        if i <= mid:
            for j in range(mid - i):
                print(" ", end="")
            for k in range(i):
                print('*', end=" ")
            print()
        else:
            for j in range(mid, i):
                print(" ", end="")
            for k in range(i, n + 1):
                print("*", end=" ")
            print()


full_pyramid(9)