def partition(arr, min, max):
    pivot = arr[max]
    i = min-1

    for j in range(min, max):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[max]=arr[max],arr[i+1]
    return i+1

def quick_sort(arr, min, max):
    if min < max:
        p = partition(arr, min, max)

        quick_sort(arr, min, p-1)

        quick_sort(arr, p+1, max)

a = [9,3,7,4,6,0,5,2]
quick_sort(a, 0, len(a)-1)
print(a)