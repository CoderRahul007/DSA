def printPairs(arr, n, sum):
     
    # Store counts of all elements
    # in a dictionary
    mydict = dict()
 
    # Traverse through all the elements
    for i in range(n):
         
        # Search if a pair can be
        # formed with arr[i]
        temp = sum - arr[i]
         
        if sum - arr[i] in mydict:
            count = mydict[temp]
            for j in range(count):
                print("(", temp, ", ", arr[i],
                      ")", sep = "", end = '\n')
                       
        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1
 
# Driver code
if __name__ == '__main__':
     
    arr = [ 1, 5, 7, -1, 5 ]
    n = len(arr)
    sum = 6
 
    printPairs(arr, n, sum)

##############################################################################################
from os import *
from sys import *
from collections import *
from math import *
from collections import OrderedDict

def pairSum(arr, s):
    n = len(arr)

    # Map to store frequency of elements.
    map = OrderedDict()

    # This will store the result.
    ans = []

    for ele in arr:
        count = map.get(s - ele, 0)

        pair = [-1 , -1]
        pair[0] = ele
        pair[1] = s - ele

        while count > 0:
            ans.append(pair)
            count -= 1

        map[ele] = map.get(ele, 0) + 1

    # This will store the final result.
    res = [[-1 for j in range(2)] for i in range(len(ans))]

    # Sorting the 'ans' array element.
    for i in range(len(ans)):
        a = ans[i][0]
        b = ans[i][1]
        res[i][0] = min(a, b)
        res[i][1] = max(a, b)
        
    # Finally sorting each pair in 'res'.
    res = sorted(res, key=lambda x: x[0])

    return res
                
# O(N^2), where ‘N’ is the number of elements in the array.

 

# For the worst case, when all elements are the same we must have to add ‘N’^2 pairs to the answer vector and so,
#  the overall time complexity will be O(N^2).
# Space Complexity

# O(N), where ‘N’ is the number of elements in the array.

 

# In the worst case, O(N) extra space is required for the hashmap to store the frequency of each element.
#  Hence the overall space complexity will be O(N).                