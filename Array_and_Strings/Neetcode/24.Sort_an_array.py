#https://leetcode.com/problems/sort-an-array/

# nums = [5,1,1,2,0,0]
nums = [5,2,3,1]


# at first we need to divide the array



def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left=merge_sort(left)
    right=merge_sort(right)
    return merge(left,right)

def merge(left,right):
    new=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i=i+1
        else:
            new.append(right[j])
            j=j+1
    while i<len(left):
        new.append(left[i])
        i=i+1
    while j<len(right):
        new.append(right[j])
        j=j+1
    return new 
  
x=merge_sort(nums)
print(x) 

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     left = merge_sort(left)
#     right = merge_sort(right)

#     return merge(left, right)

# def merge(left, right):
#     new = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             new.append(left[i])
#             i += 1
#         else:
#             new.append(right[j])
#             j += 1

#     while i < len(left):
#         new.append(left[i])
#         i += 1

#     while j < len(right):
#         new.append(right[j])
#         j += 1

#     return new

# merge_sort(nums)



