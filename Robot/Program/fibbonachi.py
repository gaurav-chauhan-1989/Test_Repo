def fib(n):
    a = 0
    b = 1
    count = 1
    if n <= 1:
        print(n)

    else:
        while count <= n:
            print(a)
            c = a+ b
            a = b
            b = c
            count+=1

fib(10)

