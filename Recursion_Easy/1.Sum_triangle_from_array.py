# Sum triangle from array
# https://www.geeksforgeeks.org/sum-triangle-from-array/


arr=[1,2,3,4,5]

def SumTriangle(arr):
        if len(arr)==1:
            return
        new=[]
        for i in range(len(arr)-1):
              new.append(arr[i]+arr[i+1])
        print(new)
        SumTriangle(new)
SumTriangle(arr)
