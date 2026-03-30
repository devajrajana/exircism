def find(search_list, target):
    low = 0
    high = len(search_list) - 1

    while low <= high:
        # Find the middle index
        mid = (low + high) // 2
        
        # Check if target is at mid
        if search_list[mid] == target:
            return mid
        
        # If target is greater, ignore left half
        elif search_list[mid] < target:
            low = mid + 1
            
        # If target is smaller, ignore right half
        else:
            high = mid - 1

    # Target was not found in the list
    raise ValueError("value not in array")