# Maintain two dictionaries:

#     frequency {key: frequency} which helps to store the frequency of each key
#     cache {frequency: OrderedDict} which stores all key value pairs with the same counter in a ordered dict

#     Get Method:

#     if not in the cache, return -1
#     obtain the counter f of the key
#     remove the key value pair from the ordered dict that corresponding to frequency f. If the ordered dict is empty, remove it from cache. If the frequency is equal to minimum frequency and the ordered dict is empty after removal, increment minimum frequency by 1
#     insert the key value pair to the orderded dict that corresponding to frequency f+1
#     update the frequency dict and return the value

#     Put Method:

#     call get method to check the presence and increment counter
#     if key is not in the cache:
#     if the cache is full, empty one spot
#     update minimum frequency to 1, and put the key value pair to cache
#     if key is in the cache, only need to update the value

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFrequency = 1
        self.cache = defaultdict(OrderedDict)   # dict {frequency : orderedDict({key, value})}
        self.frequency = {}                     # dict {key : frequency}
        
    def get(self, key: int) -> int: 
        if key not in self.frequency:
            return -1
        f = self.frequency[key]     # get the counter 
        self.frequency[key] = f + 1  # update the counter
        pairs = self.cache[f]
        res = pairs[key]
        del pairs[key]   # remove pair from ordered dict with frequency f
        if len(pairs) == 0:
            del self.cache[f]   # remove ordered dict if empty
            if f == self.minFrequency:
                self.minFrequency += 1  # update min frequency
        self.cache[f+1][key] = res   # put the pair to ordered dict with frequency f + 1
        
        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        oldValue = self.get(key)
        if oldValue == -1: # key is not in the cache
            if len(self.frequency) == self.capacity and self.cache: # cache is full, empty one spot
                k, v = self.cache[self.minFrequency].popitem(last=False)
                del self.frequency[k]
                if len(self.cache[self.minFrequency]) == 0:
                    del self.cache[self.minFrequency]      
            self.minFrequency = 1
            self.frequency[key] = 1
            self.cache[1][key] = value
        else: # key is in the cache, the frequency increment is done in get method
            self.cache[self.frequency[key]][key] = value    
########################################################################################################

from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
    

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = None
        
        # hash map for key-node
        self.key2node = dict()
        
        # doubly-linked hash map
        self.freq2node = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1
        
        node = self.key2node[key]
        # cuz node has been "get", its frequency would go up
        # remove its old pair in freq2node
        del self.freq2node[node.freq][key]
        
        # further check whether old node.freq is empty in freq2node
        if not self.freq2node[node.freq]:
            del self.freq2node[node.freq]
        
        # update node in freq2node
        node.freq += 1
        self.freq2node[node.freq][key] = node
        
        # update min_freq
        if not self.freq2node[self.min_freq]:
            self.min_freq += 1
    
        return node.val
        

    def put(self, key: int, value: int) -> None: 
        if not self.capacity:
            return 
        
        if key in self.key2node:
            self.key2node[key].val = value
            # update key 
            _ = self.get(key)
            return 
        
        # already reached capacity limit
        if len(self.key2node) == self.capacity:
            # remove least frequently used node
            k, node = self.freq2node[self.min_freq].popitem(last=False)
            del self.key2node[k]
        
        self.freq2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.min_freq = 1
        return 
#####################################################################################

class Node:
    
    def __init__(self, key = None, val = 0, frequency = 1):
        self.frequency = frequency
        self.val = val
        self.key = key
        self.prev, self.next = None, None

class DoublyLinkedList:
    
    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    
    # when cache size > capacity, we pop LFU but if there are two then we pop LRU.
    # so we can actually directly pop LRU for that LFU Node List, it would be valid.
    def pop_lfu(self):
        lfu_node, lru_next = self.head.next, self.head.next.next
        self.head.next, lru_next.prev = lru_next, self.head
        return lfu_node
    
    def pop(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev
    
    def insert(self, node):
        tail_prev = self.tail.prev
        tail_prev.next = self.tail.prev = node
        node.prev, node.next = tail_prev, self.tail
        
        
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freq_adjacency_list = defaultdict(DoublyLinkedList)
        self.least_frequency = 0

    # Common update for node when it's frequency is increased due to Get/Put Operation
    def update_node(self, key):
        node = self.cache[key]
        current_node_list = self.freq_adjacency_list[node.frequency]
        current_node_list.pop(node)
        
        # we update(increment) the least frequency when current frequency was the least frequency and
        # least frequent list was empty , we check in simple way if head points to tail then list it empty
        if node.frequency == self.least_frequency and current_node_list.head.next == current_node_list.tail:
            self.least_frequency += 1
            
        self.cache[key] = Node(key, node.val, node.frequency + 1)
        self.freq_adjacency_list[node.frequency + 1].insert(self.cache[key])
    
    def get(self, key: int) -> int:
        
        if key not in self.cache:
            return -1

        self.update_node(key)
        return self.cache[key].val
  
    def put(self, key: int, value: int) -> None:
	
        if self.capacity == 0:
            return -1
			
        if key not in self.cache:
		
            if len(self.cache) == self.capacity:
                least_frequency_list = self.freq_adjacency_list[self.least_frequency]
                lfu_node = least_frequency_list.pop_lfu()
                del self.cache[lfu_node.key]
                
            self.least_frequency = 1
            self.cache[key] = Node(key, value, 1)
            self.freq_adjacency_list[1].insert(self.cache[key])
                
        else:
            self.update_node(key)
            self.cache[key].val = value        