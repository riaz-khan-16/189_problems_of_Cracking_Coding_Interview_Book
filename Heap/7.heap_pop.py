# The pop operation in a heap typically removes the top element of the heap, which is
# either the maximum or minimum element depending on whether it's a max heap or min heap, 
#respectively. After removing the top element, the heap needs to be adjusted to maintain its heap property.


def pop_max_heap(heap):
    if len(heap) == 0:
        return None  # Heap is empty

    max_element = heap[0]
    heap[0] = heap[-1]  # Replace the root with the last element
    del heap[-1]  # Remove the last element
    _heapify_down_max(heap, 0)  # Heapify down from the root
    return max_element

def _heapify_down_max(heap, index):
    left_child_index = 2 * index + 1
    right_child_index = 2 * index + 2
    largest = index

    # Check if left child is larger than current node
    if left_child_index < len(heap) and heap[left_child_index] > heap[largest]:
        largest = left_child_index

    # Check if right child is larger than current node
    if right_child_index < len(heap) and heap[right_child_index] > heap[largest]:
        largest = right_child_index

    # If one of the children is larger, swap and continue heapifying down
    if largest != index:
        heap[largest], heap[index] = heap[index], heap[largest]
        _heapify_down_max(heap, largest)

# Example usage
heap = [15, 10, 5]
print("Before pop:", heap)
max_element = pop_max_heap(heap)
print("Max element popped:", max_element)
print("After pop:", heap)
