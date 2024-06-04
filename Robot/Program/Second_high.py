a = [2,6,8,9,1,2,12,10,8,9]
high = 0
second_high = 0
res = 0
for i in a:
    if i > high:
        second_high = high
        high = i

    else:
        second_high = max(second_high, i)

print(second_high)












