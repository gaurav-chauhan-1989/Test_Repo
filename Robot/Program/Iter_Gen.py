def gen(n):
    for i in range(n):
        yield i

a=gen(5)
print(a.__next__())
print(a.__next__())