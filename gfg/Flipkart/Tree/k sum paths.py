# Given a binary tree and an integer K. Find the number of paths in the tree which have their sum equal to K.
# A path may start from any node and end at any node in the downward direction.


# Example 1:

# Input:      
# Tree = 
#           1                               
#         /   \                          
#        2     3
# K = 3
# Output: 2
# Explanation:
# Path 1 : 1 + 2 = 3
# Path 2 : only leaf node 3

# Example 2:

# Input: 
# Tree = 
#            1
#         /     \
#       3        -1
#     /   \     /   \
#    2     1   4     5                        
#         /   / \     \                    
#        1   1   2     6    
# K = 5                    
# Output: 8
# Explanation:
# The following paths sum to K.  
# 3 2 
# 3 1 1 
# 1 3 1 
# 4 1 
# 1 -1 4 1 
# -1 4 2 
# 5 
# 1 -1 5 

# class Solution{
#   public:
#     int mod = 1e9+7;
#     void dfs(Node *root, int k, unordered_map <long long,int> &mp, long long s, long long &c){
#         if(!root) return;
#         s += root->data;
#         mp[s]++;
#         if(s == k)
#             c = (c+1)%mod;
#         if(mp.find(s-k) != mp.end()){
#             c = (c+mp[s-k])%mod;
#             if(k == 0)
#                 c -= 1;
#         }
#         dfs(root->left , k, mp, s, c);
#         dfs(root->right, k, mp, s, c);
#         mp[s]--;
#     }
#     int sumK(Node *root,int k)
#     {
#        long long c = 0, s = 0;
#         unordered_map <long long,int> mp;
#         dfs(root, k, mp, s, c);
#         return c;
#     }
# };

# tc: O(N), sc: O(N)
# prefixsum2 - prefixsum1 == target ---> requirement, it means that a range sum equals to target  
# prefixsum2 - target == prefixsum1, ----> prefixsum2 is current sum, prefixsum1 is previous sum, I use hash map to save lookup time
# prefix sum is used to find the sum of path == target, and backtracking is used to update the info of hash map and current sum

class Solution:
    # 1. check whether root is valid
    # 2. update current sum
    # 3. use prefixsum2 - target == prefixsum1 to check how many paths whose sum equals to target
    # 4. traverse to left and right childs
    # 5. backtrack to root, update hash map and current sum

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        if not root: 
            return 0
        res = 0 # final output
        prefixSum = 0 # current sum
        prefixsum2num = {0:1} # to record how many paths whose sum equals to target

        def backtrack(root):
            if root == None:
                return
            nonlocal res, prefixSum, prefixsum2num
            prefixSum += root.val

            target = prefixSum - targetSum
            res += prefixsum2num.get(target, 0)
            prefixsum2num[prefixSum] = prefixsum2num.get(prefixSum, 0) + 1

            backtrack(root.left)
            backtrack(root.right)
            prefixsum2num[prefixSum] = prefixsum2num.get(prefixSum) - 1
            prefixSum -= root.val

        backtrack(root)
        return res

############################################################################
class Solution:
    def pathSum(self, root, target):
        self.result = 0
        
        self.lookup ={}
        
        # recursive to get result
        self.dfs(root, target, 0)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currSum):
        if not root:
            return None
        
        currSum = currSum+root.val
        
        if currSum == target :
            self.result+=1
            
        if (currSum-target) in self.lookup:
            self.result += self.lookup[currSum-target]
            
        if currSum in self.lookup:
            self.lookup[currSum] +=1
        else:
            self.lookup[currSum] = 1
        
        self.dfs(root.left, target, currSum)
        self.dfs(root.right, target, currSum)
        
        # Since path always has to be downwards and can't extend from left subtree to right subtree therefore, for every root node, the currentSum has to be decremented by 1.
        self.lookup[currSum] -=1