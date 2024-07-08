#https://leetcode.com/problems/partition-equal-subset-sum/description/

nums = [1,5,11,5]

#find sum

sum=0
for i in nums:
    sum=sum+i
if sum%2==0:
    half_of_sum=sum/2
else:
    print(False)

def sub_set_sum(p,up):
    if p==half_of_sum:
        return True
    if p>half_of_sum:
        return False
    if not up:
        return False
    return sub_set_sum(p+up[0],up[1:]) or sub_set_sum(p,up[1:])
    


#Dynamic Programming

def dp(nums,target):

    res=set()
    res.add(0)
 
    for num in range(len(nums)-1,-1,-1):
        newDP=set()
        for i in res:
            newDP.add(i+nums[num])
            newDP.add(i)
        res=newDP  
    print(res)      
    return True if target in res else False

print(dp(nums,half_of_sum) )      








