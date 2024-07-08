
nums = [7,7,5,7,7,7,1]
nums = [10,9,2,5,3,7,101,18]

#recursie method

def f(p,up):
    if not up:
        print(len(p))
        return len(p)
    if up[0]>p[-1]:
        f(p+[up[0]],up[1:])
        f(p,up[1:])
    else:
         f(p,up[1:])


#f([nums[0]],nums[1:])       

#dynamic Programming
nums =[4,10,4,3,8,9]
dp=[1]*(len(nums))
dp[0]=1

for i in range(1,len(nums)):
    for j in range(i):
        if nums[i]>nums[j]:
           dp[i] = max(dp[i], dp[j] + 1)


print(dp)     