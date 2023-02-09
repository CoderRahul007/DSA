class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        if not root :
            return root
        
        if root.data == n1 or root.data == n2:
            return root
        l = self.lca(root.left , n1 , n2)
        r = self.lca(root.right , n1 , n2)
        
        if l and r:
            return root
        elif l:
            return l
        else:
            return r

#LUCID EXPLAINATION

# The question is simply asking to find the subtree's root which will contain both n1 and n2, right?! So we do the same,



# Well, if there is no root, you gotta return null/root. if(root==nullptr) { return root; }  
# if your root data contains either n1 or n2, you return that root. 
# WHY?? because it will be used in calculation of two different answer A.K.A. left and right side of tree.
# Now save your Left answer of the left side of tree in a variable, 
# this variable with either have a null or a valid node depending on 
# recursive calls if it finds the required node, Do the same for the Right side make a variable and save the answer.
# Now, we have two different variables namely left and right. 
# Both contains answer either null or a valid node, now we check three conditions
# If Left answer is not null and right answer is also not null,
#  then the answer is the root itself, since left and right are 
# subtrees of the root and if both are not null it clearly means the values 
# n1 and n2 lies in right as well as left side, For example, Example test case 1 is the perfect example for this case
# If left answer is not null but right answer is null, then it means 
# both n1 and n2 lies on the left side of tree inside the subtree with
#  root as left answer, return left answer. For example, Example test case 2 is the perfect example for this case
# If right answer is not null but left answer is null, then it means both
#  n1 and n2 lies on the right side of tree inside the subtree with root as right answer, return right answer.

