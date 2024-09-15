# https://leetcode.com/problems/koko-eating-bananas/description/

piles = [312884470]
h = 968709470
def simulate(m):
    hour=0
    for i in piles:
        if i%m!=0:
            hour=hour+i//m+1
        else:
            hour=hour+i//m
    if hour<=h:
        return True
    else:
        return False


l=1
r=max(piles)
ans=max(piles)
while l<=r:
    m=(l+r)//2
    if simulate(m):
        if m<ans:
            ans=m
        r=m-1
    else:
        l=m+1
print(ans)




