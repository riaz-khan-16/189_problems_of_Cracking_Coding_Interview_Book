arr=[4,5,6,7,1,2,3]
n=len(arr)


def heapify_Min(arr,n, i):
    lowest=i
    left_child=2*i+1
    right_child=2*i+2

    if left_child<n and arr[left_child]<arr[lowest]:
        lowest=left_child
    if right_child<n and arr[right_child]<arr[lowest]:
        lowest=right_child
    if lowest != i:
        arr[i],arr[lowest]=arr[lowest],arr[i]
        heapify_Min(arr,n, lowest)

heapify_Min(arr,n,2)  
heapify_Min(arr,n,1)  
heapify_Min(arr,n,0)  

print(arr)
        


