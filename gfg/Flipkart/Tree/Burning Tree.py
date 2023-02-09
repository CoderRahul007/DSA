# Given a binary tree and a node called target.
#  Find the minimum time required to burn the complete binary 
# tree if the target is set on fire. It is known that in 1 second 
# all nodes connected to a given node get burned. That is its left child, right child, and parent.



# Example 1:

# Input:      
#           1
#         /   \
#       2      3
#     /  \      \
#    4    5      6
#        / \      \
#       7   8      9
#                    \
#                    10
# Target Node = 8
# Output: 7
# Explanation: If leaf with the value 
# 8 is set on fire. 
# After 1 sec: 5 is set on fire.
# After 2 sec: 2, 7 are set to fire.
# After 3 sec: 4, 1 are set to fire.
# After 4 sec: 3 is set to fire.
# After 5 sec: 6 is set to fire.
# After 6 sec: 9 is set to fire.
# After 7 sec: 10 is set to fire.
# It takes 7s to burn the complete tree.

# Example 2:

# Input:      
#           1
#         /   \
#       2      3
#     /  \      \
#    4    5      7
#   /    / 
#  8    10
# Target Node = 10
# Output: 5

############# Not working ###################
# 
# https://github.com/striver79/FreeKaTreeSeries/blob/main/L31_timeToBurnATreeJava
###################################33 STriver ####################################
# An easy to understand solution: 

 

# class Solution {
#  public:
#  Node* markParents(unordered_map<Node* , Node*>& parent_track,Node* root,int target){
#     Node* targetNode=NULL;
#      queue<Node*>q;
#      q.push(root);
#      parent_track[root]=NULL;
#      while(!q.empty()){
#          Node* current=q.front();
#          q.pop();
#          if(current->left){
#              parent_track[current->left]=current;
#          q.push(current->left);
#              }
#          if(current->right){
#              parent_track[current->right]=current;
#          q.push(current->right);
#          }
#          if(current->data==target){
#              targetNode=current;
#          }
#      }
#      return targetNode;
#  }
#  int findMaxDistance(unordered_map<Node* , Node*>&parent_track,Node* &targetNode){
#      queue<Node*>q;
#      q.push(targetNode);
#      map<Node*,bool>visited;
#      visited[targetNode]=true;
#      int maxi=0;
#      while(!q.empty())
#    {   int flag=0;
#      int size=q.size();
#      for(int i=0;i<size;i++)
# {
#     Node* current=q.front();
#     q.pop();
#     if(current->left && !visited[current->left]){
#         flag=1;
#         visited[current->left]=true;
#         q.push(current->left);
#     }
#      if(current->right && !visited[current->right]){
#         flag=1;
#         visited[current->right]=true;
#         q.push(current->right);
#     }
#      if(parent_track[current] && !visited[parent_track[current]]){
#         flag=1;
#         visited[parent_track[current]]=true;
#         q.push(parent_track[current]);
#     }
# }
# if(flag==1)maxi++;
#  }
#      return maxi;
#  }
 
#    int minTime(Node* root, int target) 
#    {
# unordered_map<Node* , Node*>parent_track;
# Node* targetNode=markParents(parent_track,root,target);
#    int maxi=findMaxDistance(parent_track,targetNode);
#    return maxi;
#    }
# };

####################################################################################
def buildParent(mp , target , root):
    q = [root]
    res = None
    while q:
        s = len(q)
        temp = q.pop(0)
        if temp.data == target:
            res = temp
        if temp.left :
            mp[temp.left] = temp
            q.append(temp.left)
        if temp.right:
            mp[temp.right] = temp
            q.append(temp.right)
    return res
    
def findMinTime(target , mp):
    
    vis = {}
    q = [target]
    time = 0
    vis[target] = True
    while q:
        s = len(q)
        temp = q.pop(0)
        flag = False
        while s:
            if temp.left and (not temp.left in vis or not vis[temp.left]):
                q.append(temp.left)
                vis[temp.left] = True
                flag = True
            if temp.right and (not temp.right in vis or not vis[temp.right]):
                q.append(temp.right)
                vis[temp.right] = True
                flag = True
            if temp in mp and (not mp[temp] in vis or not vis[mp[temp]]):
                q.append(mp[temp])
                vis[mp[temp]] = True
                flag = True                
                
            s-=1
        if flag:
            time+=1
    return time
    
