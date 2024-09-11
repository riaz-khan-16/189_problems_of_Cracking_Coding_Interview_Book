#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
# weights = [3,2,2,4,1,4]
# days = 3
# weights = [1,2,3,1,1]
# days = 4


l=max(weights)
sum=0
for i in weights:
    sum=sum+i
r=sum

def simulate(least_wieght):

    x=0
    d=1
    for i in weights:
        x=x+i
        if x>least_wieght:
            x=i
            d=d+1
    return d<=days

res=[]
while l<=r:
    mid=(l+r)//2
    if simulate(mid):
        res.append(mid)
        r=mid-1
    else:
        l=mid+1
    
    

    

print(res)



