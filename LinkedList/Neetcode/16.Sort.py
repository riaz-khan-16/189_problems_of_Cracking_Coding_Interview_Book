
# https://leetcode.com/problems/sort-list/submissions/

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to merge two sorted lists
def merge_sorted_lists(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left.data <= right.data:
        result = left
        result.next = merge_sorted_lists(left.next, right)
    else:
        result = right
        result.next = merge_sorted_lists(left, right.next)
    
    return result

# Function to find the middle of the list
def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Merge sort function
def merge_sort(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next

    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = merge_sorted_lists(left, right)
    
    return sorted_list

# Function to print the list
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Example usage
head = Node(3)
head.next = Node(1)
head.next.next = Node(5)
head.next.next.next = Node(2)

print("Linked List before sorting:")
print_list(head)

head = merge_sort(head)

print("Linked List after sorting:")
print_list(head)