class Solution:
    def minTime(self, root,target):
        # code here
        mp = {}
        t = buildParent(mp , target , root)
        maxi = findMinTime(t , mp)
        return maxi

###########################################
# from submission
from collections import defaultdict

class Solution:
    def __init__(self):
        self.neighbours = defaultdict(set)
   
    def get_neighbours(self, root):
        if root is None:
           return
        else:
            if root.left:
               self.neighbours[root.data].add(root.left.data)
               self.neighbours[root.left.data].add(root.data)
               self.get_neighbours(root.left)
            if root.right:
               self.neighbours[root.data].add(root.right.data)
               self.neighbours[root.right.data].add(root.data)
               self.get_neighbours(root.right)
    def minTime(self, root,target):
        # code here
           self.get_neighbours(root)
           if len(self.neighbours) < 1:
               return 0
           visited = {target}
           q = [target]
           steps = 0
           while len(visited) != len(self.neighbours):
               steps += 1
               new_queue = set()
               while len(q) != 0:
                   curr_neighbour = q.pop()
                   for new_neighbour in self.neighbours[curr_neighbour]:
                       if new_neighbour not in visited:
                           visited.add(new_neighbour)
                           new_queue.add(new_neighbour)
               q = new_queue
           return steps
##############################################
# From Docs

#  Using BFS

# The idea is to first create an undirected graph of the given binary tree and then doing a bfs traversal of the undirected graph starting from the start node. We will keep a variable ‘count’ that will be incremented at each level of bfs traversal. ‘count-1’ is the required time needed to burn the whole tree.

 

# Algorithm

 

#     Initialize an unordered map ‘M’ that maps from integer to array of integers that store the edges and vertices of an undirected graph formed.
#     Store the edges and vertices in ‘M’ using inorder traversal of the tree.
#     Run BFS traversal from the ‘start’ node and increment the ‘count’ variable at each iteration.
#     Return count - 1.

# Time Complexity

# O(N), where ‘N’ is the number of nodes in the tree.


# We are doing inorder traversal of the tree to store all the edges and vertices in ‘M’ that will take O(N) time. Then we are doing bfs traversal of the undirected graph formed that will take O(V+E) i.e O(N) time. So the overall time complexity is O(N).
# Space Complexity

# O(N), where ‘N’ is the number of nodes in the tree.

 

# In the undirected graph, there will be ‘N’ vertices and 2(N-1) edges. So the overall space complexity is O(N + 2(N-1) = O(N)
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    where N is the total number of nodes in the given tree.
'''
from sys import stdin,setrecursionlimit
from queue import Queue
from collections import deque
from collections import defaultdict

setrecursionlimit(10**7)

# Binary tree node class for reference 
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None


def inorder(root, m):

    if (root):
    
        inorder(root.left, m)
        if (root.left):
            
            
            m[root.data].append(root.left.data)
            m[root.left.data].append(root.data)
        
        if (root.right):
            
            m[root.data].append(root.right.data)
            m[root.right.data].append(root.data)
        
        inorder(root.right, m)
    


	
def timeToBurnTree(root, start):

    # Initialize map to store edges and vertices.
    m=defaultdict(list)
    
    # Store edges by doing inorder traversal.
    inorder(root, m)
    
    # Initialize queue for bfs traversal.
    q=deque()
    
    q.append(start)
    
    # Variable to keep count of number of levels from start node.
    count = 0
    visited=defaultdict(bool)
    visited[start] = True
    
    # Iterate while queue is not empty.
    while (q):
    
        count+=1
        n=len(q)
        for i in range(n):
        
            node = q[0]
            q.popleft()
            
            for j in m[node]:
            
                if(visited[j]==None or visited[j]==False):
                
                    q.append(j)
                    visited[j]=True
                
            
        
    
    
    return count - 1
        
    


# Fast input
def takeInput() :
	
    arr = list(map(int, stdin.readline().strip().split(" ")))

    rootData = arr[0]

    n = len(arr)

    if(rootData == -1) :
        start = int(input().strip())
        return None, start

    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        
        leftChild = arr[index]
        
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        
        index += 1
        rightChild = arr[index]
        
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  

        index += 1

    start = int(input().strip())

    return root, start


root, start = takeInput()

print(timeToBurnTree(root, start))        