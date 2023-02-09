# 208. Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
# store and retrieve keys in a dataset of strings. There are various applications of this
#  data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
#  (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted 
# string word that has the prefix prefix, and false otherwise.
 

# Example 1:

# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True


class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.childrens:
                curr.childrens[i] = TrieNode()
            curr = curr.childrens[i]
        curr.isWord = True

        
    def search(self, word: str) -> bool:
        curr = self.root
        for s in word:
            if s not in curr.childrens:
                return False
            curr = curr.childrens[s]
        return curr.isWord
            
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for s in prefix:
            if s not in curr.childrens:
                return False
            curr = curr.childrens[s]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode:
    def __init__(self):
        self.childrens = {}
        self.isWord = False
        self.refs = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        cur = self.root
        cur.refs += 1
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self.root
        cur.refs -= 1
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

    def search(self , word):
        curr = self.root
        for char in word:
            if char not in curr.children or curr.refs <= 0:
                return False
            curr = curr.children[char]
        return curr.isWord

# Note: Insert and search costs O(key_length),
#  however, the memory requirements of Trie is O(ALPHABET_SIZE * key_length * N) 