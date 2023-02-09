# Given two distinct words startWord and targetWord, and a list denoting wordList of unique words
#  of equal lengths. Find all shortest transformation sequence(s) from startWord to targetWord. 
#  You can return them in any order possible.
# Keep the following conditions in mind:

#     A word can only consist of lowercase characters.
#     Only one letter can be changed in each transformation.
#     Each transformed word must exist in the wordList including the targetWord.
#     startWord may or may not be part of the wordList.
#     Return an empty list if there is no such transformation sequence.

# The first part of this problem can be found here.


# Example 1:

# Input:
# startWord = "der", targetWord = "dfs",
# wordList = {"des","der","dfr","dgt","dfs"}
# Output:
# der dfr dfs
# der des dfs
# Explanation:
# The length of the smallest transformation is 3.
# And the following are the only two ways to get
# to targetWord:-
# "der" -> "des" -> "dfs".
# "der" -> "dfr" -> "dfs".


# For example
# wordList = {"des","der","dfr","dgt","dfs"}
# startWord = "der", targetWord= "dfs"
# pattern: des ->*es
#  		   |  \ 
#         d*s  de*
#we will try each word to map to the pattern
#and we form a adjancency list corresponding to the pattern

from collections import deque
import string

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        #Code here
        if targetWord not in wordList:
            return []
        ans = []
        queue = deque([[startWord]])
        visited = set()
        word = set(wordList)
        while queue:
            layer = set()
            for _ in range(len(queue)):
                cur = queue.popleft()
                last = cur[-1]
                if last == targetWord:
                    ans.append(cur)
                # look for next layer of word
                for i in range(len(startWord)):
                    for c in string.ascii_lowercase:
                        next = last[:i] + c + last[i+1:]
                        if next in word and next not in visited:
                            queue.append(cur + [next])
                            layer.add(next)
            visited.update(layer)
        return ans


########################################################################################################################################

# Approach
# First let's see what the problem asked

# Path to the endWord
# This path should be shortest
# The Second point 👆 can be solved by simple BFS ( Solution is same as Word Ladder-I. Click this link for solution )

# But we need to modify the code of Word Ladder-I to store the level / distance of each node from our startWord(source node)

# After BFS We got the distance at which our endWord/target exists so

# Apply Simple Iterative DFS
# by maintaining the path
# and when we encounter the target just append the path to our result
# ⚠ One important thing which doing dfs is that only traverse
# from nodes in lower level - - to nodes in higher level
# You can see that in the code where the condition is
# dist[child] > dist[node]
# this means that the child node is of next level
# By this way we can make sure that we do not loop in the graph forever

# Code

class Solution:
    def findLadders(self, startWord : str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words=set(wordList)
        if endWord not in words:
            return[]
        words.add(startWord)
        
        adj=defaultdict(set)
        
        for word in words:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    neww = word[:i]+c+word[i+1:]
                    if neww!=word and neww in words:
                        adj[word].add(neww)
                        adj[neww].add(word)
        
        
        dist=defaultdict(int)
        vis=set([startWord])
        q=deque([(startWord,1)])
        while q:
            curr,d=q.popleft()
            dist[curr]=d
            for child in adj[curr]:
                if child not in vis:
                    q.append((child,d+1))
                    vis.add(child)
        
        res=[]
        stack=[(startWord,[startWord])]
        while stack:
            curr,path=stack.pop()
            if curr == endWord and len(path)==dist[b]:
                res.append(path)
            for child in adj[curr]:
                if dist[child]>dist[curr]:
                    stack.append((child,path+[child]))
        
        return res

# Complexity
# Time
# O(N x L) where N is the number of words and L is the length of each word
# T = O(26 * L * N + V*E)
# for building adjacency graph "adj" - NxL
# for dfs - N
# for bfs - N
# Space
# O(N)
# We used the following DS

# Stack for DFS - N
# Queue from BFS - N
# HashMap for the adjacency graph and distance- N,N
# List for keeping track of visted node N


##################################################################################################################

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        wordList = set(wordList)
        n = len(beginWord)

        found, swapped = False, False
        start_q, end_q= {beginWord}, {endWord}
        paths, res = collections.defaultdict(set), []

        while start_q and not found:
            next_q = set()
            wordList -= set(start_q)
            for word in start_q:
                for i in range(n):
                    first, second = word[:i], word[i+1:]
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = first+c+second
                        if new_word in wordList:
                            if new_word in end_q:
                                found = True
                            else:
                                next_q.add(new_word)

                            paths[new_word].add(word) if swapped else paths[word].add(new_word)

            start_q = next_q
            
            if len(start_q) > len(end_q):
                start_q, end_q = end_q, start_q
                swapped = not swapped
        
        res = []
        
        def bfs(word, cur_path):
            if word == endWord:
                cur_path.append(word)
                res.append(cur_path[::])
                return
            else:
                for parent in paths[word]:
                    bfs(parent, cur_path+[word])
        bfs(beginWord, [])
        return res

# https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS

################################################################################################

from collections import defaultdict, deque
class Solution(object):
	def findLadders(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""
		
		if endWord not in wordList:
			return []
		
		# Since all words are of same length.
		L = len(beginWord)
		
		# Dictionary to hold combination of words that can be formed,
		# from any given word. By changing one letter at a time.
		all_combo_dict = defaultdict(list)
		for word in wordList:
			for i in range(L):
				# Key is the generic word
				# Value is a list of words which have the same intermediate generic word.
				all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)
		
		# Queue for BFS
		queue = deque([(beginWord, 1)])
		# Visited to make sure we don't repeat processing same word.
		
		visited = {beginWord: True}
		node_dist_and_path = {beginWord: (0, [[beginWord]])}  # node->(dist, list of paths) # path including this word
		
		shortest_distance = None
		while queue:
			current_word, level = queue.popleft()
			
			if shortest_distance is not None and level > shortest_distance:
				continue
				
			for i in range(L):
				# Intermediate words for current word
				intermediate_word = current_word[:i] + "*" + current_word[i + 1:]
				
				# Next states are all the words which share the same intermediate state.
				for word in all_combo_dict[intermediate_word]:
					# If at any point if we find what we are looking for					
					if word == endWord:  # We don't break here! just set the shortest_distance
						shortest_distance = level+1						
					
					if word in node_dist_and_path: # Even when it is already visited, we accumulate paths, as long as it is the shortest!
						next_dist, next_path = node_dist_and_path[word]
						if next_dist == level + 1:  # only update when the distance is equal
							cur_word_dist, cur_word_path = node_dist_and_path[current_word]
							node_dist_and_path[word] = (level + 1, next_path + [a + [word] for a in cur_word_path])
							
					else:  # So it is definitely not visted yet
						cur_word_dist, cur_word_pathes = node_dist_and_path[current_word]
						new_pathes_to_store = [a + [word] for a in cur_word_pathes]
						node_dist_and_path[word] = (level + 1, new_pathes_to_store)
						
					if word not in visited:  # Otherwise, add it to the BFS Queue. Also mark it visited
						visited[word] = True
						queue.append((word, level + 1))
						
		if endWord not in node_dist_and_path:
			return []
		else:
			return node_dist_and_path[endWord][1]