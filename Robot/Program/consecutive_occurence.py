s = "aabbbccaaaacccccddcc"

d = {}
c = ''
for i in s:
    if i in d and i ==c:
        temp = d[i]
        d[i] +=1
    else:
        d[i] = 1
    c = i

print(d)

max_occ = max(d, key=d.get)
print(f"Max occurence is {max_occ}: {d[max_occ]}")