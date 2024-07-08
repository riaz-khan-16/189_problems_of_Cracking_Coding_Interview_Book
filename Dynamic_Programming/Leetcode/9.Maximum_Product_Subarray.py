#https://leetcode.com/problems/maximum-product-subarray/description/

nums = [2,3,-2,4]

nums=[-1,-2,-3,-4,-5]


def f(nums):
    mx=1
    mn=1
    res=max(nums)
    for num in nums:
        temp=mx
        mx=max(mx*num,mn*num,num)
        mn=min(temp*num,mn*num,num)
        if mx>res:
            res=mx
    return res      

print(f(nums))      