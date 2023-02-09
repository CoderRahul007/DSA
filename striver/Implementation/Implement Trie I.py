#  Hashmap/Dictionary Approach

# Firstly we have defined the node class of Trie having members:

#     child  - storing the address of child nodes (hashmap of character number and address of Trie Node)
#     isEnd - a bool variable for marking this node as an end of some word.

# Then we have defined our Trie Class having members:

#     root - The root node for whole Trie, every word starts from this node.
#     insert(word) - To insert a string "word" in Trie
#     search(word) - To check if string "word" is present in Trie or not.
#     startsWith(word) - To check if there is any string in the Trie that starts with the given prefix string "word".

# Definition of insert(word):

#     Initialize the current node with the root node of Trie.
#     Iterate over the word from left to right and if there is no node present for the next character of the word then create a new node and store it in child member of the previous character’s node.
#     Keep updating the current node to the corresponding node for the next character of the word.
#     Finally, when we reached the end of the word, mark the isEnd member of the current node to true as it will denote the word is present or not.

# Definition of search(word):

#     Initialize the current node with the root node of Trie.
#     Iterate over the word from left to right and if there is no node present for the next character of the word then return false as the word is not present in the Trie.
#     Keep updating the current node to the corresponding node for the next character of the word.
#     Finally, when we reached the end of the word, return the isEnd bool variable of the current node as it will denote the word is present or not.

# Definition of startsWith(word):

#     Initialize the current node with the root node of Trie.
#     Iterate over the word from left to right and if there is no node present for the next character of the word then return false as the no word is present in the Trie with this word as a Prefix.
#     Keep updating the current node to the corresponding node for the next character of the word.
#     Finally, when we reached the end of the word, return true as some word must be present in the Trie as we are able to cover the whole prefix word.

# Time Complexity

# O(N*W) (insert - O(W), search - O(W), startsWith - O(W))

# where N is the number of queries and W is the average length of words.

# For all the operations we are iterating over the word and checking in hashmap for the next character of the word so that’s an O(1) operation on average so Overall Time Complexity for insert, search, startsWith is O(W).
# Space Complexity

# O(N*W) where N is the number of words inserted and W is the average length of words.

# As we are making nodes of each character of a node so at max we can have all unique sequence of the words. This hashmap approach of storing child is more space-efficient than an array for storing child as we will only store the address for the nodes present in the Trie.

'''
    Time Complexity : O(N*W) (insert - O(W), search - O(W), startsWith - O(W))
    Space Complexity : O(N*W)

    Where N is the number of queries and W is the average length of words.
'''
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode :
    
    def __init__(self) :

        self.child = {}
        self.isEnd = False

class Trie :

    def __init__(self) :

        self.node = TrieNode()
    
    def insert(self, string) :

        n = len(string)
        if(n == 0) :
            self.node.isEnd = True
            return 
        else :
            if string[0] in self.node.child :
                self.node.child[string[0]].insert(string[1:])
            
            else :
                self.node.child[string[0]] = Trie()
                self.node.child[string[0]].insert(string[1:])
        return 

    
    def search(self, word) :
        temp = self.node
        for i in range(len(word)) :
            if word[i] not in temp.child :
                return False
            
            else :
                temp = temp.child[word[i]].node

        if(temp.isEnd == True) :
            return True
        else :
            return False

        
    def startWith(self, prefix) :
        temp = self.node
        for i in range(len(prefix)) :
            if prefix[i] not in temp.child :
                return False

            temp = temp.child[prefix[i]].node
        
        return True



# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")

########################################################################################################################
#  Array Approach

# Firstly we have defined the node class of Trie having members:

#     child  - storing the address of child nodes (Array of the address of Trie Nodes with size 26 initialized with NULL)
#     isEnd - a bool variable for marking this node as an end of some word.

# Then we have defined our Trie Class having members:

