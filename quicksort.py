
def quick_sortv1(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x< pivot]
    right = [x for x in arr if x > pivot]
    middle = [x for x in arr if x==pivot]
    return quick_sortv1(left) + middle + quick_sortv1(right)


unsorted_list = [4,4,2,6,2,673,2,4,24]
sorted_list = quick_sortv1(unsorted_list)
print(sorted_list)