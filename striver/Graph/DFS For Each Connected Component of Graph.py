
# DFS For Each Connected Component

#     Run a loop from 0 to V-1 and if this vertex is not visited do a DFS from this vertex and add all
#      the reachable vertex to a vector/list ‘singleComponent’.
#     Sort the singleComponent vector/list in increasing order and add it to the answer vector/list 
#     which is called ‘components’.
#     Print the size of the vector/list ‘components’ on the first line.
#     On each line after the first, print one single component from the vector/list ‘components’.

# Time Complexity

# O(VLogV + E), Where V is the number of vertices and E is the number of edges in the graph.

 

# The time complexity of a DFS is O(V+E) and we are sorting every component which would
#  be VlogV so overall complexity is O(V+E+VlogV) which is O(VlogV+E).
# Space Complexity

# O(V+E), Where V is the number of vertices and E is the number of edges in the graph.

# To store the graph in the adjacency list.


"""
    Time complexity : O(Vlog(V) + E )
    Space complexity : O(V+E)
    where V is the number of vertex and E is the number of edges in graph

"""


def depthFirstSearchHelper(vertex, visited, singleComponent, gra):
    visited[vertex] = True
    singleComponent.append(vertex)

    for child in gra[vertex]:

        # Check if the node is visited before or not.
        if visited[child] == False:
            depthFirstSearchHelper(child, visited, singleComponent, gra)


def depthFirstSearch(V, E, edges):

    # Creating Adjacency Matrix.
    gra = [[] for i in range(V + 1)]
    for a, b in edges:
        gra[a].append(b)
        gra[b].append(a)

    components = []
    visited = [False for i in range(V + 1)]

    for vertex in range(V):

        if visited[vertex] == False:
            singleComponent = []
            depthFirstSearchHelper(vertex, visited, singleComponent, gra)
            singleComponent.sort()
            components.append(singleComponent)

    return components
