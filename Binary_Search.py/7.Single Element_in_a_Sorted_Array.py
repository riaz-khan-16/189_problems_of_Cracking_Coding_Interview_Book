nums = [1,1,2,2,3,3,4,4,7,8,8,13,13]



def bsearch1(nums):
    left,right=0,len(nums)-1

    while left<=right:
        mid=(left+right)//2

        if mid%2==0 and nums[mid]==nums[mid+1]:
            left=mid+1
        elif mid%2!=0 and nums[mid]==nums[mid-1]:
            left=mid+1
        else:
            right=mid-1
    
