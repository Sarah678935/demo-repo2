def binary_search3(arr, target):
    left = 0
    right = len(arr) - 1
while left <= right:
        mid_point = (left + right) // 2    
 
        if target < arr[mid_point]:
            right = mid_point - 1
        elif target > arr[mid_point]:
            left = mid_point + 1
        else:
            return mid_point
return -1