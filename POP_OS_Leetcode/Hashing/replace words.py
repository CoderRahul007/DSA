'''# In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

# You need to output the sentence after the replacement.

 

# Example 1:

# Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"'''

 

# Constraints:

#     The input will only have lower-case letters.
#     1 <= dict.length <= 1000
#     1 <= dict[i].length <= 100
#     1 <= sentence words number <= 1000
#     1 <= sentence words length <= 1000
# class Solution:
#     def replaceWords(self, dict: List[str], sentence: str) -> str:
#         def replace(word):
#             for i in range(1,len(word)):
#                 if word[:i] in dict:
#                     return word[:i]
#             return word
#         return " ".join(map(replace,sentence.split()))
#         #always search in the constant list


#Java Trie Solution-----------------------------------------
# class Solution {
#     public String replaceWords(List<String> roots, String sentence) {
#         TrieNode trie = new TrieNode();
#         for (String root: roots) {
#             TrieNode cur = trie;
#             for (char letter: root.toCharArray()) {
#                 if (cur.children[letter - 'a'] == null)
#                     cur.children[letter - 'a'] = new TrieNode();
#                 cur = cur.children[letter - 'a'];
#             }
#             cur.word = root;
#         }

#         StringBuilder ans = new StringBuilder();

#         for (String word: sentence.split("\\s+")) {
#             if (ans.length() > 0)
#                 ans.append(" ");

#             TrieNode cur = trie;
#             for (char letter: word.toCharArray()) {
#                 if (cur.children[letter - 'a'] == null || cur.word != null)
#                     break;
#                 cur = cur.children[letter - 'a'];
#             }
#             ans.append(cur.word != null ? cur.word : word);
#         }
#         return ans.toString();
#     }
# }

# class TrieNode {
#     TrieNode[] children;
#     String word;
#     TrieNode() {
#         children = new TrieNode[26];
#     }
# }


'''Trie in python -----------------------'''
# class Node(object):
#     def __init__(self,val):
#         self.val = val
#         self.children = {}
        
# class Trie(object):
#     def __init__(self):
#         self.root = Node(None)
    
#     def add(self, word : str) -> None:
#         curr = self.root
#         for char in word:
#             if char not in curr.children:
#                 curr.children[char] = Node(char)
#             curr = curr.children[char]
#         curr.children['*'] = None

# class Solution:
#     def __init__(self):
#         self.visited = {}
        
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         #1. Add all prefixes from the dictionary into a prefix tree
#         tree = Trie()
#         for word in dictionary:
#             tree.add(word)
        
#         #2. Split sentence into individual words
#         sentence = sentence.strip(' ').split(' ')
        
#         for i in range(len(sentence)):
            
#             #3. If a word has already been seen, use the previous result for that word
#             if sentence[i] in self.visited:
#                 sentence[i] = self.visited[sentence[i]]
#                 continue
            
#             #4. Check if a prefix exists in the dictionary and replace it
#             curr = tree.root
#             for j,char in enumerate(sentence[i]):

#                 if char in curr.children:
#                     curr = curr.children[char]
#                 else:
#                     #5. Cache result for O(1) look-up time if this word is seen again
#                     self.visited[sentence[i]] = sentence[i]
#                     break
                    
#                 if '*' in curr.children:                    
#                     #5. Cache result for O(1) look-up time if this word is seen again
#                     self.visited[sentence[i]] = sentence[i][:j+1]
#                     sentence[i] = self.visited[sentence[i]]
#                     break
        
#         return ' '.join(sentence)
import collections
from functools import reduce
class Solution(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True
        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root 
            '''Structure of trie for cat{'c':{'a':address,'t':address,'True':'cat'}}   '''
        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur:
                    break
                
                # print('before',letter)
                # for i,v in cur.items():
                #     print(i,'------')               
                #     print(v)
                # print()
                cur = cur[letter]     # going at deeper levels of dictinary whenever the letter is found                
                # print('after',letter)     
                # for i,v in cur.items():
                #     print(i,'--------')        
                #     print(v)      
            return cur.get(END, word) # if END is reached output that else the word
        
        return " ".join(map(replace, sentence.split()))
s=Solution()
print(s.replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery"))

#Output Of searching in trie
# Break
# before c
# c ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})})})
# b ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})})})
# r ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})})})

# after c
# a --------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})})
# before a
# a ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})})

# after a
# t --------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})
# before t
# t ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})

# after t
# True --------
# cat
# Break
# Break
# before r
# c ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})})})
# b ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})})})
# r ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})})})

# after r
# a --------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})})
# before a
# a ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})})

# after a
# t --------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})
# before t
# t ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})

# after t
# True --------
# rat
# Break
# before b
# c ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})})})
# b ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})})})
# r ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})})})

# after b
# a --------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})})
# Break
# Break
# before b
# c ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'cat'})})})
# b ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})})})
# r ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'a': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'rat'})})})

# after b
# a --------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})})
# before a
# a ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {'t': defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})})

# after a
# t --------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})
# before t
# t ------
# defaultdict(<function Solution.replaceWords.<locals>.<lambda> at 0x7f9064be4dc0>, {True: 'bat'})

# after t
# True --------
# bat
# Break
# the cat was rat by the bat
