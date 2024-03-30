

def push_max_heap(heap, item):
    heap.append(item)
    _heapify_up_max(heap, len(heap) - 1)

def _heapify_up_max(heap, index):
    parent_index = (index - 1) // 2
    if parent_index >= 0 and heap[parent_index] < heap[index]:
        heap[parent_index], heap[index] = heap[index], heap[parent_index]
        _heapify_up_max(heap, parent_index)

# Example usage
heap = []
push_max_heap(heap, 10)
push_max_heap(heap, 5)
push_max_heap(heap, 15)

print(heap)  # Output: [15, 5, 10]


