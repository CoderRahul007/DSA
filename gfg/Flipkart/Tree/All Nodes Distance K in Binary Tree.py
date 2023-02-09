# The idea is simple:

# DFS and add reference to parent for each node
# Create empty Set of already visited Nodes and an empty result List
# DFS with increasing depth-counter going from target in directions 
# of parent, left and right node if present and not already visited
# Add to visited Set and also to result List if depth counter equals k
# Return result List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def dfs_add_parent(self, node: TreeNode, parent: Optional[TreeNode] = None):
        node.parent = parent
        if node.right:
            self.dfs_add_parent(node.right, node)
        if node.left:
            self.dfs_add_parent(node.left, node)
            
        
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
            self.dfs_add_parent(root)
            found_k_dist = []
            visited = set()
            def dfs_get_distance(node: TreeNode, current: int):
                visited.add(node)
                if current == k:
                    found_k_dist.append(node.val)
                    return
                for neighbor in [node.parent, node.left, node.right]:
                    if neighbor and neighbor not in visited:
                        dfs_get_distance(neighbor, current + 1)
                        
            dfs_get_distance(target, 0)
            
            return found_k_dist

####################################################
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
		# get the path to the target node
        def traverse(root: TreeNode, path: [TreeNode]) -> [TreeNode]:
            if not root:
                return None
            if root == target:
                return path + [root]
            return traverse(root.left, path + [root]) or traverse(root.right, path + [root])
        
        stack = traverse(root, [])
        res = []
        
		# get the nodes has the distance k to the `start node` and without passing through  `exclude node`
        def gets(start: TreeNode, exclude: TreeNode, k: int) -> [TreeNode]:
            queue = [start]
            for i in range(k):
                nexts = []
                for node in queue:
                    if node.left and node.left is not exclude:
                        nexts.append(node.left)
                    if node.right and node.right is not exclude:
                        nexts.append(node.right)
                queue = nexts
            return queue
        
        res, prev = [], None
        while K > -1 and stack:
            cur = stack.pop()
            res += gets(cur, prev, K)
            K -= 1
            prev = cur

        return [item.val for item in res]
##########################################################################
class Solution:
    def find_node(self, root, target, path):
        if root is None:
            return False
        path.append(root)
        if root.data == target:
            return True
        if self.find_node(root.left, target, path) or self.find_node(root.right, target, path):
            return True
        path.pop()
        return False
    def find_distance_node(self, node, dist, res):
        if node is None:
            return
        if dist < 0:
            return
        if dist == 0:
            res.append(node.data)
            return
        self.find_distance_node(node.left, dist-1, res)
        self.find_distance_node(node.right, dist-1, res)
        
    def KDistanceNodes(self,root,target,k):
        path = []
        self.find_node(root, target, path)
        res = []
        if len(path) == 1:
            self.find_distance_node(path[0], k, res)
        else:
            self.find_distance_node(path[-1], k, res)
            
            curr = path.pop()
            k = k -1
            while k > 0 and len(path) > 0:
                if path[-1].right == curr:
                    self.find_distance_node(path[-1].left, k-1, res)
                elif path[-1].left == curr:
                    self.find_distance_node(path[-1].right, k-1, res)
                curr = path.pop()
                k = k - 1
            if len(path) > 0:
                res.append(path[-1].data)
 
                
        return sorted(res)        
##########################################################################
# https://www.youtube.com/watch?v=B89In5BctFA
# Simple One
# import java.io.*;
# import java.util.*;

# class TreeNode {
# 	public int val;
# 	public TreeNode left;
# 	public TreeNode right;
# 	public TreeNode() {}

# 	public TreeNode(int val) { this.val = val; }
# }

# class GFG {
# 	List<TreeNode> path = null;
# 	//Finding all the nodes at a distance K from target
# 	//node.
# 	public List<Integer> distanceK(TreeNode root,
# 								TreeNode target, int K)
# 	{
# 		path = new ArrayList<>();
# 		findPath(root, target);
# 		List<Integer> result = new ArrayList<>();
# 		for (int i = 0; i < path.size(); i++) {
# 			findKDistanceFromNode(
# 				path.get(i), K - i, result,
# 				i == 0 ? null : path.get(i - 1));
# 		}
# 		//Returning list of all nodes at a distance K
# 		return result;
# 	}

# 	// Blocker is used for ancestors node if target at
# 	//left then we have to go in right or if target at
# 	// right then we have to go in left.
# 	public void findKDistanceFromNode(TreeNode node,
# 									int dist,
# 									List<Integer> result,
# 									TreeNode blocker)
# 	{
# 		if (dist < 0 || node == null
# 			|| (blocker != null && node == blocker)) {
# 			return;
# 		}

# 		if (dist == 0) {
# 			result.add(node.val);
# 		}

# 		findKDistanceFromNode(node.left, dist - 1, result,
# 							blocker);
# 		findKDistanceFromNode(node.right, dist - 1, result,
# 							blocker);
# 	}
# 	//Finding the path of target node from root node
# 	public boolean findPath(TreeNode node, TreeNode target)
# 	{
# 		if (node == null)
# 			return false;

# 		if (node == target || findPath(node.left, target)
# 			|| findPath(node.right, target)) {
# 			path.add(node);
# 			return true;
# 		}

# 		return false;
# 	}
# 	// Driver program to test the above functions
# 	public static void main(String[] args)
# 	{
# 		GFG gfg = new GFG();
# 		/* Let us construct the tree shown in above diagram */
# 		TreeNode root = new TreeNode(20);
# 		root.left = new TreeNode(8);
# 		root.right = new TreeNode(22);
# 		root.left.left = new TreeNode(4);
# 		root.left.right = new TreeNode(12);
# 		root.left.right.left = new TreeNode(10);
# 		root.left.right.right = new TreeNode(14);
# 		TreeNode target = root.left.right;
# 		System.out.println(gfg.distanceK(root, target, 2));
# 	}
# }
        