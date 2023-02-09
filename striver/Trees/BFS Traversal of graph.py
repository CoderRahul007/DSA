''' 
	Time complexity: O(V + E). 
	Space complexity: O(V^2). 

	Where V is the number of vertices in the input graph and 
    E is the number of edges in the input graph.
'''

# List for keeping track of the final BFS traversal.
result = [] 

def printBFSHelper(edges, source, visited):

    # A queue for visiting each vertex in the graph.
    queue = []
    # Marking source vertex as already visited.
    visited[source] = True
    queue.append(source)

    # While the queue has vertices to visit keep adding the other vertices 
    # in the queue which are connected by an edge.
    while len(queue) != 0:
        front = queue.pop(0)
        result.append(front)

        for i in range(len(edges)):

            if edges[front][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

# Function to change the edge matrix representation to 
# adjacency matrix representation of the given graph.
def createAdjMat(vertex, edges):

    adjacency_matrix = [[0] * vertex for _ in range(vertex)]

    for i in range(len(edges[0])):
        adjacency_matrix[edges[0][i]][edges[1][i]] = 1
        adjacency_matrix[edges[1][i]][edges[0][i]] = 1

    return adjacency_matrix


def BFS(vertex, edges):

    # Creating an adjacency matrix representation from the edges given.
    adjacency_matrix = createAdjMat(vertex, edges)
    # Initializing a list for keeping track of already visited vertices.
    visited = [False] * len(adjacency_matrix)

    for i in range(len(visited)):
        
        # Visit the vertex if it is not visited.
        if not visited[i]:
            printBFSHelper(adjacency_matrix, i, visited)

    return result
