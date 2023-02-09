# #########################################################################3

# Time Complexity
# O(N ^ 3), where ‘N’ is the length of the string ‘WORD’.

# First, we are generating all the possible substrings of ‘WORD’ it takes O(N^2) time,
#  and then we are adding this substring into HashSet ‘ans', it takes O(N) time. Hence
#  overall time complexity will be O(N ^ 3).

# Space Complexity
# O(N ^ 2), where ‘N’ is the length of the string ‘WORD’.

# Because in the worst case the size of our hash set is of order ‘N ^ 2’ .
# Hence overall time complexity will be O(N ^ 2).

from os import *
from sys import *
from collections import *
from math import *

def distinctSubstring(word):
    # Write your code here.
    mp = set()
    for i in range(len(word)):
        tmp = ""
        for j in range(i , len(word)):
            tmp += word[j]
            mp.add(tmp)
    return len(mp)
            

######################################################################################
# using trie
# The basic idea of this approach is the first iterate over this string ‘WORD’ and store 
# all substrings of this string into a ‘TRIE’. Then iterate through this ‘TRIE’ and count
#  how many words are there in the ‘TRIE’ that is our desired result.

 

# The steps are as follows:

 

#     Declare a variable ‘count’ = 0 in which we store the number of the distinct 
#     substrings in the string ‘WORD’.
#     TrieNode class/struct:
#         Make an array of ‘children’ that is a type of class/struct TrieNode.
#         Make a node ‘trie’ of the class/struct TrieNode.
#         We run a loop ‘i’ = 0 to ‘N’:
#             Call insertIntoTrie(substring(i)).
#         Call countNodeInTrie(‘trie’).
#         Finally, return ‘count’.
#     insertIntoTrie(‘word’)
#         Make a TrieNode ‘curr’ and store ‘trie’.
#         Run a loop for ‘i’ = 0 to the length of the ‘word’:
#             ‘Index’ = ‘word[i]’ - ‘a’.
#             If ‘curr.children[‘index’]’ is equal to ‘NULL’:
#                 Add a new ‘TrieNode’ node at this ’curr’ node.
#             ‘curr’ is equal to ‘curr.children[index]'.
#     countNodeInTrie(‘curr’).
#         If  ‘curr’ is equal to ‘NULL’:
#             Return.
#         Run a loop ‘i’ to 26:
#             If ‘curr.children[i]’ is not equal to ‘NULL’:
#                 ‘count’ = ‘count’ +1
#             ‘countNodeInTrie’(‘curr.children[i]’).

# Time Complexity

# O(N ^ 3), where ‘N’ is the size of ‘WORD’.


# First, we are generating all the possible substrings of ‘WORD’ it takes O(N^2) time,
#  and then we are adding this substring into the ‘TRIE’ that takes O(N) time. After that,
#  we iterate over ‘TRIE’ and count all different nodes that take O(N^2) time. Hence the 
# overall time complexity is O(N^3).
# Space Complexity

# O(N ^ 2), where ‘N’ is the size of ‘WORD’.

# Because we are storing all the substrings of the ‘WORD’ (i.e ‘N’ ^ 2) into the ‘TRIE’ and 
# then iterating over all the ‘TRIE’. Hence the space complexity is O(N^2).

"""	
	Time complexity: O(N ^ 3)
	Space complexity: O(N ^ 2) 
	Where N represents the length of word.
"""


class TrieNode:
    def __init__(self):
        self.children = [None] * 26


trie = []
countNodes = 0


# Add string str into the Trie.
def insert(string):

    curr = trie

    for i in range(len(string)):
        ind = ord(string[i]) - 97

        if curr.children[ind] == None:
            curr.children[ind] = TrieNode()
        curr = curr.children[ind]


# Count Nodes of the Trie.
def countNodeInTrie(curr):

    if curr == None:
        return

    for i in range(26):
        if curr.children[i] != None:
            global countNodes
            countNodes += 1
            countNodeInTrie(curr.children[i])


def distinctSubstring(word):

    global trie
    trie = TrieNode()
    global countNodes
    countNodes = 0

    # Iterate over the word and add it's substrings into the Trie.
    for i in range(len(word)):
        h = word[i:]
        insert(h)

    curr = trie
    countNodeInTrie(curr)

    del trie

    return countNodes
