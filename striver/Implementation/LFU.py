# Doubly Linked List

# In this approach, we will make a hashmap of all frequencies,
#  but instead of storing the nodes in an ordered map, we will 
# store them in a doubly-linked list. Due to using a doubly-linked list, 
# if we have a reference for a node we can delete it in constant time.

# We will create a Node(key, value), where key and value are the respective 
# values in the cache. It also has prev and next, the pointer not next, and previous nodes in the linked list.

# We will create a class DoubleLinkedList, which has properties like rootNode 
# a Node object, representing the sentinel node of the linked list. rootNode.prev 
# will point to the last node of the list, while rootNode.next will point to the first node of the list.

# We will create a method in LFUCache class updateNodeFreq(node), where node a Node
#  class object whose frequency is to be updated.

# In this approach, we will make a hashmap of all frequencies, but instead of storing 
# the nodes in an ordered map, we will store them in a doubly-linked list. Due to using
#  a doubly-linked list, if we have a reference for a node we can delete it in constant time.

# We will create a Node(key, value), where key and value are the respective values in the cache.
#  It also has prev and next, the pointer not next, and previous nodes in the linked list.

# We will create a class DoubleLinkedList, which has properties like rootNode a Node object,
# representing the sentinel node of the linked list. rootNode.prev will point to the last node of the list,
#  while rootNode.next will point to the first node of the list.

# We will create a method in LFUCache class updateNodeFreq(node), where node a Node class object whose
#  frequency is to be updated.

 

# Algorithm:

#     In the class DoubleLinkedList, 
#         constructor():
#             Set rootNode as Node(0, 0)
#             Set rootNode.next and rootNode.prev as rootNode
#             Set currentSize  as 0
#         In the pop(node) method:
#             If currentSize is 0 return
#             If node is null set node as rootNode.prev
#             Set node.prev.next as node.next
#             Set node.next.prev as node.prev
#             Decrease currentSize by 1
#             Return node
#         In the append(node) method:
#             Set node.next as rootNode.next
#             Set node.prev as rootNode
#             Set node.next.prev as node
#             Set rootNode.next as node
#             Increase currentSize by 1
#     In the class LFUCache:
#         In the constructor(capacity):
#             Set currentSize as 0
#             Set capacity as capacity 
#             Initialise an empty hashmap of nodes nodeMap
#             Initialise an empty hashmap of DoubleLinkedList freqMap
#             Set minFreq as 0
#         In the function updateNodeFreq(node)
#             Set freq as node.freq
#             Call freqMap[freq].pop(node)
#             If minFreq is equal to freq and freqMap[freq] is empty
#                 Then increase minFreq by 1
#             Increase node.freq by 1
#             Set freq as node.freq
#             Insert node in freqMap[freq]
#         Int the function get(key) function:
#             If key is not in nodeMap, return -1
#             Set node as nodeMap[key]
#             Call updateNodeFreq(node)
#             Return node.value
#         In the put(key, value) function
#             If capacity is 0 return
#             If key is in nodeMap
#                 Set node as nodeMap[key]
#                 Call updateNodeFreq(node)
#                 Set node.value as value
#                 Return
#             If currentSize is equal to capacity:
#                 Set node as nodeMap[minFreq].pop()
#                 Delete nodeMap[node.key]
#                 Decrease currentSize by 1
#             Set node as Node(key, value)
#             Set nodeMap[key] as node
#             Call freqMap[1].append(node)
#             Set minFreq as 1
#             Increase currSize by 1

# Time Complexity

# O(M), Where ‘M’ denotes the number of operations.

 

# We are using a hashmap of a doubly-linked list, all the operations. Hence the final time complexity is O(M).
# Space Complexity

# O(N), Where ‘N’ is the size of the cache.

 

# We are storing at maximum ‘N’ elements in the hashmap of the doubly linked list.
#  Hence the final time complexity is O(N).


'''
    Time Complexity: O(M)
    Space Complexity: O(N)

    Where 'N' denotes size of cache and 'M' denotes the number of operations.
'''

import collections

class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.freq = 1
        self.prev = self.next = self

# Double Linked List class.
class DoubleLinkedList:

    def __init__(self):
        self.rootNode = Node(0, 0) # Dummy node.
        self.rootNode.next = self.rootNode.prev = self.rootNode
        self.currentSize = 0

    def __len__(self):
        return self.currentSize

    # Insert the node at the head of the the Doubly Linked list.
    def append(self, node):
        node.next = self.rootNode.next
        node.prev = self.rootNode
        node.next.prev = node
        self.rootNode.next = node
        self.currentSize += 1

    # Function that deletes the given node from the linked list.
    # If no node is given it will remove the last node in the doubly linked list.
    def pop(self, node=None):

        if self.currentSize == 0:
            return

        # If no node is given set node as the last node.
        if not node:
            node = self.rootNode.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.currentSize -= 1

        return node

