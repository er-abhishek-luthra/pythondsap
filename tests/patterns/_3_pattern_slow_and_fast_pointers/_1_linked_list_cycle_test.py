import pytest
from patterns._3_slow_and_fast_pointers._1_linked_list_cycle import Node, hasCycle

def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def create_cycle_at_index(head, index):
    """Helper function to create a cycle at the specified index."""
    if not head:
        return None
    
    # Find the node at the specified index
    cycle_node = head
    for _ in range(index):
        if not cycle_node:
            return head
        cycle_node = cycle_node.next
    
    # Find the last node
    last_node = head
    while last_node.next:
        last_node = last_node.next
    
    # Create cycle by connecting last node to cycle_node
    last_node.next = cycle_node
    return head

def test_empty_list():
    """Test case for an empty list."""
    assert not hasCycle(None)

def test_single_node():
    """Test case for a list with a single node."""
    head = Node(1)
    assert not hasCycle(head)

def test_single_node_with_self_cycle():
    """Test case for a single node pointing to itself."""
    head = Node(1)
    head.next = head
    assert hasCycle(head)

def test_two_nodes_no_cycle():
    """Test case for two nodes without a cycle."""
    head = create_linked_list([1, 2])
    assert not hasCycle(head)

def test_two_nodes_with_cycle():
    """Test case for two nodes with a cycle."""
    head = create_linked_list([1, 2])
    head.next.next = head
    assert hasCycle(head)

def test_multiple_nodes_no_cycle():
    """Test case for multiple nodes without a cycle."""
    head = create_linked_list([1, 2, 3, 4, 5])
    assert not hasCycle(head)

def test_cycle_at_beginning():
    """Test case for a cycle that starts at the beginning."""
    head = create_linked_list([1, 2, 3, 4, 5])
    head = create_cycle_at_index(head, 0)
    assert hasCycle(head)

def test_cycle_at_middle():
    """Test case for a cycle that starts in the middle."""
    head = create_linked_list([1, 2, 3, 4, 5])
    head = create_cycle_at_index(head, 2)
    assert hasCycle(head)

def test_cycle_at_end():
    """Test case for a cycle that starts at the end."""
    head = create_linked_list([1, 2, 3, 4, 5])
    head = create_cycle_at_index(head, 4)
    assert hasCycle(head)

def test_long_list_no_cycle():
    """Test case for a long list without a cycle."""
    head = create_linked_list(range(1000))
    assert not hasCycle(head)

def test_long_list_with_cycle():
    """Test case for a long list with a cycle."""
    head = create_linked_list(range(1000))
    head = create_cycle_at_index(head, 500)
    assert hasCycle(head)