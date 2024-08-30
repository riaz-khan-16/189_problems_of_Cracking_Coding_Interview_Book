# https://leetcode.com/problems/squares-of-a-sorted-array/description/

nums = [-4,-1,0,3,10]

res=[]
l,r=0,len(nums)-1

while l<=r:
    if nums[l]*nums[l]>nums[r]*nums[r]:
        res.append(nums[l]*nums[l])
        l=l+1
    else:
        res.append(nums[r]*nums[r])
        r=r-1

print(res[::-1])


