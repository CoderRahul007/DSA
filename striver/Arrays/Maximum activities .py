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


def maximumActivities(start, finish):
    # Write your Code here.
    temp = []
    for i in range(len(start)):
        temp.append([start[i] , finish[i]])
    temp.sort(key=lambda x: x[1])
    res = temp[0]
    c  = 1
    for i in range(1  , len(start)):
        if res[1] <= temp[i][0]:
            c+=1
            res = temp[i]
    return c
        
    