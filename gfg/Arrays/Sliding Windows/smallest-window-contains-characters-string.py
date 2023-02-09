# Python program to find the smallest
# window containing
# all characters of a pattern
from collections import defaultdict

MAX_CHARS = 256

# Function to find smallest window
# containing all distinct characters


def findSubString(strr):

	n = len(strr)

	# if string is empty or having one char
	if n <= 1:
		return strr

	# Count all distinct characters.
	dist_count = len(set([x for x in strr]))

	curr_count = defaultdict(lambda: 0)
	count = 0
	start = 0
	min_len = n

	# Now follow the algorithm discussed in below
	# post. We basically maintain a window of characters
	# that contains all characters of given string.
	for j in range(n):
		curr_count[strr[j]] += 1

		# If any distinct character matched,
		# then increment count
		if curr_count[strr[j]] == 1:
			count += 1

		# Try to minimize the window i.e., check if
		# any character is occurring more no. of times
		# than its occurrence in pattern, if yes
		# then remove it from starting and also remove
		# the useless characters.
		if count == dist_count:
			while curr_count[strr[start]] > 1:
				curr_count[strr[start]] -= 1					
				start += 1

			# Update window size
			len_window = j - start + 1

			if min_len > len_window:
				min_len = len_window
				start_index = start

	# Return substring starting from start_index
	# and length min_len """
	return str(strr[start_index: start_index +
					min_len])


# Driver code
if __name__ == '__main__':

	print("Smallest window containing "
		"all distinct characters is: {}".format(
			findSubString("aabcbcdbca")))

# Maintain an array (visited) of maximum possible characters (256 characters) and as soon as we find any in the string, mark that index in the array (this is to count all distinct characters in the string).
# Take two pointers start and end which will mark the start and end of window.
# Take a counter=0 which will be used to count distinct characters in the window.
# Now start reading the characters of the given string and if we come across a character which has not been visited yet increment the counter by 1.
# If the counter is equal to total number of distinct characters, Try to shrink the window.
# For shrinking the window -: 
#     If the frequency of character at start pointer is greater than 1 increment the pointer as it is redundant.
#     Now compare the length of present window with the minimum window length.


# Naive Approach

# Python3 code for the same approach
import sys

MAX_CHARS = 256

# Function to find smallest window containing
# all distinct characters
def findSubString(str):

    n = len(str)

    # Count all distinct characters.
    dist_count = 0
    hash_map = {}
    for i in range(n):
        if(str[i] in hash_map):

            hash_map[str[i]] = hash_map[str[i]] + 1

        else:

            hash_map[str[i]] = 1

    dist_count = len(hash_map)
    size = sys.maxsize
    res = 0

        # Now follow the algorithm discussed in below
    for i in range(n):
        count = 0
        visited= [0]*(MAX_CHARS)
        sub_str = ""
        for j in range(i,n):
            if (visited[ord(str[j])] == 0):
                count += 1
                visited[ord(str[j])] = 1

            sub_str += str[j]
            if (count == dist_count):
                break
        if (len(sub_str) < size and count == dist_count):
            res = sub_str
            size = len(res)
    return res

# Driver Code
str = "aabcbcdbca"
print(f"Smallest window containing all distinct characters is: {findSubString(str)}")

# This code is contributed by shinjanpatra.
