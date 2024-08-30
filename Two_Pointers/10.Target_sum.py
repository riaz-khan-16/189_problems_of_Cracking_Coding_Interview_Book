#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/


# def bsearch(arr,target):
#     left=0
#     right=len(arr)-1
#     while left<=right:
#         mid=(left+right)//2
#         if arr[mid]==target:
#             return mid
#         if arr[mid]>target:
#             right=mid-1
#         if arr[mid]<target:
#             left=mid+1
#     return -1
def bsearch(left,right,target):

    while left<=right:
        mid=(left+right)//2
        if numbers[mid]==target:
            return mid
        if numbers[mid]>target:
            right=mid-1
        if numbers[mid]<target:
            left=mid+1
    return -1



    
numbers = [2,7,11,15]
target = 9
numbers =[5,25,75]
target = 100

numbers =[1,2,3,4,4,9,56,90]
target=8

def f(numbers,target):
    for i in range(len(numbers)):
        next_ele=target-numbers[i]
        next=bsearch(i+1,len(numbers)-1,next_ele)
        if next!=-1:
            return [i,next]
        
           
    
print(f(numbers,target))        

        