class LFUCache:
    def __init__(self, capacity):
        self.currentSize = 0
        self.capacity = capacity

        self.nodeMap = dict()
        self.freqMap = collections.defaultdict(DoubleLinkedList)
        self.minFreq = 0


    # Update the freqency of any node.
    def updateNodeFreq(self, node):

        freq = node.freq

        # Remove the node from it's frequency list.
        self.freqMap[freq].pop(node)

        if self.minFreq == freq and not self.freqMap[freq]:
            self.minFreq += 1

        node.freq += 1
        freq = node.freq

        # Add the node in the new frequency list.
        self.freqMap[freq].append(node)

    def get(self, key):

        # If the key is not in nodeMap it's not in the cache.
        if key not in self.nodeMap:
            return -1

        # If the node is is present update it's frequency and return the value.
        node = self.nodeMap[key]
        self.updateNodeFreq(node)

        return node.value

    def put(self, key, value):


        if self.capacity == 0:
            return

        # If the key is already present return the value and update the freqency.
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.updateNodeFreq(node)
            node.value = value
            return

        # If the capacity is full remove the LFU node.
        if self.currentSize == self.capacity:

            node = self.freqMap[self.minFreq].pop()
            del self.nodeMap[node.key]
            self.currentSize -= 1


        # Add the node in the freqency list and nodemap
        node = Node(key, value)
        self.nodeMap[key] = node
        self.freqMap[1].append(node)
        self.minFreq = 1

        self.currentSize += 1

#######################################################################################################

# Ordered map

# In this approach, we create a hash map of ordered maps, where each key in
#  the map will have a set of the node with that frequency. Each time node is 
# fetched or updated, we update the frequency of the node by deleting it from its 
# ordered map and adding it in the ordered map with 1 higher frequency.

# We also maintain a minimum frequency, if the cache is full we can delete the first
#  element in the map of minimum frequency, since each map is ordered it will be the 
# first element of the map.

# In an ordered map deletion will take logarithmic time.

 

# We create a Node(value) class, where ‘value’ is the value of the node and it also has
#  a frequency property ‘freq’ which is initialized to 1.
 

# We will also create a helper method in the LFUCache class called updateNodeFreq(key), 
# where the key is the key of the node whose frequency is to be updated.

 

# Algorithm:

#     In the constructor(capacity) function:
#         Set capacity as ‘capacity,
#         Initialise a hashmap of an integer as key and ordered map as the value called countNode
#         Initialise a hashmap of an integer key and Node as value called  keyNode
#         Set minCount as 0
#     In the function updateNodeFreq(key):
#         Set freq as keyNode[key].freq
#         Delete key from the ordered map ‘countNode[freq]’
#         Increase keyNode[key].freq by 1
#         Set countNode[freq + 1][key] as keyNode[key].
#         If the length of the map countNode[minCount] is 0
#             Increase minCount by 1
#     In the get(key) function
#         If key is not in keyNode return -1
#         Set value as keyNode[key].value
#         Call updateNodeFreq(key)
#         Return value
#     Int the put(key, value)
#         If capacity is 0 return
#         If key is in keyNode
#             Set keyNode[key].value as value
#             Call updateNodeFreq(key)
#             Return from the function
#         If size of keyNode is equal to capacity
#             Pop the first item in coutNode[minCount] as set it’s key as minKey
#             Delete minKey from keyNode
#         Set keyNode[key] equal to a new instance of Node(value)
#         Set countNode[1][key] as keyNode[key]
#         Set minCount as 1

# Time Complexity

# O(M * logN),  where ‘N’ denotes the size of the cache and ‘M’ denotes the number of operations. 
 
# Each operation takes O(logN) time as we are using an ordered map.
# Space Complexity

# O(N), where ‘N’ denotes the size of the cache.
 
#  We maintain the cache in the form of a set of size ‘N’.

'''
    Time Complexity: O(M * log(N))
    Space Complexity: O(N)

    Where 'N' denotes size of cache and 'M' denotes the number of operations.
'''

import collections

# Node class that stores value and frequence of a cache item.
class Node:
    def __init__(self, val):
        self.value = val
        self.freq = 1

class LFUCache:

    # Initialise the mincount, capacity integers.
    # Also Hashmap of OrderedMaps to keep track of nodes with particular frequency.
    def __init__(self, capacity: int):
        self.keyNode = {}
        self.countNode = collections.defaultdict(collections.OrderedDict)
        self.capacity = capacity
        self.minCount = 0

    # Update a node's frequency by 1 and also cheks if minimun frequency can be updated.
    def updateNodeFreq(self, key: int) -> None:
        freq = self.keyNode[key].freq
        self.countNode[freq].pop(key)
        self.keyNode[key].freq += 1
        self.countNode[freq + 1][key] = self.keyNode[key]

        # If nothing is present in the minimun count increase it by 1.
        if len(self.countNode[self.minCount]) == 0:
           self.minCount += 1

    def get(self, key: int) -> int:

        # If the key is not present return -1.
        if key not in self.keyNode:
            return -1

        # Get the value and update node's frequency.
        value = self.keyNode[key].value
        self.updateNodeFreq(key)

        return value


    def put(self, key: int, value: int) -> None:

        # If capacity is 0 return.
        if self.capacity == 0:
            return

        # If the key is already present update it's value and frequency.
        if key in self.keyNode:
            self.keyNode[key].value = value
            self.updateNodeFreq(key)
            return

        # If number of items are equal to the capacity of the cach.
        if len(self.keyNode) == self.capacity:

            # Delete the LRU node of minimun frequency.
            minKey, _ = self.countNode[self.minCount].popitem(last=False)
            del self.keyNode[minKey]


        # Add the new node at frequency 1.
        self.keyNode[key] = Node(value)
        self.countNode[1][key] = self.keyNode[key]
        self.minCount = 1

