
def heapify_Min(arr, i):
    lowest=i
    left_child=2*i+1
    right_child=2*i+2
    n=len(arr)
    if left_child<n and arr[left_child]<arr[lowest]:
        lowest=left_child
    if right_child<n and arr[right_child]<arr[lowest]:
        lowest=right_child
    if lowest != i:
        arr[i],arr[lowest]=arr[lowest],arr[i]
        heapify_Min(arr,lowest)
def pop_heap(heap):
    if len(heap) == 0:
        return None  # Heap is empty

    min_element = heap[0]
    heap[0] = heap[-1]  # Replace the root with the last element
    del heap[-1]  # Remove the last element
    heapify_Min(heap, 0)  # Heapify down from the root
   


class KthLargest:

    def __init__(self, k, nums):

        self.arr=nums
        self.k=k
        n=len(self.arr)

        for i in range(n // 2 - 1, -1, -1):

                    heapify_Min(self.arr, i)

        while len(self.arr)>k:
             pop_heap(self.arr)
             
        
    
    def add(self, val):

        if val>self.arr[0]:
             x=self.arr[0]
             self.arr[0]=val
             heapify_Min(self.arr, 0)

        
        return self.arr[0]


        
nums=[4, 5, 8, 2]
k=3

# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
param_1 = obj.add(1)
print(param_1)