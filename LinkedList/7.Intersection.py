# Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
# Return the intersecting node. Note that the intersection is defined based on reference, not 
# value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting. 


class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_intersection(list1, list2):
    if not list1 or not list2:
        return None

    # Helper function to get the length of a linked list
    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # Get the lengths of both linked lists
    len1 = get_length(list1)
    len2 = get_length(list2)

    # Reset the pointers to the beginning of the lists
    current1, current2 = list1, list2

    # Move the pointer of the longer list to make both lists equal in length
    while len1 > len2:
        current1 = current1.next
        len1 -= 1

    while len2 > len1:
        current2 = current2.next
        len2 -= 1

    # Traverse both lists until an intersection is found
    while current1 and current2:
        if current1 == current2:
            return current1
        current1 = current1.next
        current2 = current2.next

    return None

# Test cases
# Case 1: No Intersection
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list2 = ListNode(5, ListNode(6, ListNode(7)))
result = find_intersection(list1, list2)
print(result)  # Output should be None

# Case 2: Single Node Intersection
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
list2 = ListNode(5, ListNode(6, list1.next.next))
result = find_intersection(list1, list2)
print(result.value)  # Output should be 3

# Add more test cases as needed...