#     root - The root node for whole Trie, every word starts from this node.
#     insert(word) - To insert a string "word" in Trie
#     search(word) - To check if string "word" is present in Trie or not.
#     startsWith(word) - To check if there is any string in the Trie that starts with the given prefix string "word".

# Definition of insert(word):

#     Initialize the current node with the root node of Trie.
#     Iterate over the word from left to right and if there is NULL in the address of the node for the next character of the word then create a new node and store the address in child member of the previous character’s node.
#     Keep updating the current node to the corresponding node for the next character of the word.
#     Finally, when we reached the end of the word, mark the isEnd member of the current node to true as it will denote the word is present or not.

# Definition of search(word):

#     Initialize the current node with the root node of Trie.
#     Iterate over the word from left to right and if there is NULL in the address of the node for the next character of the word then return false as the word is not present in the Trie.
#     Keep updating the current node to the corresponding node for the next character of the word.
#     Finally, when we reached the end of the word, return the isEnd bool variable of the current node as it will denote the word is present or not.

# Definition of startsWith(word):

#     Initialize the current node with the root node of Trie.
#     Iterate over the word from left to right and if there is NULL in the address of the node for the next character of the word then return false as the no word is present in the Trie with this word as a Prefix.
#     Keep updating the current node to the corresponding node for the next character of the word.
#     Finally, when we reached the end of the word, return true as some word must be present in the Trie as we are able to cover the whole prefix word.

# Time Complexity

# O(N*W) (insert - O(W), search - O(W), startsWith - O(W))

# where N is the number of queries and W is the average length of words.

# For all the operations we are iterating over the word and checking in the array for the next character of the word so Overall Time Complexity for insert, search, startsWith is O(W).

# This array approach of storing child is more time-efficient than hashmap for storing child as the constant factor of O(1) in hashmaps is more costly.
# Space Complexity

# O(N*W) where N is the number of words inserted and W is the average length of words.

# As we are making nodes of each character of a node so at max we can have all unique sequence of the words. So overall space can be at max 26*N*W, so Overall Space Complexity is O(N*W)

'''
    Time Complexity : O(N*W) (insert - O(W), search - O(W), startsWith - O(W))
    Space Complexity : O(N*W)

    Where N is the number of queries and W is the average length of words.
'''
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

class TrieNode :
    
    def __init__(self) :

        self.child = [None for i in range(26)]
        self.isEnd = False

class Trie :

    def __init__(self) :

        self.node = TrieNode()
    
    def insert(self, string) :

        n = len(string)
        if(n == 0) :
            self.node.isEnd = True
            return 
        else :
            if self.node.child[ord(string[0]) - ord('a')] != None :
                self.node.child[ord(string[0]) - ord('a')].insert(string[1:])
            
            else :
                self.node.child[ord(string[0]) - ord('a')] = Trie()
                self.node.child[ord(string[0]) - ord('a')].insert(string[1:])
        return 

    
    def search(self, word) :
        temp = self.node
        for i in range(len(word)) :
            if temp.child[ord(word[i]) - ord('a')] == None:
                return False
            
            else :
                temp = temp.child[ord(word[i]) - ord('a')].node

        if(temp.isEnd == True) :
            return True
        else :
            return False

        
    def startWith(self, prefix) :
        temp = self.node
        for i in range(len(prefix)) :
            if temp.child[ord(prefix[i]) - ord('a')] == None :
                return False

            temp = temp.child[ord(prefix[i]) - ord('a')].node
        
        return True



# main
t = int(input().strip())
root = Trie()
for i in range(t) :

    q_str = stdin.readline().strip().split(" ")
    q = int(q_str[0].strip())
    str1 = q_str[1].strip()

    if(q == 1) :
        root.insert(str1)
    
    elif (q == 2) :
        if(root.search(str1)) :
            print("true") 

        else :
            print("false")
        
    else :
        if(root.startWith(str1)) :
            print("true")

        else :
            print("false")

