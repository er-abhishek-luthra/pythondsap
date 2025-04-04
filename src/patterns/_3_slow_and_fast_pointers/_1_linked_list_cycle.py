
"""
Problem Statement #
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



def hasCycle(node:Node) -> bool :
    """
    Determines if linked list has a cycle

    Parameters:
    node (Node): The head of linked list

    Returns:
    bool: True is there is a cycle, False otherwise
    """
    slow = node
    fast = node
    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next # Move slow pointer one step
        fast = fast.next.next # Move fast pointer one step
        if slow is fast :
            return True # cycle detected
    return False # No cycle