# Using Recursion

# Starting from the given pixel let's traverse the image using recursion.
# The idea is to replace the colour of the starting pixel with the new colour and repeat the same procedure for the adjacent same coloured pixels.
# During the traversal, we do not replace the colour of the current pixel if:
#     It has a different colour than the starting pixel.
#     Or if it has already been replaced with a new colour.
# In this way, we generate a new image.
# This approach is the same as applying DFS on the given image.


# Algorithm:

# Start with the given pixel.
# Base Condition 1: If the pixel has a different color than the starting pixel, return.
# Base Condition 2: If the pixel has already been replaced with the new color, return.
# Replace the colour of the current pixel with the new colour.
# Recur for the adjacent pixels (up, down, left and right).
# Return the new image.

# Time Complexity

# O(M * N) per test case, where M and N are the number of rows and columns in the image, respectively.

 

# In the worst case, we will be traversing the complete image. Hence, the overall time complexity is O(M * N)
# Space Complexity

# O(M * N) per test case, where M and N are the number of rows and columns in the image, respectively.

# In the worst case, O(M * N) extra space is required by the recursion stack. 
# Hence the overall space complexity is O(M * N).

'''
	Time complexity: O(M * N)
	Space Complexity: O(M * N)
	
	Where M and N are the number of rows and columns in the image, respectively.
'''

def floodFillHelper(image, i, j, oldColor, newColor):

    # Check if the current coordinates are valid or not.
    if (i < 0 or i >= len(image) or j < 0 or j >= len(image[0])):
        
        # Invalid coordinates. So, return.
        return

    if (image[i][j] != oldColor):

        # Current pixel has a different colour than starting pixel.
        return

    if (image[i][j] == newColor):

        # Current pixel has already been visited.
        return

    # Replace the colour of current pixel.
    image[i][j] = newColor

    # Recur for adjacent pixels.
    floodFillHelper(image, i, j + 1, oldColor, newColor)
    floodFillHelper(image, i, j - 1, oldColor, newColor)
    floodFillHelper(image, i + 1, j, oldColor, newColor)
    floodFillHelper(image, i - 1, j, oldColor, newColor)

def floodFill(image, x, y, newColor):
    oldColor = image[x][y]
    floodFillHelper(image, x, y, oldColor, newColor)
    return image


#######################################################################################
# Contributed By

# Using BFS

# This approach is similar to the previous one but instead of using recursion/DFS, we use BFS to traverse the image.
# Algorithm:

# Create an empty queue that can hold coordinates of the pixel.
# Initialize the queue by pushing the starting coordinates.
# Repeat the following steps until the queue becomes empty:
#     Pop the top coordinates from the queue. This will be the current pixel which we will be exploring.
#     If the current pixel has not been colored, then change its color to the new color and push the adjacent pixels (up, down, left, and right) into the queue.
# When the queue becomes empty, we have changed the color of all the required pixels. Hence, return the new image.

# Time Complexity

# O(M * N) per test case, where M and N are the number of rows and columns in the image, respectively.

# In the worst case, we will be traversing the complete image. Hence, the overall time complexity is O(M * N)
# Space Complexity

# O(M * N) per test case, where M and N are the number of rows and columns in the image, respectively.

# In the worst case, O(M * N) extra space is required by the queue. Hence the overall space complexity is O(M * N).

'''
	Time complexity: O(M * N)
	Space Complexity: O(M * N)
	
	Where M and N are the number of rows and columns in the image, respectively.
'''

from collections import deque 

def floodFill(image, x, y, newColor):

    oldColor = image[x][y]

    # Number of rows.
    m = len(image)

    # Number of columns.
    n = len(image[0])

    # Queue to hold the coordinates of the pixels.
    q=deque([])

    q.append((x, y))

    while (len(q)>0):

        currentPixel = q.popleft()

        # i and j represent the row and column of the current pixel.
        i = currentPixel[0]
        j = currentPixel[1]

        # Check if the current coordinates are valid.
        if (i >= 0 and i < m and j >= 0 and j < n):

            # Now, check if the current pixel has been colored or not.
            if (image[i][j] == oldColor and image[i][j] != newColor):
                
                # So, replace the old colour.
                image[i][j] = newColor

                # Push the adjacent pixels into the queue.
                q.append((i, j + 1))
                q.append((i, j - 1))
                q.append((i + 1, j))
                q.append((i - 1, j))

    return image