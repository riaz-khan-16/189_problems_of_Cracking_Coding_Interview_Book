
#Palindrome: Implement a function to check if a linked list is a palindrome. 


class  Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

Linkedlist=Node(1,Node(2,Node(3,Node(2,Node(1)))))    

def insertAtHead(head,newNode):
    if head is None:
        head=newNode
    else:
        temp=head
        head=newNode
        head.next=temp   
    return head    

def reverse_it(head):
    reverse=Node()
    current=head
    while current is not None:
        x=current.data
        reverse=insertAtHead(reverse,Node(x))
        current=current.next

    return reverse    
reverse=reverse_it(Linkedlist)

def is_equal(list1,list2):
    list1=list1
    list2=list2
    while list1 is not None and list2 is not None:
                d1=list1.data
                d2=list2.data
                if d1==d2:
                     list1=list1.next
                     list2=list2.next
                else:
                     return False 
                     break
    return True                


print(is_equal(reverse, Linkedlist))


#method 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to reverse a linked list
def reverse(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to check if linked list is palindrome
def is_palindrome(head):
    if not head or not head.next:
        return True

    # Step 1: Find the middle of the linked list
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    second_half = reverse(slow)

    # Step 3: Compare both halves
    first_half = head
    second_half_copy = second_half  # To restore the list later
    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next

    # Optional Step 4: Restore the original list by reversing the second half back
    reverse(second_half_copy)

    return True

# Helper function to print the linked list
def print_list(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()

# Example usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print("Original Linked List:")
print_list(head)

if is_palindrome(head):
    print("\nThe linked list is a palindrome.")
else:
    print("\nThe linked list is not a palindrome.")
