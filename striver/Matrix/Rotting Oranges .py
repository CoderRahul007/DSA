''' 
    Time Complexity - O(N * M * max(N, M))
    Space Complexity - O(1)

    where N and M are the number of rows and columns of
    the grid respectively.
'''

def isValid(i, j, n, m):
    return i >= 0 and i < n and j >= 0 and j < m


def minTimeToRot(grid, n, m):

    # Variables for tracking currently rotten orange and time elapsed.
    rotten, time = 2, 0

    # List for exploring all 4 directions.
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # Check till we process all rotten oranges.
    while(True):

        # Variable to check if a rotten orange is there to process.
        notFound = True

        # Iterate through all cells
        for i in range(n):
            for j in range(m):

                # If we get current rotten orange.
                if(grid[i][j] == rotten):

                    notFound = False

                    # Check all adjacent cells and rot them, if valid.
                    # Assign them different value (currRottenNum + 1).
                    for k in range(4):

                        nextI = i + dx[k]
                        nextJ = j + dy[k]

                        if(isValid(nextI, nextJ, n, m) and grid[nextI][nextJ] == 1):
                            grid[nextI][nextJ] = rotten + 1

        # If no rotten oranges is present to process, break.
        if(notFound):
            break
        # Else, increment to check next rotten oranges.
        rotten += 1
        time += 1

    # If a fresh orange is still present, return -1.
    for i in range(n):
        for j in range(m):

            #   If left
            if(grid[i][j] == 1):
                return -1

    # Return time elapsed.
    return max(0, time - 1)


###############################################################################################
''' 
    Time Complexity - O(N * M)
    Space Complexity - O(N * M)

    where N and M are the number of rows and columns of
    the grid respectively.
'''

from queue import Queue


def isValid(visited, i, j, n, m):
    return i >= 0 and i < n and j >= 0 and j < m and visited[i][j] == False

def minTimeToRot(grid, n, m):

    time = 0

    # 2D array to mark visited cells.
    visited = [[False for i in range(m)] for j in range(n)]

    # Queue for BFS.
    Q = Queue()

    # Push all the rotten oranges into the queue as level 0.
    for i in range(n):
        for j in range(m):

            if(grid[i][j] == 2):
                Q.put((i, j))
                visited[i][j] = True

    # List for exploring all 4 directions.
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # Search till queue is not empty.
    while (Q.qsize() > 0): # after addition of new cells it will fetch that in next iter

        levelSize = Q.qsize()

        while(levelSize > 0): # present iter
            levelSize -= 1
            (i, j) = Q.get()

            # Check all adjacent cells and push them in queue, if fresh and valid.
            for k in range(4):
                nextI = i+dx[k]
                nextJ = j+dy[k]

                if(isValid(visited, nextI, nextJ, n, m) and grid[nextI][nextJ] == 1):
                    Q.put((nextI, nextJ))
                    visited[nextI][nextJ] = True

        # Increment time for next level.
        time += 1

    # If a fresh orange is still present, return -1.
    for i in range(n):
        for j in range(m):

            if(grid[i][j] == 1 and visited[i][j] == False):
                return -1

    #   Return time elapsed.
    return max(0, time - 1)
