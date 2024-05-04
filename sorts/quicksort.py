def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
print(quicksort([10, 8, 25, 456, 74, 1, 2, 3, 4, 8, 7, 9, 5, 2, 3]))
print(quicksort([10, 5, 3, 2]))
