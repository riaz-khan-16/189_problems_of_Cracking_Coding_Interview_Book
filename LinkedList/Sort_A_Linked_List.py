
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



            
def insertion_sort(head):
    sorted_list = None
    current = head

    while current:
        next_node = current.next
        sorted_list = sorted_insert(sorted_list, current)
        current = next_node

    return sorted_list

def sorted_insert(sorted_list, new_node):
    if not sorted_list or sorted_list.data >= new_node.data:
        new_node.next = sorted_list
        sorted_list = new_node
    else:
        current = sorted_list
        while current.next and current.next.data < new_node.data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    return sorted_list

# Example usage
head = Node(4)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)

print("Linked List before sorting:")
print_list(head)

head = insertion_sort(head)

print("Linked List after sorting:")
print_list(head)

        

