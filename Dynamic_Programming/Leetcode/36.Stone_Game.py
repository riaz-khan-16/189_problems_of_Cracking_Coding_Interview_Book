# 877. Stone Game


piles = [5,3,4,5]
piles = [5,5,6,6]
# piles = [3,7,2,3]
memo={}

def dp(alice, bob, start,end, isAlice):
        
        if start>end and alice>bob:
                return  True
        if start>end and alice<bob:
                return  False
        if start>end and alice==bob:
                return False
        
        if (alice,bob,start,end,isAlice) in memo:
                return memo[(alice,bob,start,end,isAlice)]
        if isAlice:
                memo[(alice,bob,start,end,isAlice)]=dp(alice+piles[start], bob,start+1,end, False) or dp(alice+piles[end], bob, start,end-1, False)
                return  memo[(alice,bob,start,end,isAlice)]
                
        if not isAlice:
                memo[(alice,bob,start,end,isAlice)]=dp(alice, bob+piles[start],start+1,end,True) or dp(alice, bob+piles[end],start,end-1,True)
                return memo[(alice,bob,start,end,isAlice)]

                
res=dp(0, 0, 0,len(piles)-1, True)    
print(res)          

