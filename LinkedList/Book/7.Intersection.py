class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to get the length of a list
def get_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

# Function to find the intersection point
def get_intersection(head1, head2):
    # Step 1: Get the lengths of both linked lists
    len1 = get_length(head1)
    len2 = get_length(head2)

    # Step 2: Align the start of both lists
    if len1 > len2:
        for _ in range(len1 - len2):
            head1 = head1.next
    else:
        for _ in range(len2 - len1):
            head2 = head2.next

    # Step 3: Traverse both lists together
    while head1 and head2:
        if head1 == head2:
            return head1  # Found the intersection point
        head1 = head1.next
        head2 = head2.next

    return None  # No intersection found

# Helper function to print a linked list
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Example usage
# List 1: 1 -> 2 -> 3 \
#                     -> 6 -> 7
# List 2:       4 -> 5 /

# Creating two intersecting linked lists
common = Node(6)
common.next = Node(7)

head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)
head1.next.next.next = common

head2 = Node(4)
head2.next = Node(5)
head2.next.next = common

# Print both lists
print("List 1:")
print_list(head1)

print("\nList 2:")
print_list(head2)

# Find intersection
intersection = get_intersection(head1, head2)

if intersection:
    print(f"\nIntersection at node with data: {intersection.data}")
else:
    print("\nNo intersection found.")


A=Node(1)
A.next=Node(2)
A.next.next=Node(3)

B=Node(1)
B.next=Node(2)
B.next.next=Node(3)

print(A==B)