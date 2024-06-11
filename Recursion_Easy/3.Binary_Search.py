arr=[12]
target=12


def bsearch(s,e):
    mid=(s+e)//2
    if s>e:
        return -1
    elif arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return bsearch(s,mid-1)
    elif arr[mid]<target:
        return bsearch(mid+1,e)



x=bsearch(0,len(arr))    
print(x)    
