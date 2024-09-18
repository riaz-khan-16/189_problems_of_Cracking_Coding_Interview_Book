def search_rotated_sorted_array(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # If the target is at the mid
        if arr[mid] == target:
            return mid
        
        # Check if the left half is sorted
        if arr[left] <= arr[mid]:
            # If target is in the left half
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            # If target is in the right half
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1  # Target not found
