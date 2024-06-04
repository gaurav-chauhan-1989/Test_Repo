s = 'Gaurav Chauhan'
a = {}
for i in s:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
max_occ = max(a, key=a.get)    # To get maximum occurrence in a dictionary.
print(max_occ)
print(a)