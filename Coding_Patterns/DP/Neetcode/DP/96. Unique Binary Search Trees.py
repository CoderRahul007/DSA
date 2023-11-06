# Given an integer n, return the number of structurally unique BST's 
# (binary search trees) which has exactly n nodes of unique values from 1 to n.

class Solution:
    def numTrees(self, n: int) -> int:
        numTree = [1]*(n+1)
        # numTree[0] = 1
        # numTree[1] = 1
        for node in range(2 , n+1):
            total = 0
            for root in range(1 , node + 1 ):
                left = root - 1
                right =  node - root
                total += numTree[left] * numTree[right]
            numTree[node] = total
        return numTree[n]

#O(n**2)
#O(n)
# for each numbber of nodes we have to calculate number of bst by considering each node as root
# 1 ,2 , 3 ,4
# first consider 1 as root and left as 0 node and right as 2 , 3 ,4
# similarily for 2 and 3 and 4
# base case is for 0 and 1 node we will have only 1 bst
