def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2 
        left = nums[:mid]
        print(len(left))
        right = nums[mid:]
        print(len(right))
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1    
        while i < len(left):
             nums[k] = left[i]
             i += 1
             k += 1
        while j < len(right):
             nums[k] = right[j]
             j += 1
             k += 1
 
list_1 = [7, 89, 25, 4, 3, 2, 87, 45, 23, 12, 96, 365, 159, -1, 5]
print(list_1)
merge_sort(list_1)
print(list_1)
