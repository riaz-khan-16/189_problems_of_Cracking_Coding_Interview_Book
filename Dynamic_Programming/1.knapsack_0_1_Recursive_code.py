wt=[1,3,4,5]
val=[1,4,5,7]
W=7


def knapscak(wt,val,W,n):
    # base condition

    if n==0 or W==0:
        return 0
    if wt[n-1]<=W:
        return max(val[n-1]+ knapscak(wt,val,W-wt[n-1],n-1),knapscak(wt,val,W,n-1))
    if wt[n-1]>W:
        return knapscak(wt,val,W,n-1)

n=len(wt)
print(knapscak(wt,val,W,n))