def heapify(arr, n, i):

    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child
    # Check if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    # Check if right child of root exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:

        largest = right
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Heapify the affected sub-tree
        heapify(arr, n, largest)



# Example usage:

arr = [12, 11, 13, 5, 6, 7]

n = len(arr)


heapify(arr,n,0)
print(arr)

for i in range(n // 2 - 1, -1, -1):

    heapify(arr, n, i)



print("Max heap array is:", arr)