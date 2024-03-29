def insert(heap,value):
        heap.append(value)
        i = len(heap) - 1
        parent=(i - 1) // 2
        while i > 0 and heap[parent] < heap[i]:
            heap[parent], heap[i] = heap[i], heap[parent]
            i = parent