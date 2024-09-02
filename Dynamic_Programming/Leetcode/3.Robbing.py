#Leetcode 198

arr=[2,7,9,3,1]

arr = [1,2,3,1]
nums=arr =[2,1,1,2]


#memo
memo={}
def dp(i):
    if i>=len(nums):
        return 0
    if i in memo:
        return memo[i]
    include=nums[i]+dp(i+2)
    exclude=dp(i+1)
    memo[i]=max(include,exclude)
    return max(include,exclude)
print(dp(0))

#tabular

def dp(nums):
    a=0, b=0
    for i in nums:
        temp=max(a+i,b)
        a=b
        b=temp
    return b
