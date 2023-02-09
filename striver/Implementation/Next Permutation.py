# https://www.codingninjas.com/codestudio/problems/next-permutaion_893046?topList=striver-sde-sheet-problems

# Greedy

# The basic idea of this approach is to develop a greedy algorithm to find the lexicographically next greater permutation.

# First of all, note that a permutation of integers which is sorted in descending order, will not have any 
# lexicographically greater permutation. For example, no next permutation will be possible for [4, 3, 2, 1].

 

# Now, consider two elements in the given permutation, P[i] and P[j] such that i < j. If P[i] < P[j], 
# we can easily swap the ith and the jth element to generate a permutation which will be necessarily greater 
# than the previous one. But in order to find the smallest among all of them we will have to choose (i, j) 
# such that the ith element will be farthest from the front and if there are multiple options for the jth element,
#  we will choose the smallest one. Why? Since we are considering the lexicographical ordering, a positive change 
#  in the element closer to front will generate a larger number than the other one. For example, consider [3, 4, 1, 2], 
#  if we choose i = 0, j = 1, then we will get next permutation [4, 3, 1, 2] and if we choose i = 2, j = 3, then we 
#  will get a lexicographically smaller permutation [3, 4, 2, 1]. Therefore, we should choose ‘i’ as large as possible.

# Now, consider the following steps:

#     Start iterating from the end of the given permutation and search a pair of indexes (i, i+1) such that P[i] < P[i+1].
#     If such a pair doesn’t exist, then the permutation is sorted in descending order. And as discussed above, the next permutation will be the
#      lexicographically smallest permutation i.e. the reverse of the given permutation.
#     Suppose we reached an index ‘i’ such that P[i] < P[i+1]. In this case, we can just swap to (i, i+1)th elements but the resulting permutation
#      may not be the just next greater permutation. Therefore, we will start searching for the smallest element which will be on the right side of 
#      the ith element and is greater than the ith element. Let's say the index of that element is ‘j’.
#     Now, swap P[i] and P[j]. After the swap operation, we will get a lexicographically greater permutation but that again may not be the immediate next one. 
#     Since the element at the ith index in the next permutation is greater than the ith element in the given permutation, we can sort all the elements after
#      ith index in ascending order to ensure that the next permutation is just greater one.
#     Now, notice that the ith index is the first index from the end for which P[i] < P[i+1], i.e. elements in the right side of the ith element must be sorted 
#     in descending order. And after doing the swap operation on ith and jth index this order won’t change. Why? Because jth element is the smallest element which
#      is greater than the ith element; i.e. P[j-1] < P[i] < P[j]. Therefore, the resulting sequence (from (i+1)th element to end) is still sorted which means that 
#      in order to sort it in ascending order, we can just reverse it.

# Time Complexity

# O(N), where ‘N’ is the length of the given permutation.

 

# Since in the worst case we will traverse the whole permutation twice. So, the overall time complexity will be O(N).
# Space Complexity

# O(1).

 
def nextPermutation(perm, n):
    # Write your code here.
    # Return a list.
    i = n-2 # [3, 4, 1, 2] , [1 5 2 4  3]
    while i >= 0 and perm[i] >= perm[i+1]: # find the element till which there is decreasing order
        i-=1
    if i >= 0:
        j = n-1
        while perm[i] >= perm[j]: # find first ele which is greater than i and swap with it this will always be ther else i will be 0
            j-=1
        perm[i] , perm[j] = perm[j] , perm[i] # swap it [3, 4, 1, 2] -> [3, 4, 2, 1] i = 2 , j = 3 ,***** [1 5 3 4  2] , i = 2 , j = 4
        x = i+1
        y = n-1
        while x < y : # reverse the array from i
            perm[x] , perm[y] = perm[y] , perm[x]# [1 5 3 2  4]
            x+=1
            y-=1
    else: # if all decreasing then reverse
        return perm[::-1]
            
    return perm # [1 5 3 2 4 ]