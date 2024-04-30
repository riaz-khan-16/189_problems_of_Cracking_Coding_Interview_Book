# Sum triangle from array
# https://www.geeksforgeeks.org/sum-triangle-from-array/


arr=[1,2,3,4,5]

def SumTriangle(arr):
        if len(arr)==1:
            return
        
        for i in range(len(arr)-1):
              arr[i]=arr[i]+arr[i+1]
        arr.pop      
        print(arr)
        SumTriangle(arr)
SumTriangle(arr)
