#https://leetcode.com/problems/design-linked-list/



class MyLinkedList(object):

    class Node:
        def __init__(self, next=None, val=0):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        curr = 0
        while curr < index:
            current = current.next
            curr += 1
        return current.val

    def addAtHead(self, val):
        new = self.Node(val=val)
        new.next = self.head
        self.head = new
        self.size += 1

    def addAtTail(self, val):
        if self.head is None:
            self.head = self.Node(val=val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = self.Node(val=val)
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val=val)
            return
        elif index == self.size:  # Handle adding at the tail
            self.addAtTail(val=val)
            return
        else:
            curr = 0
            current = self.head
            while curr < index - 1:
                current = current.next
                curr += 1
            new = self.Node(val=val)
            new.next = current.next
            current.next = new
        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = 0
            current = self.head
            while curr < index - 1:
                current = current.next
                curr += 1
            current.next = current.next.next
        self.size -= 1


# Example usage:
linked_list = MyLinkedList()
linked_list.addAtHead(1)
linked_list.addAtTail(3)
linked_list.addAtIndex(1, 2)  # Linked list becomes 1 -> 2 -> 3
print(linked_list.get(1))     # Output: 2
linked_list.deleteAtIndex(1)  # Now the list is 1 -> 3
print(linked_list.get(1))     # Output: 3

