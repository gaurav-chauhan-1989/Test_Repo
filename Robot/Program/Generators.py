def generator():
    for i in range(10):
        yield i

a = generator()
print(a.__next__())
print(a.__next__())
