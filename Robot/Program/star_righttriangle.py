def right_triangle(n):
    for i in range(1, n+1):
        for j in range(i):
            print('*', end="")
        print()

right_triangle(5)