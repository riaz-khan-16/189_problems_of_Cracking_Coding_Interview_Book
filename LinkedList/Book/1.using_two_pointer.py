class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates_sorted(head):
    current = head

    # Traverse the list till the end
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # Move to the next node if no duplicate
            current = current.next

    return head

def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Example usage
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)

print("Original List:")
print_list(head)

head = remove_duplicates_sorted(head)

print("List after removing duplicates:")
print_list(head)
