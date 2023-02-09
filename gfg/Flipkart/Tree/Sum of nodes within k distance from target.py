# Given a binary tree, a target node and a positive integer K on it, 
#  the task is to find the sum of all nodes within distance K from the 
# target node (including the value of the target node in the sum).

# Examples:

#     Input: target = 9, K = 1,  
#     Binary Tree =             1
#                                     /  \
#                                  2     9
#                                /      /   \
#                             4      5     7
#                           /  \           /  \
#                        8    19      20   11
#                      /      /   \
#                  30     40   50
#     Output: 22
#     Explanation: Nodes within distance 1 from 9 is 9 + 5 + 7 + 1 = 22

#     Input: target = 40,  K = 2,  
#     Binary Tree =             1
#                                     /  \
#                                  2     9
#                                /      /   \
#                             4      5     7
#                           /  \           /  \
#                        8    19      20   11
#                      /      /   \
#                  30     40   50
#     Output: 113
#     Explanation: Nodes within distance 2 from 40 is
#     40 + 19 + 50 + 4 = 113

 

# Approach: This problem can be solved using hashing and Depth-First-Search based on the following idea:

#     Use a data structure to store the parent of each node. Now utilise that data structure to perform a DFS traversal from target and calculate the sum of all the nodes within K distance from that node.

# Follow the steps mentioned below to implement the approach:

#     Create a hash table (say par)to store the parent of each node.
#     Perform a DFS and store the parent of each node.
#     Now find the target in the tree.
#     Create a hash table to mark the visited nodes.
#     Start a DFS from target:
#         If the distance is not K, add the value in the final sum.
#         If the node is not visited then continue the DFS traversal for its neighbours also (i.e. parent and child) with the help of par and the links of each node.
#         Return the sum of its neighbours while the recursion for the current node is complete
#     Return the sum of all the nodes within K distance from the target.

# Below is the implementation of the above approach:


# import java.util.*;

# public class Main {
# 	// Structure of a tree node
# 	static class Node {
# 		int data;
# 		Node left;
# 		Node right;
# 		Node(int val)
# 		{
# 			this.data = val;
# 			this.left = null;
# 			this.right = null;
# 		}
# 	}

# 	// Function for marking the parent node
# 	// for all the nodes using DFS
# 	static void dfs(Node root,
# 			HashMap <Node, Node> par)
# 	{
# 		if (root == null)
# 			return;
# 		if (root.left != null)
# 			par.put( root.left, root);
# 		if (root.right != null)
# 			par.put( root.right, root);
# 		dfs(root.left, par);
# 		dfs(root.right, par);
# 	}
# 	static int sum;
# 	// Function calling for finding the sum
# 	static void dfs3(Node root, int h, int k,
# 			HashMap <Node, Integer> vis,
# 			HashMap <Node, Node> par)
# 	{
# 		if (h == k + 1)
# 			return;
# 		if (root == null)
# 			return;
# 		if (vis.containsKey(root))
# 			return;
# 		sum += root.data;
# 		vis.put(root, 1);
# 		dfs3(root.left, h + 1, k, vis, par);
# 		dfs3(root.right, h + 1, k, vis, par);
# 		dfs3(par.get(root), h + 1, k, vis, par);
# 	}
# 	// Function for finding
# 	// the target node in the tree
# 	static Node dfs2(Node root, int target)
# 	{
# 		if (root == null)
# 			return null;
# 		if (root.data == target)
# 			return root;
# 		Node node1 = dfs2(root.left, target);
# 		Node node2 = dfs2(root.right, target);
# 		if (node1 != null)
# 			return node1;
# 		if (node2 != null)
# 			return node2;
# 		return null;
# 	}

# 	static int sum_at_distK(Node root, int target,
# 				int k)
# 	{
# 		// Hash Map to store
# 		// the parent of a node
# 		HashMap <Node, Node> par = new HashMap<>();

# 		// Make the parent of root node as NULL
# 		// since it does not have any parent
# 		par.put(root, null);

# 		// Mark the parent node for all the
# 		// nodes using DFS
# 		dfs(root, par);

# 		// Find the target node in the tree
# 		Node node = dfs2(root, target);

# 		// Hash Map to mark
# 		// the visited nodes
# 		HashMap <Node, Integer> vis = new HashMap<>();

# 		sum = 0;

# 		// DFS call to find the sum
# 		dfs3(node, 0, k, vis, par);
# 		return sum;
# 	}



# 	public static void main(String args[]) {
# 		// Taking Input
# 		Node root = new Node(1);
# 		root.left = new Node(2);
# 		root.right = new Node(9);
# 		root.left.left = new Node(4);
# 		root.right.left = new Node(5);
# 		root.right.right = new Node(7);
# 		root.left.left.left = new Node(8);
# 		root.left.left.right = new Node(19);
# 		root.right.right.left = new Node(20);
# 		root.right.right.right
# 			= new Node(11);
# 		root.left.left.left.left
# 			= new Node(30);
# 		root.left.left.right.left
# 			= new Node(40);
# 		root.left.left.right.right
# 			= new Node(50);

# 		int target = 9, K = 1;

# 		// Function call
# 		System.out.println( sum_at_distK(root, target, K) );
		
# 	}
# }


######################################
# ANother solution
class Solution:
    def sum_at_distK(self,root, target, k):
        # code here
        self.targetNode = None
        childToParent = {}
        def makeparent(root , target):
            if not root:
                return
            if root.data == target:
                self.targetNode = root
            if root.left :
                childToParent[root.left] =  root
            if root.right:
                childToParent[root.right] = root
                
            makeparent(root.left , target)
            makeparent(root.right , target)
        
        makeparent(root , target)   

        q = [self.targetNode]
        vis = set()
        res = 0
        while len(q) > 0 and k >= 0:
            n = len(q)
            while n > 0:
                temp = q.pop(0)
                if temp in vis:
                    n-=1
                    continue
                vis.add(temp)
                res += temp.data
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                if temp in childToParent :
                    q.append(childToParent[temp])
                n-=1
            k-=1
        return res