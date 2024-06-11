

nums =[48,9,50,48,38,34,47,8,1,44,27,42,45,25,23,40,6,39,21,48]
nums=[1,1,1,1,1]
target =3

# def f(a,index,target):
#     if index==len(nums):
#         if a==target:
#            return 1
#         else:
#            return 0
    
#     left=f(a+nums[index],index+1,target)
#     right=f(a-nums[index],index+1,target)

#     return left+right

# x=f(0,0,target)
# print(x)


def f(p,up,target):
    if not up:
        if p==target:
            return 1
        else:
            return 0
         
    left=f(p+up[0],up[1:],target)
    right=f(p-up[0],up[1:],target)   

    return left+right

print(f(0,nums,target))

    
