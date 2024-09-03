flowerbed = [1,0,0,0,1,0,0,0,1]
n = 2



res=0
flowerbed=[0]+flowerbed+[0]
for i in range(1,len(flowerbed)-1):
    if flowerbed[i-1]==0 and flowerbed[i+1]==0 and flowerbed[i]!=1:
        flowerbed[i]=1
        res=res+1
print(res>=n)



