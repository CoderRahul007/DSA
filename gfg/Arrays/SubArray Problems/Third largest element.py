class Solution:
    def thirdLargest(self,a, n):
        # code here
        if n < 3:
            return -1
  
        # Traverse through all array elements
        for i in range(3): # bubble sort for 3 elements it will sort till 3 greatest element 
            swapped = False
     
            # Last i elements are already
            #  in place
            for j in range(0, n-i-1):
      
                # traverse the array from 0 to
                # n-i-1. Swap if the element
                # found is greater than the
                # next element
                if a[j] > a[j+1] :
                    a[j], a[j+1] = a[j+1], a[j]
                    swapped = True
     
            # IF no two elements were swapped
            # by inner loop, then break
            if swapped == False:
                break
        return a[-3]
