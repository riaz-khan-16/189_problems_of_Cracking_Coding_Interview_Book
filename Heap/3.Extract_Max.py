



def heapify(arr,n,i):
    largest = i  
    left = 2 * i + 1 
    right = 2 * i + 2  
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)

def extract_max(heap):
        if len(heap) == 0:
            return None
        max_val = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        heapify(heap,n-1,0)
        return max_val

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
for i in range(n//2-1,-1,-1):
     heapify(arr,n, i)
print(arr)

print(extract_max(arr)) 

print(arr)

     
     


