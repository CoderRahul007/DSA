'''
	Time complexity: O(N * L) 
        insert - O(N)
        countWordsEqualTo - O(N)
        countWordsStartingWith - O(N)
        erase - O(N)
	Space complexity: O(N * L) 

	Where 'N' and 'L' represents the numbers of words 
	and the longest word in words.
'''
 
class TrieNode():
    
    def __init__(self):
        self.children = [None] * 26
        self.wordCount = 0
        self.prefixCount = 0
        
class Trie():
    
    # Declare a variable root that denotes the root of the Trie.
    def __init__(self):
        self.root = TrieNode()
        
    # In this function we are inserting the word into our Trie.
    def insert(self, word):
        curr = self.root
        
        for i in range (len(word)):
            index = ord(word[i]) - 97
            
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
                
            curr = curr.children[index]
            curr.prefixCount += 1
            
        curr.wordCount += 1
        
    def countWordsEqualTo(self, word):
        curr = self.root
        
        # Iterating through the starting word.
        for i in range (len(word)):
            index = ord(word[i]) - 97
            
            if curr.children[index] == None:
                return 0
                
            curr = curr.children[index]
            
        return curr.wordCount
    
    def countWordsStartingWith(self, word):
        curr = self.root
        
        # Iterating through the starting word.
        for i in range (len(word)):
            index = ord(word[i]) - 97
            
            if curr.children[index] == None:
                return 0
                
            curr = curr.children[index]
            
        return curr.prefixCount
    
    # In this function we are removing the word from "TRIE".
    def erase(self, word):
        
        curr = self.root
        toBeDeleted = None
        
        # Iterating through the starting word.
        for i in range (len(word)):
            index = ord(word[i]) - 97
            
            parent = curr
            curr = curr.children[index]
            
            # If we are removing the given word then subtract 1 from the prefixCount.
            curr.prefixCount -= 1
            
            if toBeDeleted:
                toBeDeleted = None
                
            if curr.prefixCount == 0:
                if not toBeDeleted:
                    parent.children[index] = None
                    
                toBeDeleted = curr
            
            curr.wordCount -= 1
            
            if toBeDeleted:
                toBeDeleted = None
