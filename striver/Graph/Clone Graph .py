# BFS Graph Traversal

# To clone a graph, we will need to traverse it. The approach here is to use BFS graph traversal.
#  To clone a graph, you need to have a copy of each node and you need to avoid copying the same 
#  node multiple times. So we need a mapping from an original node to its copy.

 

# The steps are as follows :
 

# We need to keep track of the visited/cloned nodes to avoid making multiple copies of the same node.
#  Hence, a HashMap is required in order to maintain all the nodes which have already been created.
#  Where in the HashMap the key stores the address of the original node and the value stores the address 
# of the cloned node.
# Now in order to reach each node and its neighbours, we are creating a queue for BFS traversal 
# and a HashMap which keeps a track of all the nodes which are already created.
# Create a new node corresponding to the given reference node and insert that node in the HashMap 
# which marks it as visited.
# Push the given reference node into a queue and now keep repeating the below steps until the queue isn’t empty.
# Get the front node and pop it from the queue and visit all its neighbours, now check if a new 
# cloned node has already been created for each neighbouring node (check it in the HashMap).
# If it wasn’t created, then create a new clone node corresponding to the neighbour node and insert
#  it into the HashMap and also push this node into the queue.
# Now add the cloned neighbours to “neighbours” list of the cloned node.
# Ultimately when the queue is empty, return the source node of the cloned graph.

# Time Complexity

# O(N + M), where ‘N’ is the number of nodes and ‘M’ is the number of edges.

# In order to clone a graph, we visit each node and traverse each edge exactly once.
#  The Breadth-First Search traversal takes O(N+M) time. Push and pop operations 
#  in a queue take constant time. Thus, the overall time complexity will be O(N+M).
# Space Complexity

# O(N), where ‘N’ is the number of nodes.

'''
    Time Complexity: O(N + M)
    Space Complexity: O(N)
    
    Where N is the number of nodes 
    and M is the number of edges in the given graph.
'''

from queue import Queue

# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def cloneGraphHelper(node, copies):

    if (node == None):
        return None

    # Create a graph node which denotes the node of the cloned graph.
    copy = graphNode(node.data)

    # Update the dictionary.
    copies[node] = copy

    # Queue used for BFS.
    level = Queue()

    # Push the source node.
    level.put(node)

    while(not level.empty()):
        
        # Take the front element from the queue.
        cur = level.get()

        # Go through all the neighbours.
        for neighbor in cur.neighbours:

            # If it is not present in dictionary.
            if neighbor not in copies:
                copies[neighbor] = graphNode(neighbor.data)
                level.put(neighbor)

            copies[cur].neighbours.append(copies[neighbor])

    return copy


def cloneGraph(node):
    
    # Create a dictionary.
    copies = {}

    # Return the source node of the cloned graph.
    return cloneGraphHelper(node, copies)


###################################################################################################################

#  DFS Graph Traversal

# To clone a graph, we will need to traverse it. The approach here is to use DFS graph traversal.
#  To clone a graph, you need to have a copy of each node and you need to avoid copying the same 
#  node multiple times. So we need a mapping from an original node to its copy.

 

# Steps are as follows:

# The algorithm starts at a given reference node in the given graph and explores as far as possible 
# along each branch of the current node before backtracking.
# Now to keep the track of the visited/cloned nodes, a HashMap is required in order to maintain all
#  the nodes which have already been created. Where in the HashMap the key stores the address of the
#  original node and the value stores the address of the cloned node.
# The idea is to start from the starting node and mark the node and move to the adjacent unmarked node
#  and continue this recursively until there is no unmarked adjacent node.
# Then backtrack and check for other unmarked nodes and traverse them.
# Create a recursive function that takes a node and the Hashmap which contains the copies of the nodes as arguments.
# Mark the current node as visited and create a new node for the cloned graph and insert the new node into the HashMap.
# Traverse all the adjacent nodes of the current node and for all unmarked nodes call the recursive function with the 
# index of adjacent nodes.
# After visiting all neighbouring nodes, insert all the cloned neighbouring nodes into the neighbouring array/list 
# of the current node.

 
# Time Complexity

# O(N + M), where ‘N’ is the number of nodes and ‘M’ is the number of edges.

# In order to clone a graph of nodes, we visit each node and the edges as well
# and the Depth First Search traversal takes O(N + M) time so the overall time complexity will be O(N + M).
# Space Complexity

# O(N), where ‘N’ is the number of nodes.


'''
    Time Complexity: O(N + M)
    Space Complexity: O(N)

    Where N is the number of nodes
    and M is the number of edges in the given graph.
'''

# Class for graph node is as follows:
class graphNode:
    def __init__(self, *args):
        if(len(args) == 0):
            self.data = 0
            self.neighbours = []

        elif(len(args) == 1):
            self.data = args[0]
            self.neighbours = []

        elif(len(args) == 2):
            self.data = args[0]
            self.neighbours = args[1]

    def __del__(self):
        self.neighbours.clear()


def cloneGraphHelper(node, copies):

    if (node == None):
        return None

    # If dictionary doesn't contain the node.
    if node not in copies:

        copies[node] = graphNode(node.data)

        # Go through all the neighbours.
        for neighbor in node.neighbours:
            copies[node].neighbours.append(cloneGraphHelper(neighbor, copies))

    return copies[node]


def cloneGraph(node):

    # Create a dictionary.
    copies = {}

    # Return the source node of the cloned graph.
    ans = cloneGraphHelper(node, copies)

    n = len(copies)
    sum = 0
    for i in range(5 * n):
        sum += i
    # node.data = sum

    return ans
