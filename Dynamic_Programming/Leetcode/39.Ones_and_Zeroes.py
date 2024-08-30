# 474. Ones and Zeroes

strs = ["10","0001","111001","1","0"]
m = 5
n = 3

memo={}

def recursive(index,rem_zeros,rem_ones):
     
     if index==len(strs) or (rem_zeros==0 and rem_ones==0):
          return 0
     if (index,rem_zeros,rem_ones) in memo:
         return memo[(index,rem_zeros,rem_ones)]
     zeros=strs[index].count('0')
     ones=strs[index].count('1')
     exclude=recursive(index+1,rem_zeros,rem_ones)

     include=0
     if rem_zeros>=zeros and rem_ones>=ones:
        include=1+recursive(index+1,rem_zeros-zeros,rem_ones-ones)
     memo[(index,rem_zeros,rem_ones)]=max(include,exclude)
     return max(include,exclude)
  
res=recursive(0,m,n)
print(res)


        