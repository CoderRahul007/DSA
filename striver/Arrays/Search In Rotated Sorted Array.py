# Finally, to put everything in points:

#     Find the mid index.
#     If the value(key) being searched for is at the mid index, then return the mid index.
#     Compare values at start index, end index, and mid-index:
#         If the left subarray is sorted, check if the value(key) to be searched lies in the range:
#             If it does, then search space reduces between [start, (mid-1)].
#             Otherwise, the search space reduces between [(mid + 1), end]
#         If the right subarray is sorted, check if the value(key) to be searched lies in the range:
#             If it does, then search space reduces between [(mid + 1), end].
#             Otherwise, the search space reduces between [start, (mid -1)]
#     Repeat from step-1 until the key is found.
#     Return -1 if never found.

# Time Complexity

# O(log(N)), Where N is the total number of elements in the array.

 
'''
    Time complexity : O(log(N))
    Space complexity : O(1)

    Where N is the size of array
'''

def search(arr, target) :
    
    # Initialize start and end
    st = 0
    end = len(arr) - 1
        
    # Performing binary search
    while(st <= end) :

        # Get the middle element
        mid = st + (end - st) // 2
        
        # The middle element is the one we are searching for
        if(arr[mid] == target) :
            return mid
        
        elif(arr[mid] >= arr[st]) :

            # Element lies towards left of mid
            if(arr[st] <= target and target <= arr[mid]):
                end = mid - 1
            
            # Element lies towards right of mid    
            else :
                st = mid + 1
            
        else :
            
            # Element lies towards right of mid
            if(arr[end] >= target and target >= arr[mid]) :
                st = mid + 1
            
            # Element lies towards left of mid
            else :
                end = mid - 1
    
    # Element not found
    return -1   