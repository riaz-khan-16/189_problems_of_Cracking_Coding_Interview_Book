# Brute force algorithm

prices = [7,1,5,3,6,4]

best=0
l=0
r=1


while r<len(prices):
       if prices[l]<prices[r]:
              profit=prices[r]-prices[l]
              best=max(best,profit)
       else:
              l=r
       r=r+1
print(best)       