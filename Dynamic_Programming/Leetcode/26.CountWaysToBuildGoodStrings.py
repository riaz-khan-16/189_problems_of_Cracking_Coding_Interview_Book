# https://leetcode.com/problems/count-ways-to-build-good-strings/description/

low = 3
high = 3
zero = 1
one = 1

low = 2
high = 3
zero = 1
one = 2

# zero='0'*zero
# one='1'* one

memo={}
def dp(p):

    if p in memo:
        return memo[p]
    if p>high:
        return 0
    if p==low and p<high:
        memo[p]= 1+dp(p+zero)+dp(p+one)
        return 1+dp(p+zero)+dp(p+one)
    if p==low==high:
        return 1
    if p==high:
        return 1
    memo[p]=dp(p+zero)+dp(p+one)
    return dp(p+zero)+dp(p+one)
res=dp(0)

print(res)
