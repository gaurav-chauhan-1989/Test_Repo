
a = [5,3,7,5,2,8,4,9,1,10,6]
size = len(a)
for i in range(size):
    for j in range(0,size-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)
