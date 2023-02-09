'''
    Time Complexity: O(N^2)
    Space Complexity: O(1)

    Where N is the length of the string
'''


def kDistinctChars(k, str):

    ans = 0

    for i in range(len(str)):

        # Create a set of unique characters
        uniqueChars = set()

        for j in range(i, len(str)):

            # Add characters in the set
            uniqueChars.add(str[j])

            # If set size is greater than K then we won't consider this substring
            if(len(uniqueChars) > k):
                break

            # Update the answer
            ans = max(ans, j - i + 1)

    return ans




##########################################################################################

'''
    Time Complexity: O(N)
    Space Complexity: O(1)

    Where N is the length of the string
'''

def kDistinctChars(k, str):

    # Initialise left and right pointers
    left = 0
    right = 0

    maxLength = 0

    # Initialise map of characters
    uniqueChars = {}


    # While the right pointers does not reach the end of the loop
    while(right < len(str)):

        # Add the right most character of the string in the  map
        rightCh = str[right]
        uniqueChars[rightCh] = uniqueChars[rightCh] + 1 if rightCh in uniqueChars else 1

        # If the set has move than k unique characters then start decreasing the window from left
        while(len(uniqueChars) > k):

            leftCh = str[left]

            # If leftCh is present in map decrease it
            if(leftCh in uniqueChars):
                uniqueChars[leftCh] -= 1

                # Remove the character from the map if it becomes 0
                if(uniqueChars[leftCh] == 0):
                    uniqueChars.pop(leftCh)

            # Decrease the sliding window from left side
            left += 1

        maxLength = max(maxLength, right - left + 1)

        # Increase the sliding window from the right
        right += 1

    return maxLength

