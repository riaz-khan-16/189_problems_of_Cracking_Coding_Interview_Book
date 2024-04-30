 #minimum and maximum element of that array using recursion.

# https://www.geeksforgeeks.org/recursive-programs-to-find-minimum-and-maximum-elements-of-array/

arr = [1, 4, 3, 5, 4, 8, 6]

#find min
def fmin(arr):
    
    if len(arr)==1:
        print(arr[0])
        return arr[0]
    
    if arr[0]<arr[1]:
        arr[0],arr[1]=arr[1],arr[0]
        fmin(arr[1:])

    else:
       fmin(arr[1:])

fmin(arr)
def fmax(arr):
    
    if len(arr)==1:
        print(arr[0])
        return arr[0]
    
    if arr[0]>arr[1]:
        arr[0],arr[1]=arr[1],arr[0]
        fmax(arr[1:])

    else:
       fmax(arr[1:])

fmax(arr)       