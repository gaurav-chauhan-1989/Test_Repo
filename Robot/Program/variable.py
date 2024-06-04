def second_largest(a):
    largest = 0
    second_largest = 0
    for i in a:
        if i > largest:
            second_largest = largest
            largest = i
        else:
            second_largest = max()
    return second_largest



num = second_largest([1,4,6,8,7,5,8,12,15,2,19])
print(num)

