'''
    Time Complexity : O(Sum(A[i])*max(A[i])*log(N))
    Space Complexity : O(Sum(A[i]))

    where 'Sum(A[i])' is the sum of size of all words 'A[i]',
    'max(A[i])' is the maximum size of string in array 'A'.
    and 'N' is the size of array 'A'.
'''

from typing import *

def completeString(n: int, a: List[str])-> str:

    ans = ""

    mp = {}

    # Storing all strings in hashmap.
    for i in range(n):
        mp[a[i]] = 1
    

    for i in range(n):
        pre = ""
        flag = True

        # Traversing over all prefixes of the string 'a[i]'.
        for j in range(len(a[i])):

            pre += a[i][j]
            # If current prefix is not present in map, this string is invalid.
            if pre not in mp:
                flag = False
                break
            

        # Current string is a valid string.
        if flag:
            # If current string is longer than ans, we update it.
            if len(ans) < len(a[i]):
                ans = a[i]
            # If current string is of same size as 'ans', but lexicographically smaller, we update it.
            elif len(ans) == len(a[i]) and a[i] < ans:
                ans = a[i]
            
        
    

    # If there is no valid answer, we return "None".
    if len(ans) == 0:
      ans = "None"
    
    # Return the final result.
    return ans

######################################################################################
# Using Trie
'''
    Time Complexity : O(Sum(A[i]))
    Space Complexity : O(Sum(A[i]))

    where 'Sum(A[i])' is the sum of length of all words 'A[i]'.

'''

from typing import *

class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEnding = False

# Function to insert a string into trie.
def insert(word, root):

    node = root
    for c in word:
        i = ord(c) - ord('a')
        # If the next pointer is null for next character, allot the new memory.
        if node.children[i] == None:
            node.children[i] = TrieNode()
        
        node = node.children[i]
    
    # Mark the ending of word in trie.
    node.isEnding = True

# Function to check if this word has all prefixes in array.
def allPrefixed(word, root):
    node = root
    for c in word:
        i = ord(c) - ord('a')
        node = node.children[i]
        # Check if each prefix is a word in the trie.
        if node.isEnding == False:
            return False
        
    
    # We reach here if each prefix of word is present in array.
    return True

def completeString(n: int, a: List[str])-> str:

    # Initialise final answer as empty string.
    ans = ""

    root = TrieNode()

    # Insert each element of array into Trie.
    for i in a:
        insert(i, root)
    

    # Traverse over strings and check which of them have all prefixes present in array.
    for word in a:
        # This word is not valid.
        if allPrefixed(word, root) == False:
            continue
        
        # If current word is longer than 'ans'.
        if len(ans) < len(word):
            ans = word

        # If current word is of same length as 'ans', but is lexicographically smaller than 'ans'.
        elif len(ans) == len(word) and word < ans:
            ans = word
        
    

    # If no valid word is present, return "None".
    if len(ans)== 0:
        ans = "None"
    

    # Return the final result.
    return ans