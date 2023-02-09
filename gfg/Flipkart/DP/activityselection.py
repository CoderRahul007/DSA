# Given N activities with their start and finish day given in array start[ ] and end[ ].
#  Select the maximum number of activities that can be performed by a single person,
#  assuming that a person can only work on a single activity at a given day.
# Note : Duration of the activity includes both starting and ending day.


# Example 1:

# Input:
# N = 2
# start[] = {2, 1}
# end[] = {2, 2}
# Output: 
# 1
# Explanation:
# A person can perform only one of the
# given activities.

# Example 2:

# Input:
# N = 4
# start[] = {1, 3, 2, 5}
# end[] = {2, 4, 3, 6}
# Output: 
# 3
# Explanation:
# A person can perform activities 1, 2
# and 4.





class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        
        # code here
        arr = []
        for i in range(n):
            arr.append([start[i] , end[i]])        
        arr.sort(key = lambda x : x[1]) # sort by end time ascending order
        
        res = 1
        sol = arr[0]
        for i in range(1 , n):
            if sol[1] < arr[i][0]:
                res+=1
                sol = arr[i]
        return res

# Before arr  [[1, 2], [3, 4], [2, 3], [5, 6]]
# After arr  [[1, 2], [2, 3], [3, 4], [5, 6]]
# 3