
def quick_sortv1(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x< pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x==pivot]
    return quick_sortv1(left) + middle + quick_sortv1(right)


def partitionv2(arr, low, high):
    pivot = arr[high] # choosing last element as pivot
    i = low-1 # pointer for the smaller element 

    for j in range(low, high):
        if arr[j] < pivot:
            i+=1
            arr[i], arr[j] =arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1 # return the pivot point

def quick_sort_inplacev2(arr, low, high):
    if low < high:
        pi = partitionv2(arr, low, high)
        quick_sort_inplacev2(arr, low, pi-1)
        quick_sort_inplacev2(arr,pi + 1, high)  



arr = [10, 7, 8, 9, 1, 5]
quick_sort_inplacev2(arr, 0, len(arr) - 1)
print(arr)


unsorted_list = [4,4,2,6,2,673,2,4,24]
sorted_list = quick_sortv1(unsorted_list)
print(sorted_list)