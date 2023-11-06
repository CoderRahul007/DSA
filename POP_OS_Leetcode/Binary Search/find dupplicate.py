# First of all, where does the cycle come from? Let's use the function f(x) = nums[x] to construct the sequence:
#  x, nums[x], nums[nums[x]], nums[nums[nums[x]]], ....

# Each new element in the sequence is an element in nums at the index of the previous element.

# If one starts from x = nums[0], such a sequence will produce a linked list with a cycle.

#     The cycle appears because nums contains duplicates. The duplicate node is a cycle entrance.
# Floyd's algorithm consists of two phases and uses two pointers, usually called tortoise and hare.

# In phase 1, hare = nums[nums[hare]] is twice as fast as tortoise = nums[tortoise].
#  Since the hare goes fast, it would be the first one who enters the cycle and starts to run around the cycle. 
# At some point, the tortoise enters the cycle as well, and since it's moving slower the hare catches 
# the tortoise up at some intersection point. Now phase 1 is over, and the tortoise has lost.

#     Note that the intersection point is not the cycle entrance in the general case.
# To compute the intersection point, let's note that the hare has traversed twice as many nodes as the tortoise,
#  i.e. 2d(tortoise)=d(hare)2d(\text{tortoise}) = d(\text{hare})2d(tortoise)=d(hare), that means

# 2(F+a)=F+nC+a2(F + a) = F + nC + a2(F+a)=F+nC+a, where nnn is some integer.

#     Hence the coordinate of the intersection point is F+a=nCF + a = nCF+a=nC.

# In phase 2, we give the tortoise a second chance by slowing down the hare,
#  so that it now moves with the speed of tortoise: tortoise = nums[tortoise], hare = nums[hare].
#  The tortoise is back at the starting position, and the hare starts from the intersection point.

# pic
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tort=nums[0]
        hare=nums[0]
        while True:
            tort=nums[tort]
            hare=nums[nums[hare]]
            if tort==hare:
                break
        tort=nums[0]
        while tort!=hare:
            tort=nums[tort]
            hare=nums[hare]
        return tort
        
        
        
        