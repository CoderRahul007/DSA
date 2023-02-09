# https://leetcode.com/problems/lru-cache/solutions/1188897/python-doubly-ll-dict-visualized-and-commented/?languageTags=python&topicTags=linked-list
###############################################################################################

class Node:
    def __init__(self , key , val):
        self.key , self.val = key , val
        self.prev = self.next = None

class LRUCache:
    def __init__(self , capacity):
        self.cap = capacity
        self.cache = {}

        # Left- LRU  , right - MRU
        self.left , self.right = Node(0 , 0 ) , Node(0 , 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # remove node from list
    def removeFromDL(self , node):
        prev , nxt = node.prev , node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insertNodeAtRight( self  , node):
        prev = self.right.prev
        nxt = self.right

        prev.next = nxt.prev = node
        node.next , node.prev = nxt , prev
    
    def get(self , key):
        if key in self.cache:
            foundNode = self.cache[key]
            self.removeFromDL(foundNode)
            self.insertNodeAtRight(foundNode)
            return foundNode.val
        return -1
    
    def put(self , key , val):
        if key in self.cache:
            self.removeFromDL(self.cache[key])
        self.cache[key] = Node(key , val)
        self.insertNodeAtRight(self.cache[key])

        if len(self.cache) > self.cap:
            # delete the LRU
            lru = self.left.next

            # delete from DLL
            self.removeFromDL(lru)

            # delete from cache
            del self.cache[lru.key]



#############################################################################################
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.d = {}
        self.head = Node(-1,-1) # dummy node
        self.tail = self.head # both head and tail initially point at dummy node
        self.size = 0 # initially zero cuz we only have a dummy node to begin with
        
        # this impl of LRU cache has MRU items at the tail and LRU at the head
        
    def put(self, k: int, v: int) -> None:
        if k in self.d:
            node = self.d[k] # fetch rather than create
            node.v = v # update the value (ex: put(2,1) then put(2,3). Same key, different value -> must update value)
            # re-position to make node MRU (aka at tail)
            # must check if not already MRU
            if node.next:
                # 1- severe ties between node and neigh nodes
                node.prev.next = node.next
                node.next.prev = node.prev

                # 2 - stick node at the tail
                self.tail.next = node
                node.next = None
                node.prev = self.tail
                # update tail
                self.tail = node
            # otherwise it's already MRU -> no action needed
            
            
        else:
            # create node from scratch and insert in both cache and DLL
            # must check for cpacity and apply eviction polciy if necessaey
            node = Node(k,v)
            # 1- Stick at tail of DLL
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
            # 2- append to cahce dict
            self.d[k] = node
            # incrment size
            self.size += 1
            # check for capacity
            if self.size > self.capacity:
                # need to evict
                remove = self.head.next # by design, this is the fixed position of the node to be evicted
                # 1- severe ties from DLL
                self.head.next = remove.next
                remove.next.prev = self.head
                
                # self.head.next = self.head.next.next
                # self.head.next.prev = self.head
                
                # 2- remove from cahce dict
                del self.d[remove.k]
                # dec size
                self.size -= 1
            
    def get(self, k: int) -> int:
        if k not in self.d:
            return -1
        
        node = self.d[k] # fetch rather tahn create
        # check if not already MRU
        if node.next:
            # need to re-position
            # 1- severe ties
            node.prev.next = node.next
            node.next.prev = node.prev

            # 2- stick at the tail
            node.next = None
            self.tail.next = node
            node.prev = self.tail
            # update tail
            self.tail = node
            
        return node.v
        
#########################################################################
from collections import OrderedDict

class LRUCache:

	# initialising capacity
	def __init__(self, capacity: int):
		self.cache = OrderedDict()
		self.capacity = capacity

	# we return the value of the key
	# that is queried in O(1) and return -1 if we
	# don't find the key in out dict / cache.
	# And also move the key to the end
	# to show that it was recently used.
	def get(self, key: int) -> int:
		if key not in self.cache:
			return -1
		else:
			self.cache.move_to_end(key)
			return self.cache[key]

	# first, we add / update the key by conventional methods.
	# And also move the key to the end to show that it was recently used.
	# But here we will also check whether the length of our
	# ordered dictionary has exceeded our capacity,
	# If so we remove the first key (least recently used)
	def put(self, key: int, value: int) -> None:
		self.cache[key] = value
		self.cache.move_to_end(key)
		if len(self.cache) > self.capacity:
			self.cache.popitem(last = False)


# RUNNER
# initializing our cache with the capacity of 2
cache = LRUCache(2)


cache.put(1, 1)
print(cache.cache)
cache.put(2, 2)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.put(3, 3)
print(cache.cache)
cache.get(2)
print(cache.cache)
cache.put(4, 4)
print(cache.cache)
cache.get(1)
print(cache.cache)
cache.get(3)
print(cache.cache)
cache.get(4)
print(cache.cache)

#########################################################################################################

class Node:
    
    def __init__(self, key=None, val=None, prev=None, next_=None):

        self.key = key
        self.val = val
        self.prev = prev
        self.next = next_

    def __repr__(self):
        return f"{self.val} <-> {self.next}"

    def __str__(self):
        return self.__repr__()

class DLL:

    def __init__(self):
        self.head = self.tail = None
        self.node_count = 0

    def __repr__(self):
        return f"{self.head}"

    def __str__(self):
        return self.__repr__()

    def add(self, key, val):

        node = Node(key, val)

        if not self.head:
            self.head = self.tail = node
        else:        
            self.head.prev = node
            node.next = self.head
            self.head = node

        self.node_count += 1
        return node

    def remove_node(self, node):

        if node:
            if not node.prev and not node.next:
                self.head = self.tail = None
                return

            if node.prev:
                node.prev.next = node.next
            else:
                node.next.prev = None
                self.head = node.next

            if node.next:
                node.next.prev = node.prev
            else:
                node.prev.next = None
                self.tail = node.prev

            self.node_count -= 1

    def move_to_head(self, node):

        if node.prev:
            self.remove_node(node)

            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node

            self.node_count += 1

class LRUCache:
        
    def __init__(self, capacity: int, *args, **kwargs):
        
        self.cap = capacity
        self.dll = DLL()
        self.db = {}

    def get(self, key: int) -> int:
        
        found = self.db.get(key)
        
        if not found:
            return -1
        
        self.dll.move_to_head(found)
        return found.val

    def put(self, key: int, value: int) -> None:
        
        found = self.db.get(key)
        
        if found is None:
		
            if self.dll.node_count + 1 > self.cap:
			
                key_to_remove = self.dll.tail.key
                self.dll.remove_node(self.dll.tail)
                del self.db[key_to_remove]
				
            new_node = self.dll.add(key, value)
            self.db[key] = new_node
        else:
            found.val = value
            self.dll.move_to_head(found)

