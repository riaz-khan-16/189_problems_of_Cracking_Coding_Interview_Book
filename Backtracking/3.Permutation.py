#https://leetcode.com/problems/permutations/description/


nums = [1,2,3]

res=[]
def f(p,up):

    if not up:
        print(p)
        res.append(p)
        return
    for i in range(len(up)):
        f(p+[up[i]],up[0:i]+up[i+1:])

f([],nums)
print(res)