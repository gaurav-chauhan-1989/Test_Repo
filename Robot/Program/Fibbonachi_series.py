def fib(n):
    if n<=1:
        return n
    else:
        return fib(n) + fib(n-1)

a = 10
for i in range(a):
    print(fib(i))