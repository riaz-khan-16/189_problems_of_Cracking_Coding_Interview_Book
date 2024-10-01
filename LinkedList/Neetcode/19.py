class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head:
        return None
    
    # Create a dummy node to simplify edge cases where m = 1
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    
    # Move pre to the node before the `m-th` node
    for _ in range(m - 1):
        pre = pre.next
    
    # Start reversing the list from `m-th` node to `n-th` node
    current = pre.next
    prev = None
    for _ in range(n - m + 1):
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    
    # Reconnect the reversed part with the rest of the list
    pre.next.next = current
    pre.next = prev
    
    return dummy.next
