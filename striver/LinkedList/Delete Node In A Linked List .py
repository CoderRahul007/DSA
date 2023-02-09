# Problem Statement
# You are given a Singly Linked List of integers and a reference to the node to be deleted.
#  Every node of the Linked List has a unique value written on it. Your task is to delete that node from the linked list.
# A singly linked list is a linear data structure in which we can traverse only in one direction i.e. 
# from Head to Tail. It consists of several nodes where each node contains some data and a reference to the next node.
class LinkedListNode:
    def __init__(self, data):

        self.data = data
        self.next = None

    def __del__(self):
        if(self.next):
            del self.next

def deleteNode(nodeToDelete):
    # Write your code here.
    nextNode = nodeToDelete.next
    nodeToDelete.data = nextNode.data
    nodeToDelete.next = nextNode.next
    nextNode.next = None
    del(nextNode)