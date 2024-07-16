nums = [1,3,5,4,7]


def dp(p,up):
    if not up:
        print(p)
        return

    if p and p[-1]<up[0]:
        dp(p+[up[0]],up[1:])
        dp(p,up[1:])
    if p and p[-1]>=up[0]:
        dp(p,up[1:])

  


dp([nums[0]],nums[1:])
