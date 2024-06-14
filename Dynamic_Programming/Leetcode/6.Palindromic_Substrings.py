
# https://leetcode.com/problems/palindromic-substrings/

#1# Brute Force Approach
#time complexity O(N^3)
s='aa'

def brute_force(s):
    count=0
    for i in range(1,len(s)+1):
        for k in range(0,len(s)-i+1):
            print(s[k:k+i])
            x=s[k:k+i]
            if x==x[::-1]:
              count=count+1
    print(count)  
    return count

#2# Dynamic Programming

def dp(s):
    res=0
    for i in  range(len(s)):
        l=r=i
        while l>=0 and r<len(s) and s[l]==s[r]:
            res=res+1
            l=l-1
            r=r+1
        l=i
        r=i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            res=res+1
            l=l-1
            r=r+1
    print(res)        
    return res    

dp(s)








