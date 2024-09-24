class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = fast = head
    
    # Traverse the linked list
    while fast and fast.next:
        slow = slow.next  # Move slow pointer by one
        fast = fast.next.next  # Move fast pointer by two
    
    # When fast reaches the end, slow will be at the middle
    return slow.data

# Example linked list creation
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Find the middle of the linked list
middle = find_middle(head)
print("The middle element is:", middle)
