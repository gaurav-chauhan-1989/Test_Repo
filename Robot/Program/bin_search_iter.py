def bin_search(arr, a):
    arr.sort()
    min = 0
    max = len(arr)-1
    while min <= max:
        mid = (min+max)//2
        if arr[mid] == a:
            return mid

        elif arr[mid] > a:
            max = mid-1

        elif arr[mid] < a:
            min = mid+1

a = [9,3,7,4,6,0,5,2]
z = bin_search(a, 2)
print(z)
