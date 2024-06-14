
# https://leetcode.com/problems/palindromic-substrings/

#Brute Force Approach
s='aa'
count=0
for i in range(1,len(s)+1):
    for k in range(0,len(s)-i+1):
        print(s[k:k+i])
        x=s[k:k+i]
        if x==x[::-1]:
          count=count+1
print(count)  
#time complexity O(N^3)



