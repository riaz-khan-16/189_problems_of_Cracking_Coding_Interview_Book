# Bubble sort using Iterative approach


arr=[1,5,3,65,8,0,-1]

for i in range(len(arr)-1):

    for k in range(len(arr)-i-1):

        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
            
print(arr)