# Given an infinite number line. You start at 0 and can go either to the left or to the right.
#  The condition is that in the ith move, youmust take i steps.
#  Given a destination D , find the minimum number of steps required to reach that destination.

# Example 1:

# Input: D = 2
# Output: 3
# Explaination: The steps takn are +1, -2 and +3.

# Example 2:

# Input: D = 10
# Output: 4
# Explaination: The steps are +1, +2, +3 and +4.

def helper(d , i ,  c):
    if i == d:
        return c
    if abs(i) > d:
        return float('inf')
    
    pos = helper(d , i+1+c , c+1)
    neg = helper(d , i-1-c , c+1)
    return min(pos , neg)
        
    
    
class Solution:
    def minSteps(self, D):
        # code here
        c = 0
        i = 0
        return helper(D , i  , c)


#######################################################################################

# If target is negative, we can take it as positive because we start from 0 in symmetrical way. 
# Idea is to move in one direction as long as possible, this will give minimum moves. 
# Starting at 0 first move takes us to 1, second move takes us to 3 (1+2) position, 
# third move takes us to 6 (1+2+3) position, ans so on; So for finding target we keep 
# on adding moves until we find the nth move such that 1+2+3+…+n>=target. Now if sum 
# (1+2+3+…+n) is equal to target the our job is done, i.e we’ll need n moves to reach 
# target. Now next case where sum is greater than target. Find the difference by how much
#  we are ahead, i.e sum – target. Let the difference be d = sum – target. 
# If we take the i-th move backward then the new sum will become (sum – 2i), i.e 1+2+3+…-x+x+1…+n.
#  Now if sum-2i = target then our job is done. Since, sum – target = 2i, i.e difference should be 
# even as we will get an integer i flipping which will give the answer. So following cases arise. 
# Case 1 : Difference is even then answer is n, (because we will always get a move flipping which will lead to target). 
# Case 2 : Difference is odd, then we take one more step, i.e add n+1 to sum and now again take the 
# difference. If difference is even the n+1 is the answer else we would have to take one more move 
# and this will certainly make the difference even then answer will be n+2.
# Explanation : Since difference is odd. Target is either odd or even. 
# case 1: n is even (1+2+3+…+n) then adding n+1 makes the difference even. 
# case 2: n is odd then adding n+1 doesn’t makes difference even so we would have to take one more move, so n+2.
# Example: 
# target = 5. 
# we keep on taking moves until we reach target or we just cross it. 
# sum = 1 + 2 + 3 = 6 > 5, step = 3. 
# Difference = 6 – 5 = 1. Since the difference is an odd value, we will not reach the target
#  by flipping any move from +i to -i. So we increase our step. We need to increase step by 2 
# to get an even difference (since n is odd and target is also odd). Now that we have an even 
# difference, we can simply switch any move to the left (i.e. change + to -) as long as the 
# summation of the changed value equals to half of the difference. We can switch 1 and 4 or 2 and 3 or 5. 
 


# https://www.youtube.com/watch?v=kz_0GjhFOzc
 
 
def reachTarget(target) :
 
    # Handling negatives by symmetry
    target = abs(target)
     
    # Keep moving while sum is
    # smaller or difference is odd.
    sum = 0
    step = 0
    while (sum < target or (sum - target) %
                                  2 != 0) :
        step = step + 1
        sum = sum + step
     
    return step
     
 
# Driver code
target = 5
print(reachTarget(target))
 